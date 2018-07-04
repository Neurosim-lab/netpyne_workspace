from neuron import h
from neuron import crxd as rxd
from matplotlib import pyplot as plt
from matplotlib_scalebar import scalebar

sec=h.Section()

# rxd parameters
caDiff = 0.08
ip3Diff = 1.41
cac_init = 1e-4
ip3_init = 0 # 1
gip3r = 12040 * 100
gserca = 0.3913
gleak = 6.020 
kserca = 0.1
kip3 = 0.15
kact = 0.4
ip3rtau = 2000 
fc = 0.8
fe = 0.2

# create Regions
cyt = rxd.Region(h.allsec(), nrn_region='i', geometry=rxd.FractionalVolume(fc, surface_fraction=1))
er = rxd.Region(h.allsec(), geometry=rxd.FractionalVolume(fe))
cyt_er_membrane = rxd.Region(h.allsec(), geometry=rxd.ScalableBorder(1, on_cell_surface=False))

# create Species 
ca = rxd.Species([cyt, er], d=caDiff, name='ca', charge=2, initial=cac_init)
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

# extracellular
x, y, z = [-10,200], [-10, 200], [-10, 1000]
cyt_extra = rxd.Region(h.allsec(), nrn_region='i')
rxd.options.enable.extracellular = True
extracellular = rxd.Extracellular(xlo=x[0], ylo=y[0], zlo=z[0], xhi=x[1], yhi=y[1], zhi=z[1], dx=5, volume_fraction=0.2, tortuosity=1.6) #vol_fraction and tortuosity associated w region 
na = rxd.Species([extracellular,cyt_extra], name= 'na', charge=1, d=1.78)
k = rxd.Species([extracellular, cyt_extra], name='k', charge=1, d =1.78)

# plot funcs
def plotExtracellularConcentration(extracellular=extracellular, species=k, plane='xz'):
    plt.figure()
    plane2mean = {'xz': 2, 'xy': 3}
    plt.imshow(species[extracellular].states3d[:].mean(plane2mean[plane]), interpolation='nearest', origin='upper')  #  extent=k[extracellular].extent('xy')
    sb = scalebar.ScaleBar(1e-6)
    sb.location='lower left'
    ax = plt.gca()
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    plt.xlabel(plane[0])
    plt.ylabel(plane[1])
    ax.add_artist(sb)
    plt.colorbar(label="$%s^+$ (mM)"%(species.name))
    plt.show()


