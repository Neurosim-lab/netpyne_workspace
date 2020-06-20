from netpyne import specs


# Network parameters
netParams = specs.NetParams()  # object of class NetParams to store the network parameters

## Cell property rules
netParams.importCellParams(label='PT', fileName='../cells/PTcell.hoc', cellName='PTcell') 
netParams.importCellParams(label='FS', fileName='../cells/FScell.hoc', cellName='FScell') 

## Population parameters
netParams.popParams['E'] = {'cellType': 'PT', 'numCells': 3, 'yNormRange': [0.2, 0.4]}
netParams.popParams['I'] = {'cellType': 'FS', 'numCells': 3, 'yNormRange': [0.6, 0.8]}


# Stimulation parameters
netParams.stimSourceParams['bkg'] = {'type': 'NetStim', 'rate': 40, 'noise': 0.2, 'start': 1}
netParams.stimTargetParams['bkg->PYR1'] = {'source': 'bkg', 'sec': 'apic_1', 'conds': {'pop': ['E']}, 'weight': 0.1, 'delay': 5}


# Synaptic mechanism parameters
netParams.synMechParams['AMPA'] = {'mod': 'Exp2Syn', 'tau1': 0.5, 'tau2': 1.0, 'e': 0}
netParams.synMechParams['GABA'] = {'mod': 'Exp2Syn', 'tau1': 0.5, 'tau2': 1.0, 'e': -90}


# Connectivity parameters
netParams.connParams['E->I'] = {
    'preConds': {'pop': 'E'},
    'postConds': {'pop': ['I']},
    'weight': 0.03,                    # weight of each connection
    'delay': 5,     
    'synMech': 'AMPA',
    'sec': 'soma'}

netParams.connParams['I->E'] = {
     'preConds': {'pop': 'I'},
     'postConds': {'pop': ['E']},
     'weight': 0.4,                    # weight of each connection
     'delay': 10,     
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

simConfig.analysis['iplotSpikeHist'] =  {'include': ['E','I'], 'yaxis': 'count', 'showFig': True}
simConfig.analysis['iplotTraces'] = {'include': [0,4], 'oneFigPer': 'trace'}

from netpyne import sim
sim.createSimulateAnalyze()


