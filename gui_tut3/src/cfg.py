from netpyne import specs
from src.netParams import netParams

#------------------------------------------------------------------------------
#
# SIMULATION CONFIGURATION
#
#------------------------------------------------------------------------------

# Run parameters
cfg = specs.SimConfig()       # object of class simConfig to store simulation configuration
cfg.duration = 1.0*1e3        # Duration of the simulation, in ms
cfg.hParams['v_init'] = -65   # set v_init to -65 mV
cfg.dt = 0.1                  # Internal integration timestep to use
cfg.verbose = False            # Show detailed messages 
cfg.recordStep = 1             # Step size in ms to save data (eg. V traces, LFP, etc)
cfg.filename = 'rxd_net'   # Set file output name


# Recording/plotting parameters
cfg.recordTraces = {'V_soma':{'sec': 'soma','loc': 0.5,'var': 'v'},
                          'ik_soma': {'sec': 'soma', 'loc': 0.5, 'var': 'ik'},
                          'cai_soma': {'sec': 'soma', 'loc':0.5, 'var': 'cai'},
                          'cao_soma': {'sec': 'soma', 'loc': 0.5, 'var': 'cao'}}

cfg.recordLFP = [[-15, y, 1.0*netParams.sizeZ] for y in range(int(netParams.sizeY/3), int(netParams.sizeY), int(netParams.sizeY/3))]

cfg.analysis['iplotTraces'] ={'include': [0]}
cfg.analysis['iplotRaster'] = {'orderBy': 'y', 'orderInverse': True, 'saveFig': True, 'figSize': (9,3)}      # Plot a raster
cfg.analysis['iplotLFP'] = {'includeAxon': False, 'figSize': (6,10), 'saveFig': True} 
cfg.analysis['iplotRxDConcentration'] = {'speciesLabel': 'ca', 'regionLabel': 'ecs'}
