from netpyne import specs, sim

# Network parameters
netParams = specs.NetParams()  # object of class NetParams to store the network parameters


## Cell Parameters
secs = {}  # cell rule dict
secs['soma'] = {'geom': {}, 'mechs': {}}
secs['soma']['geom'] = {'diam': 18.8, 'L': 18.8, 'Ra': 123.0}
secs['soma']['mechs']['hh'] = {'gnabar': 0.12, 'gkbar': 0.036, 'gl': 0.003, 'el': -70}
netParams.cellParams['PYR'] = {'secs': secs}

## Population parameters
netParams.popParams['E'] = {'cellType': 'PYR', 'numCells': 20}
netParams.popParams['I'] = {'cellType': 'PYR', 'numCells': 20}


## Synaptic mechanism parameters
netParams.synMechParams['exc'] = {'mod': 'Exp2Syn', 'tau1': 0.1, 'tau2': 5.0, 'e': 0}  # excitatory synaptic mechanism
netParams.synMechParams['inh'] = {'mod': 'Exp2Syn', 'tau1': 0.1, 'tau2': 5.0, 'e': -70}  # inhibitory synaptic mechanism


# Stimulation parameters
netParams.stimSourceParams['bkg'] = {'type': 'NetStim', 'rate': 50, 'noise': 0.5}

netParams.stimTargetParams['bkg->PYR'] = {'source': 'bkg',
                                          'conds': {'pop': 'E'},
                                          'weight': 0.01,
                                          'delay': 5,
                                          'synMech': 'exc'}

## Cell connectivity rules
netParams.connParams['E->I'] = {        #  E -> I label
        'preConds': {'pop': 'E'},       # conditions of presyn cells
        'postConds': {'pop': 'I'},      # conditions of postsyn cells
        'divergence': 1,                # divergence
        'weight': 0.01,                 # synaptic weight
        'delay': 5,                     # transmission delay (ms)
        'synMech': 'exc'}               # synaptic mechanism
        
netParams.connParams['I->E'] = {        #  I -> E label
        'preConds': {'pop': 'I'},       # conditions of presyn cells
        'postConds': {'pop': 'E'},      # conditions of postsyn cells
        'probability': 0.7,             # probability
        'weight': 0.09,                 # synaptic weight
        'delay': 5,                     # transmission delay (ms)
        'synMech': 'inh'}               # synaptic mechanism


# Simulation options
simConfig = specs.SimConfig()           # object of class SimConfig to store simulation configuration

simConfig.duration = 1*1e3                      # Duration of the simulation, in ms
simConfig.dt = 0.025                            # Internal integration timestep to use
simConfig.verbose = False                       # Show detailed messages
simConfig.recordTraces = {'V_soma': {'sec':'soma','loc':0.5, 'var':'v'}}  # Dict with traces to record
simConfig.recordStep = 0.1                      # Step size in ms to save data (e.g. V traces, LFP, etc)
simConfig.filename = 'model_output'             # Set file output name
simConfig.savePickle = False                    # Save params, network and sim output to pickle file

simConfig.analysis['plotTraces'] = {'include': [1]}                           # Plot recorded traces for this list of cells
simConfig.analysis['plotRaster'] = {'orderInverse': True, 'syncLines': True}  # Plot a raster
simConfig.analysis['plotSpikeHist'] = {'include': ['E', 'I']}                 # Plot spike histogram
simConfig.analysis['plotRateSpectrogram'] = {'include': ['allCells']}         # Plot binned spiking rate spectrogram    


# Play around with model and see how parameters affect oscillations, e.g.:
# - set I->E connection probability to 0.0 (set back to 0.7 afterwards)
# - increase I->E connection delay to 20 ms (set back to 5 ms afterwards) 
# - increase 'inh' synapse tau2 time constatn to 20 ms (set back to 5 ms afterwards)