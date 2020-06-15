from netpyne import specs

# Network parameters
netParams = specs.NetParams()  # object of class NetParams to store the network parameters

## Cell parameters
secs = {}	# dict with section info
secs['soma'] = {'geom': {}, 'mechs': {}}
secs['soma']['geom'] = {'diam': 20, 'L': 20, 'Ra': 100.0, 'cm':1}  	 									# soma geometry
secs['soma']['mechs']['hh'] =  {'gnabar': 0.12, 'gkbar': 0.036, 'gl': 0.003, 'el': -70} 		# soma hh mechanism
secs['dend']['geom'] = {'diam': 5.0, 'L': 150.0, 'Ra': 100.0, 'cm': 1}
secs['dend']['topol'] = {'parentSec': 'soma', 'parentX': 1.0, 'childX': 0}										# soma geometry
secs['dend']['mechs']['pas'] =  {'g': 0.0004, 'e': -70} 		 		# soma hh mechanism
netParams.cellParams['PYR'] = {'secs': secs}  												# add dict to list of cell parameters

	

## Population parameters
netParams.popParams['E'] = {'cellType': 'pyr', 'numCells': 20, 'cellModel':''}

 # Stimulation parameters
netParams.stimSourceParams['IClamp1'] = {'type': 'IClamp', 'dur': 10, 'del': 20, 'amp':0.6}
netParams.stimTargetParams['IClamp1->cell0'] = {'source': 'IClamp1', 'conds': {'cellList':[0]}, 'sec':'dend', 'loc':1.0}


# Synaptic mechanism parameters
netParams.synMechParams['exc'] = {'mod': 'Exp2Syn', 'tau1': 0.1, 'tau2': 1.0, 'e': 0}


# Connectivity parameters
netParams.connParams['E->E'] = {
    'preConds': {'pop': 'E'}, 'postConds': {'pop': 'E'},
    'weight': 0.03,                    # weight of each connection
    'probability': 0.3,
    'delay': 5,     # delay min=0.2, mean=13.0, var = 1.4
    'synMech': 'exc',
    'sec': 'soma'}

# Simulation options
simConfig = specs.SimConfig()		# object of class SimConfig to store simulation configuration

simConfig.duration = 0.2*1e3 			# Duration of the simulation, in ms
simConfig.dt = 0.1 				# Internal integration timestep to use
simConfig.verbose = False  			# Show detailed messages 
simConfig.recordTraces = {'V_soma':{'sec':'soma','loc':0.5,'var':'v'},
						 'V_dend': {'sec': 'dend', 'loc': 1.0, 'var':'v'}}  # Dict with traces to record
simConfig.recordStep = 1 			# Step size in ms to save data (eg. V traces, LFP, etc)
simConfig.filename = 'gui_tut1'  # Set file output name
simConfig.saveJson = False		# Save params, network and sim output to pickle file
simConfig.analysis['plotTraces'] = {'include': [0]}

netpyne_geppetto.netParams=netParams
netpyne_geppetto.simConfig=simConfig