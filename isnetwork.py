import sys; sys.path.insert(1,'/usr/site/nrniv/local/python/netpyne')
from netpyne import specs, sim
from neuron import rxd, h
from neuron import *


# Network paramaters - volume dimensions where cells will be placed 
netParams = specs.NetParams()    #object of class NetParams to store the network parameters 
netParams.sizeX = 300   # x-dimension (horizontal length) size in um 
netParams.sizeY = 300   # y-dimension (vertical height or cortical depth)  size in um
netParams.sizeZ = 100    # z-dimension(hotizontal length) size in um 
netParams.propVelocity = 100.0  # propogation velocity (um/ms)    connectivity 
netParams.probLengthConst = 15.0  # length constant for conn probability (um)   connectivity rules

## Population parameters -- 10 locations for 100 cells 
netParams.popParams['E2'] = {'cellType': 'E', 'numCells':50, 'yRange':[1,150],'xRange':[0,150],'cellModel':'HH'}
netParams.popParams['I2'] = {'cellType': 'I', 'numCells':50, 'yRange':[1,150],'xRange':[0,150],'cellModel':'HH'}
netParams.popParams['E3'] = {'cellType': 'E', 'numCells':50, 'yRange':[1,150],'xRange':[150,300], 'cellModel':'HH'}
netParams.popParams['I3'] = {'cellType': 'I', 'numCells':50, 'yRange':[1,150],'xRange':[150,300], 'cellModel':'HH'}
netParams.popParams['E4'] = {'cellType': 'E', 'numCells':50, 'yRange':[150,300],'xRange':[150,300],'cellModel':'HH'}
netParams.popParams['I4'] = {'cellType': 'I', 'numCells':50, 'yRange':[150,300],'xRange':[0,150],'cellModel': 'HH'}
netParams.popParams['E5'] = {'cellType': 'E', 'numCells':50, 'yRange':[150,300],'xRange':[150,300],'cellModel': 'HH'}
netParams.popParams['E5'] = {'cellType': 'I', 'numCells':50, 'yRange':[150,300],'xRange':[150,300], 'cellModel': 'HH'}
netParams.popParams['E6'] = {'cellType': 'E', 'numCells': 50, 'yRange': [150,300],'xRange':[0,150], 'cellModel': 'HH'}
netParams.popParams['I6'] = {'cellType': 'I', 'numCells': 50, 'yRange': [150,300], 'xRange':[0,150],'cellModel': 'HH'}

## Cell property rules
cellRule = {'conds': {'cellType': 'E'},  'secs': {}}  # cell rule dict
cellRule['secs']['soma'] = {'geom': {}, 'mechs': {}}                              # soma params dict
cellRule['secs']['soma']['geom'] = {'diam': 15, 'L': 14, 'Ra': 120.0}                   # soma geometry
cellRule['secs']['soma']['mechs']['hh'] = {'gnabar': 0.13, 'gkbar': 0.036, 'gl': 0.003, 'el': -70}      # soma hh mechanism
netParams.cellParams['Erule'] = cellRule                          # add dict to list of cell params

cellRule = {'conds': {'cellType': 'I'},  'secs': {}}  # cell rule dict
cellRule['secs']['soma'] = {'geom': {}, 'mechs': {}}                              # soma params dict
cellRule['secs']['soma']['geom'] = {'diam': 10.0, 'L': 9.0, 'Ra': 110.0}                  # soma geometry
cellRule['secs']['soma']['mechs']['hh'] = {'gnabar': 0.11, 'gkbar': 0.036, 'gl': 0.003, 'el': -70}      # soma hh mechanism
netParams.cellParams['Irule'] = cellRule                          # add dict to list of cell params

for label in ['Erule', 'Irule']: # set 3D pt geom
			offset, prevL = 0, 0
			for secName, sec in netParams.cellParams[label]['secs'].iteritems():
				sec['geom']['pt3d'] = []
				if secName in ['soma', 'Adend1', 'Adend2', 'Adend3']:  # set 3d geom of soma and Adends
					sec['geom']['pt3d'].append([offset+0, prevL, 0, sec['geom']['diam']])
					prevL = float(prevL + sec['geom']['L'])
					sec['geom']['pt3d'].append([offset+0, prevL, 0, sec['geom']['diam']])
				if secName in ['Bdend']:  # set 3d geom of Bdend
					sec['geom']['pt3d'].append([offset+0, 0, 0, sec['geom']['diam']])
					sec['geom']['pt3d'].append([offset+sec['geom']['L'], 0, 0, sec['geom']['diam']])		
				if secName in ['axon']:  # set 3d geom of axon
					sec['geom']['pt3d'].append([offset+0, 0, 0, sec['geom']['diam']])
					sec['geom']['pt3d'].append([offset+0, -sec['geom']['L'], 0, sec['geom']['diam']])
