from netpyne import specs

#------------------------------------------------------------------------------
#
# SIMULATION CONFIGURATION
#
#------------------------------------------------------------------------------

# Run parameters
simConfig = specs.SimConfig()       # object of class simConfig to store simulation configuration
simConfig.duration = 1.0*1e3        # Duration of the simulation, in ms
simConfig.hParams['v_init'] = -65   # set v_init to -65 mV
simConfig.dt = 0.1                  # Internal integration timestep to use
simConfig.verbose = False            # Show detailed messages 
simConfig.recordStep = 1             # Step size in ms to save data (eg. V traces, LFP, etc)
simConfig.filename = 'rxd_net'   # Set file output name

 # Network dimensions
simConfig.sizeX = 100
simConfig.sizeY = 500
simConfig.sizeZ = 100

# Recording/plotting parameters
simConfig.recordTraces = {'V_soma':{'sec': 'soma','loc': 0.5,'var': 'v'},
                          'ik_soma': {'sec': 'soma', 'loc': 0.5, 'var': 'ik'},
                          'cai_soma': {'sec': 'soma', 'loc':0.5, 'var': 'cai'},
                          'cao_soma': {'sec': 'soma', 'loc':0.5, 'var': 'cao'}}

simConfig.recordLFP = [[-15, y, 1.0*simConfig.sizeZ] for y in range(int(simConfig.sizeY/3), int(simConfig.sizeY), int(simConfig.sizeY/3))]

simConfig.analysis['plotTraces']={'include': [0]}
simConfig.analysis['plotRaster'] = {'orderBy': 'y', 'orderInverse': True, 'saveFig': True, 'figSize': (9,3)}      # Plot a raster
simConfig.analysis['plotLFP'] = {'includeAxon': False, 'figSize': (6,10), 'NFFT': 256, 'noverlap': 48, 'nperseg': 64, 'saveFig': True} 
simConfig.analysis['plotRxDConcentration'] = {'speciesLabel': 'ca', 'regionLabel': 'ecs'}

# parameters
## Change ip3_init from 0 to 0.1 to observe multiscale effect:  
## high ip3 -> ER Ca released to Cyt -> kBK channels open -> less firing 
simConfig.ip3_init = 0.0  