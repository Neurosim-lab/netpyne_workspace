from netpyne import specs


# Network parameters
netParams = specs.NetParams()  # object of class NetParams to store the network parameters

## Cell property rules
netParams.importCellParams(label='PYR', fileName='cells/PTcell.hoc', cellName='PTcell', somaAtOrigin=True) 
netParams.importCellParams(label='INT', fileName='cells/SRI.hoc', cellName='SRI') 

## Population parameters
netParams.popParams['E'] = {'cellType': 'PYR', 'numCells': 2}
netParams.popParams['I'] = {'cellType': 'INT', 'numCells': 2}


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
    'weight': 0.015,  # weight of each connection
    'delay': 5,     
    'synMech': 'AMPA',
    'sec': 'soma'}

netParams.connParams['I->E'] = {
     'preConds': {'pop': 'I'},
     'postConds': {'pop': ['E']},
     'weight': 0.015,                    # weight of each connection
     'delay': 5,     
     'synMech': 'GABA',
     'sec': 'soma'}
