from neuron import rxd, h, gui
from matplotlib import pyplot

sec = h.Section(name='sec')
sec.L = 100
sec.diam = 1
sec.nseg = 100

caDiff = 0.08
ip3Diff = 1.41
cac_init = 1.e-4
ip3_init = 0.1
gip3r = 12040
gserca = 0.3913
gleak = 6.020
kserca = 0.1
kip3 = 0.15
kact = 0.4
ip3rtau = 2000
fc = 0.8
fe = 0.2

cyt = rxd.Region(h.allsec(), nrn_region='i', geometry=rxd.FractionalVolume(fc, surface_fraction=1))
er = rxd.Region(h.allsec(), geometry=rxd.FractionalVolume(fe))
cyt_er_membrane = rxd.Region(h.allsec(), geometry=rxd.ScalableBorder(1, on_cell_surface=False))

ca = rxd.Species([cyt, er], d=caDiff, name='ca', charge=2, initial=cac_init)
ip3 = rxd.Species(cyt, d=ip3Diff, initial=ip3_init)
ip3r_gate_state = rxd.State(cyt_er_membrane, initial=0.8)

h_gate = ip3r_gate_state[cyt_er_membrane]

serca = rxd.MultiCompartmentReaction(ca[cyt], ca[er], gserca / ((kserca / (1000. * ca[cyt])) ** 2 + 1), membrane=cyt_er_membrane, custom_dynamics=True)
leak = rxd.MultiCompartmentReaction(ca[er], ca[cyt], gleak, gleak, membrane=cyt_er_membrane)

minf = ip3[cyt] * 1000. * ca[cyt] / (ip3[cyt] + kip3) / (1000. * ca[cyt] + kact)
k = gip3r * (minf * h_gate) ** 3
ip3r = rxd.MultiCompartmentReaction(ca[er], ca[cyt], k, k, membrane=cyt_er_membrane)
ip3rg = rxd.Rate(h_gate, (1. / (1 + 1000. * ca[cyt] / (0.3)) - h_gate) / ip3rtau)

h.finitialize(-65)

h.dt *= 10

cae_init = (0.0017 - cac_init * fc) / fe
ca[er].concentration = cae_init

for node in ip3.nodes:
    if node.x < 0.2:
        node.concentration = 2

for t in range(0, 501, 50):
	h.continuerun(t)
	print(t)
	pyplot.plot(ca[cyt].concentration)

pyplot.show()	