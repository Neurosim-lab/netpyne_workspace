from netpyne import specs


#------------------------------------------------------------------------------
#
# NETWORK PARAMETERS
#
#------------------------------------------------------------------------------

netParams = specs.NetParams()  # object of class NetParams to store the network parameters

netParams.sizeX = 100 # x-dimension (horizontal length) size in um
netParams.sizeY = 500 # y-dimension (vertical height or cortical depth) size in um
netParams.sizeZ = 100 # z-dimension (horizontal length) size in um
netParams.propVelocity = 100.0 # propagation velocity (um/ms)
netParams.probLengthConst = 150.0 # length constant for conn probability (um)

#------------------------------------------------------------------------------
## Cell parameters
netParams.loadCellParams(label='E', fileName='cells/CSTR_cellParams.json')
netParams.importCellParams(label='I', fileName='cells/FScell.hoc', cellName='FScell')


#------------------------------------------------------------------------------
## Population parameters
netParams.popParams['E2'] = {'cellType': 'E', 'numCells': 10, 'yRange': [50,150]}
netParams.popParams['I2'] = {'cellType': 'I', 'numCells': 10, 'yRange': [50,150]}
netParams.popParams['E4'] = {'cellType': 'E', 'numCells': 10, 'yRange': [150,300]}
netParams.popParams['I4'] = {'cellType': 'I', 'numCells': 10, 'yRange': [150,300]}
netParams.popParams['E5'] = {'cellType': 'E', 'numCells': 10, 'ynormRange': [0.6,1.0]}
netParams.popParams['I5'] = {'cellType': 'I', 'numCells': 10, 'ynormRange': [0.6,1.0]}

#------------------------------------------------------------------------------
## Synaptic mechanism parameters
netParams.synMechParams['exc'] = {'mod': 'Exp2Syn', 'tau1': 0.8, 'tau2': 5.3, 'e': 0}  # NMDA synaptic mechanism
netParams.synMechParams['inh'] = {'mod': 'Exp2Syn', 'tau1': 0.6, 'tau2': 8.5, 'e': -75}  # GABA synaptic mechanism

#------------------------------------------------------------------------------
# Stimulation parameters
netParams.stimSourceParams['bkg'] = {'type': 'NetStim', 'rate': 20, 'noise': 0.3}
netParams.stimTargetParams['bkg->E'] = {'source': 'bkg', 'conds': {'cellType': ['E']}, 'weight': 0.02, 'sec': 'soma', 'delay': 'max(1, normal(5,2))', 'synMech': 'exc'}
netParams.stimTargetParams['bkg->I'] = {'source': 'bkg', 'conds': {'cellType': ['I']}, 'weight': 0.004, 'sec': 'soma', 'delay': 'max(1, normal(5,2))', 'synMech': 'exc'}

#------------------------------------------------------------------------------
# Cell connectivity rules
netParams.connParams['E->all'] = {
  'preConds': {'cellType': 'E'}, 'postConds': {'y': [50,500]},  #  E -> all (100-1000 um)
  'probability': 0.1,                  # probability of connection
  'weight': '0.04*post_ynorm',         # synaptic weight 
  'delay': 'dist_3D/propVelocity',      # transmission delay (ms) 
  'synMech': 'exc'}                     # synaptic mechanism 

netParams.connParams['I->E'] = {
  'preConds': {'cellType': 'I'}, 'postConds': {'pop': ['E2','E4','E5']},       #  I -> E
  'probability': '0.3*exp(-dist_3D/probLengthConst)',   # probability of connection
  'weight': 0.01,                                      # synaptic weight 
  'delay': 'dist_3D/propVelocity',                      # transmission delay (ms) 
  'sec': ['soma','Bdend'], 
  'synMech': 'inh'}                                     # synaptic mechanism
