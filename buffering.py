from neuron import h, rxd, gui
from matplotlib import pyplot

# morphology (a single section)
soma = h.Section(name='soma')

# specify the reaction
cyt = rxd.Region(h.allsec(), nrn_region='i')
ca = rxd.Species(cyt, initial=1, name='ca', charge=2)
buf = rxd.Species(cyt, initial=1, name='buf')
cabuf = rxd.Species(cyt, initial=0, name='cabuf')
kf = 1
kb = 0.1
buffering = rxd.Reaction(2 * ca + buf, cabuf, kf, kb)

# in NEURON 7.4, need to initialize before we can grab pointers via soma
h.finitialize()

# setup recording
t_vec, ca_vec, buf_vec, cabuf_vec = h.Vector(), h.Vector(), h.Vector(), h.Vector()
t_vec.record(h._ref_t)
ca_vec.record(soma(0.5)._ref_cai)
buf_vec.record(soma(0.5)._ref_bufi)
cabuf_vec.record(soma(0.5)._ref_cabufi)

# run the simulation until default tstop
h.run()

# plot everything
pyplot.plot(t_vec, ca_vec, label='ca')
pyplot.plot(t_vec, buf_vec, label='buf')
pyplot.plot(t_vec, cabuf_vec, label='cabuf')
pyplot.legend()
pyplot.xlim([0, max(t_vec)])
pyplot.xlabel('t (ms)')
pyplot.ylabel('Concentration (mM)')
pyplot.show()