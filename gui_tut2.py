from netpyne import specs


# Network parameters
netParams = specs.NetParams()  # object of class NetParams to store the network parameters

## Cell property rules
netParams.importCellParams(label='PT', fileName='cells/PTcell.hoc', cellName='PTcell') 
netParams.importCellParams(label='SRI', fileName='cells/SRI.hoc', cellName='SRI') 

## Population parameters
netParams.popParams['E'] = {'cellType': 'PT', 'numCells': 3}
netParams.popParams['I'] = {'cellType': 'SRI', 'numCells': 3}


# Stimulation parameters
netParams.stimSourceParams['bkg'] = {'type': 'NetStim', 'rate': 40, 'noise': 0.0, 'start': 1}
netParams.stimTargetParams['bkg->PYR1'] = { 'source': 'bkg',
                                            'conds': {'pop': ['E']},
                                            'sec': 'apic_1',
                                            'synMech': 'AMPA',
                                            'weight': 0.2,
                                            'delay': 5}

# Synaptic mechanism parameters
netParams.synMechParams['AMPA'] = {'mod': 'Exp2Syn', 'tau1': 0.01, 'tau2': 0.5, 'e': 20}
netParams.synMechParams['GABA'] = {'mod': 'Exp2Syn', 'tau1': 0.1, 'tau2': 18, 'e': -90}


# Connectivity parameters
netParams.connParams['E->I'] = {
    'preConds': {'pop': 'E'},
    'postConds': {'pop': 'I'},
    'weight': 0.01,  # weight of each connection
    'delay': 5,     
    'synMech': 'AMPA',
    'sec': 'soma'}

netParams.connParams['I->E'] = {
     'preConds': {'pop': 'I'},
     'postConds': {'pop': ['E']},
     'weight': 0.01,                    # weight of each connection
     'delay': 5,     
     'synMech': 'GABA',
     'sec': 'soma'}


# Simulation options
simConfig = specs.SimConfig()		# object of class SimConfig to store simulation configuration

simConfig.duration = 0.5*1e3 			# Duration of the simulation, in ms
simConfig.dt = 0.1			# Internal integration timestep to use
simConfig.hParams['celsius'] = 34
simConfig.verbose = False  # Show detailed messages 
simConfig.recordTraces = {'V_soma':{'sec':'soma','loc':0.5,'var':'v'}}  # Dict with traces to record
simConfig.recordStep = 0.1 			# Step size in ms to save data (eg. V traces, LFP, etc)
simConfig.filename = 'model_output'  # Set file output name
simConfig.savePickle = False 		# Save params, network and sim output to pickle file

simConfig.analysis['iplotRaster'] =  {'markerSize': 5, 'showFig': True}
simConfig.analysis['iplotTraces'] = {'include': [0,4], 'oneFigPer': 'trace'}

from netpyne import sim
sim.createSimulateAnalyze()


