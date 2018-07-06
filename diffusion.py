from neuron import h, rxd, gui
from matplotlib import pyplot

# morphology (a single section)
dend = h.Section(name='dend')
dend.L = 101
dend.nseg = 101

# initialization rule
def ip3_initializer(node):
	if 0.4 <= node.x <= 0.6:
		return 1e-3 # 1e-3 mM = 1 uM
	else:
		return 0

# specify the diffusion problem
cyt = rxd.Region([dend], nrn_region='i')
ip3 = rxd.Species(cyt, initial=ip3_initializer, name='ip3', d=1)

# in NEURON 7.4, need to initialize before we can grab pointers via dend
h.finitialize()

# setup recording at dend(0.7)
t_vec, ip3_vec = h.Vector(), h.Vector()
t_vec.record(h._ref_t)
ip3_vec.record(dend(0.7)._ref_ip3i)

# run for a while
h.tstop = 200
h.run()

# sanity check: if we've ran it long enough, [ip3] will have started to decrease
# as the system approaches equilibrium
assert(max(ip3_vec) > ip3_vec[-1])

# find all times above 1e-4 mM = 100 nM
threshold = 1e-4
times_above_threshold = t_vec.as_numpy()[(ip3_vec.as_numpy() > threshold)]

# display results
print 'First above threshold at t = %g' % times_above_threshold[0]
print 'Peak ip3:', max(ip3_vec)

# plot voltage vs time
pyplot.figure(figsize=(8,4)) # Default figsize is (8,6)
pyplot.plot(t_vec, ip3_vec)
pyplot.xlabel('time (ms)')
pyplot.ylabel('ip3 (mM)')
pyplot.show()
