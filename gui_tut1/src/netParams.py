from netpyne import specs

# Network parameters
netParams = specs.NetParams()  # object of class NetParams to store the network parameters

## Cell parameters
secs = {}	# dict with section info
secs['soma'] = {'geom': {}, 'mechs': {}}
secs['soma']['geom'] = {'diam': 12, 'L': 12, 'Ra': 100.0, 'cm': 1}  	 						# soma geometry
secs['soma']['mechs']['hh'] = {'gnabar': 0.12, 'gkbar': 0.036, 'gl': 0.0003, 'el': -54.3} 		# soma hh mechanism

secs['dend'] = {'geom': {}, 'mechs': {}}
secs['dend']['geom'] = {'diam': 1.0, 'L': 200.0, 'Ra': 100.0, 'cm': 1}
secs['dend']['topol'] = {'parentSec': 'soma', 'parentX': 1.0, 'childX': 0}						# dend geometry
secs['dend']['mechs']['pas'] = {'g': 0.001, 'e': -70} 		 		                            # dend pas mechanism

netParams.cellParams['pyr'] = {'secs': secs}  												    # add dict to list of cell parameters
	
## Population parameters
netParams.popParams['E'] = {'cellType': 'pyr', 'numCells': 40}

 # Stimulation parameters
netParams.stimSourceParams['IClamp1'] = {'type': 'IClamp', 'dur': 5, 'del': 20, 'amp': 0.1}
netParams.stimTargetParams['IClamp1->cell0'] = {'source': 'IClamp1', 'conds': {'cellList':[0]}, 'sec':'dend', 'loc':1.0}


# Synaptic mechanism parameters
netParams.synMechParams['exc'] = {'mod': 'Exp2Syn', 'tau1': 0.1, 'tau2': 1.0, 'e': 0}


# Connectivity parameters
netParams.connParams['E->E'] = {
    'preConds': {'pop': 'E'},
    'postConds': {'pop': 'E'},
    'weight': 0.005,                    # weight of each connection
    'probability': 0.1,
    'delay': 5,     # delay min=0.2, mean=13.0, var = 1.4
    'synMech': 'exc',
    'sec': 'dend'}
