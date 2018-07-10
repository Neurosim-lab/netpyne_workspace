from neuron import h
from neuron import crxd as rxd

# ---------------------
# rxd intracellular and extracellular
# ---------------------

rxd.nthread(4)

# parameters
ip3_init = 0  # Change value between 0 and 1: high ip3 -> ER Ca released to Cyt -> kBK channels open -> less firing
caDiff = 0.08  # calcium diffusion coefficient
ip3Diff = 1.41  # ip3 diffusion coefficient
caci_init = 1e-5  # intracellular calcium initial concentration
caco_init = 2.0   # extracellular calcium initial concentration
gip3r = 12040 * 100  # ip3 receptors density
gserca = 0.3913  # SERCA conductance
gleak = 6.020   # ER leak channel conductance
kserca = 0.1  # SERCA reaction constant
kip3 = 0.15  # ip3 reaction constant
kact = 0.4  #
ip3rtau = 2000  # ip3 receptors time constant
fc = 0.8  # fraction of cytosol
fe = 0.2  # fraction of ER
margin = 20  # extracellular volume additional margin 
x, y, z = [0-margin, 100+margin], [-500-margin, 0+margin], [0-margin, 100+margin]

# create intracellular region
cyt = rxd.Region(h.allsec(), nrn_region='i', geometry=rxd.FractionalVolume(fc, surface_fraction=1))
er = rxd.Region(h.allsec(), geometry=rxd.FractionalVolume(fe))
cyt_er_membrane = rxd.Region(h.allsec(), geometry=rxd.ScalableBorder(1, on_cell_surface=False))

# create extracellular region
rxd.options.enable.extracellular = True
extracellular = rxd.Extracellular(xlo=x[0], ylo=y[0], zlo=z[0], xhi=x[1], yhi=y[1], zhi=z[1], dx=5, volume_fraction=0.2, tortuosity=1.6) #vol_fraction and tortuosity associated w region 

# create Species 
ca = rxd.Species([cyt, er, extracellular], d=caDiff, name='ca', charge=2, 
      initial=lambda nd: caco_init if isinstance(nd,rxd.node.NodeExtracellular) else (0.0017 - caci_init * fc) / fe if nd.region == er else caci_init)
ip3 = rxd.Species(cyt, d=ip3Diff, name='ip3', initial=ip3_init)
ip3r_gate_state = rxd.State(cyt_er_membrane, initial=0.8)

# create Reactions 
serca = rxd.MultiCompartmentReaction(ca[cyt], ca[er], gserca / ((kserca / (1000. * ca[cyt])) ** 2 + 1), membrane=cyt_er_membrane, custom_dynamics=True)
leak = rxd.MultiCompartmentReaction(ca[er], ca[cyt], gleak, gleak, membrane=cyt_er_membrane)

minf = ip3[cyt] * 1000. * ca[cyt] / (ip3[cyt] + kip3) / (1000. * ca[cyt] + kact)
h_gate = ip3r_gate_state[cyt_er_membrane]
kip3 = gip3r * (minf * h_gate) ** 3
ip3r = rxd.MultiCompartmentReaction(ca[er], ca[cyt], kip3, kip3, membrane=cyt_er_membrane)
ip3rg = rxd.Rate(h_gate, (1. / (1 + 1000. * ca[cyt] / (0.3)) - h_gate) / ip3rtau)



