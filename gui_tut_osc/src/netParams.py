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

# Play around with model and see how parameters affect oscillations, e.g.:
# - set I->E connection probability to 0.0 (set back to 0.7 afterwards)
# - increase I->E connection delay to 20 ms (set back to 5 ms afterwards) 
# - increase 'inh' synapse tau2 time constatn to 20 ms (set back to 5 ms afterwards)
