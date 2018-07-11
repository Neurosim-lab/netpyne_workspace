from netpyne import specs


# Network parameters
netParams = specs.NetParams()  # object of class NetParams to store the network parameters

## Population parameters
netParams.popParams['E'] = {'cellType': 'PT', 'numCells': 3, 'cellModel':''}
netParams.popParams['I'] = {'cellType': 'FS', 'numCells': 3, 'cellModel':''}


## Cell property rules
netParams.importCellParams(label='PT_rule', conds={'cellType': 'PT'}, fileName='cells/PTcell.hoc', cellName='PTcell') 
#netParams.importCellParams(label='FS_rule', conds={'cellType': 'FS'}, fileName='cells/FS3.hoc', cellName='FScell') 

# Stimulation parameters
netParams.stimSourceParams['bkg'] = {'type': 'NetStim', 'rate': 40, 'noise': 0.0, 'start': 1}
netParams.stimTargetParams['bkg->PYR1'] = {'source': 'bkg', 'sec': 'soma', 'conds': {'pop': ['E']}, 'weight': 0.12, 'delay': 5}


# Synaptic mechanism parameters
netParams.synMechParams['AMPA'] = {'mod': 'Exp2Syn', 'tau1': 0.5, 'tau2': 1.0, 'e': 0}
netParams.synMechParams['GABA'] = {'mod': 'Exp2Syn', 'tau1': 0.5, 'tau2': 1.0, 'e': -120}


# Connectivity parameters
netParams.connParams['E->I'] = {
    'preConds': {'pop': 'E'}, 'postConds': {'pop': ['I']},
    'weight': 0.03,                    # weight of each connection
    'delay': 5,     
    'synMech': 'AMPA',
    'sec': 'soma'}

netParams.connParams['I->E'] = {
     'preConds': {'pop': 'I'}, 'postConds': {'pop': ['E']},
     'weight': 0.4,                    # weight of each connection
     'delay': 15,     
     'synMech': 'GABA',
     'sec': 'soma'}


# Simulation options
simConfig = specs.SimConfig()		# object of class SimConfig to store simulation configuration

simConfig.duration = 0.5*1e3 			# Duration of the simulation, in ms
simConfig.dt = 0.1			# Internal integration timestep to use
simConfig.verbose = False  			# Show detailed messages 
simConfig.recordTraces = {'V_soma':{'sec':'soma','loc':0.5,'var':'v'}}  # Dict with traces to record
simConfig.recordStep = 1 			# Step size in ms to save data (eg. V traces, LFP, etc)
simConfig.filename = 'model_output'  # Set file output name
simConfig.savePickle = False 		# Save params, network and sim output to pickle file
simConfig.recordCells = [0]

#simConfig.analysis['plotSpikeHist'] =  {'include': ['E','I'], 'yaxis': 'count'}
simConfig.analysis['plotTraces']={'include': [0,4], 'oneFigPer': 'trace'}

# from netpyne import sim
# sim.createSimulateAnalyze()