## Synaptic mechanism parameters
netParams.synMechParams['exc'] = {'mod': 'Exp2Syn', 'tau1': 0.8, 'tau2': 5.3, 'e': 0}  # NMDA synaptic mechanism
netParams.synMechParams['inh'] = {'mod': 'Exp2Syn', 'tau1': 0.6, 'tau2': 8.5, 'e': -75}  # GABA synaptic mechanism

# Stimulation parameters
netParams.stimSourceParams['bkg'] = {'type': 'NetStim', 'rate': 20, 'noise': 0.3}
netParams.stimTargetParams['bkg->all'] = {'source': 'bkg', 'conds': {'cellType': ['E','I']}, 'weight': 0.01, 'delay': 'max(1, normal(5,2))', 'synMech': 'exc'}
# Simulation options
simConfig = specs.SimConfig()        # object of class SimConfig to store simulation configuration

simConfig.duration = 1*1e3           # Duration of the simulation, in ms
simConfig.dt = 0.05                 # Internal integration timestep to use
simConfig.verbose = False            # Show detailed messages
simConfig.recordTraces = {}
simConfig.recordTraces['V_soma']={'sec':'soma','loc':0.5,'var':'v'}  # Dict with traces to record
simConfig.recordTraces['nai']= {'sec': 'soma', 'loc': 0.5, 'var': 'nai'} #record the nai concentration
simConfig.recordTraces['ki']= {'sec': 'soma', 'loc': 0.5, 'var': 'ki'}   #record the ki concentration
simConfig.recordTraces['nao']= {'sec': 'soma', 'loc': 0.5, 'var': 'nao'}
simConfig.recordTraces['ko'] = {'sec': 'soma', 'loc': 0.5, 'var': 'ko'}
simConfig.recordStep = 1             # Step size in ms to save data (e.g. V traces, LFP, etc)
simConfig.filename = 'model_output'  # Set file output name
simConfig.savePickle = False         # Save params, network and sim output to pickle file
simConfig.analysis['plotRaster'] = {'orderBy': 'y', 'orderInverse': True}      # Plot a raster
simConfig.analysis['plotTraces'] = {'include': [('E2',0), ('E4', 0), ('E5', 5), ('I2',0)]}      # Plot recorded traces for this list of cells
simConfig.analysis['plot2Dnet'] = True           # plot 2D visualization of cell positions and connections
simConfig.analysis['plotConn'] = True           # plot connectivity matrix
# simConfig.analysis['plot2Dnet'] = {'include': ['allcells'],'figSize':(12,12), 'view':'xy', 'showConns': True, 'showFig':True}

# Create network and run simulation w Rxd 

sim.create() 
cyt = rxd.Region(h.allsec(), nrn_region='i')
rxd.options.enable.extracellular = True
extracellular = rxd.Extracellular(xlo=-2, ylo=-300, zlo=-2, xhi = 300, yhi =0, zhi =100, dx=5, volume_fraction=0.2, tortuosity=1.6) #vol_fraction and tortuosity associated w region 
rxd_na = rxd.Species([extracellular,cyt], name= 'na', charge= 1, d=1.78)
rxd_k = rxd.Species([extracellular, cyt], name = 'k', charge = 1, d =1.78)
h.finitialize()
print 'initial state %g' % rxd_na[extracellular].states3d.mean()
na = rxd_na[cyt]
k = rxd_k[cyt]
na_ecs = rxd_na[extracellular]
k_ecs = rxd_k[extracellular]
na_ecs.states3d[:] = 140
k_ecs.states3d[:] = 4
rxd_na[extracellular].states3d[:] = h.nao0_na_ion
rxd_k[extracellular].states3d[:] = h.ko0_k_ion


sim.simulate()
sim.analyze()

print 'initial state %g' % rxd_na[extracellular].states3d.mean()

from matplotlib import pyplot
from matplotlib_scalebar import scalebar

sb = scalebar.ScaleBar(1e-6)
sb.location='lower left'
pyplot.imshow(k[extracellular].mean(2), extent=k[extracellular].extent('xy'), interpolation='nearest', origin='lower')
pyplot.colorbar()
sb = scalebar.ScaleBar(1e-6)
sb.location='lower left'
ax = pyplot.gca()
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
ax.add_artist(sb)
pyplot.colorbar(label="$K^+$ (mM)")