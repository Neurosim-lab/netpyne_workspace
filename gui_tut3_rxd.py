from netpyne import specs, sim
from neuron import rxd, h, gui

# --------------------------------
# Network parameters
# --------------------------------

netParams = specs.NetParams()  # object of class NetParams to store the network parameters

netParams.sizeX = 200 # x-dimension (horizontal length) size in um
netParams.sizeY = 1000 # y-dimension (vertical height or cortical depth) size in um
netParams.sizeZ = 200 # z-dimension (horizontal length) size in um
netParams.propVelocity = 100.0 # propagation velocity (um/ms)
netParams.probLengthConst = 150.0 # length constant for conn probability (um)

## Population parameters
netParams.popParams['E2'] = {'cellType': 'E', 'numCells': 1, 'yRange': [100,300], 'cellModel': 'HH'}
# netParams.popParams['I2'] = {'cellType': 'I', 'numCells': 1, 'yRange': [100,300], 'cellModel': 'HH'}
# netParams.popParams['E4'] = {'cellType': 'E', 'numCells': 1, 'yRange': [300,600], 'cellModel': 'HH'}
# netParams.popParams['I4'] = {'cellType': 'I', 'numCells': 1, 'yRange': [300,600], 'cellModel': 'HH'}
# netParams.popParams['E5'] = {'cellType': 'E', 'numCells': 1, 'ynormRange': [0.6,1.0], 'cellModel': 'HH'}
# netParams.popParams['I5'] = {'cellType': 'I', 'numCells': 1, 'ynormRange': [0.6,1.0], 'cellModel': 'HH'}

## Cell property rules
netParams.loadCellParamsRule(label='CellRule', fileName='cells/IT2_reduced_cellParams.json')
netParams.cellParams['CellRule']['conds'] = {'cellType': ['E','I']}

## increase conducante of calcium-related channels  
'''
kBK - hyperpolarizing, + ica, ca flows out = cai decreases
cat - depolarizing, -ica, ca flows in = cai increases -- uses ghk eqn but can't get to be affected by concetration

'''
caInc = 10 # 1000
caMechParams = {'cal': ['gcalbar', caInc], 'can': ['gcanbar', caInc], 'cat': ['gcatbar', caInc], 'kBK': ['gpeak', caInc]} #cal 0.0005 can 0.0001 cat 0.00075
secs = ['soma', 'Adend1', 'Adend2', 'Adend3', 'Bdend']
for k,v in caMechParams.iteritems():
    for sec in secs:
        netParams.cellParams['CellRule']['secs']['soma']['mechs'][k][v[0]] *= v[1]
        
# remove channels
removeMechs = ['cadad', 'cat', 'cal', 'can']#, 'nax']
secs = ['soma', 'Adend1', 'Adend2', 'Adend3', 'Bdend']
for mech in removeMechs:
    for sec in secs:
        del netParams.cellParams['CellRule']['secs'][sec]['mechs'][mech]
 




## Synaptic mechanism parameters
netParams.synMechParams['exc'] = {'mod': 'Exp2Syn', 'tau1': 0.8, 'tau2': 5.3, 'e': 0}  # NMDA synaptic mechanism
netParams.synMechParams['inh'] = {'mod': 'Exp2Syn', 'tau1': 0.6, 'tau2': 8.5, 'e': -75}  # GABA synaptic mechanism

# Stimulation parameters
netParams.stimSourceParams['bkg'] = {'type': 'NetStim', 'rate': 40, 'noise': 0.3}
netParams.stimTargetParams['bkg->all'] = {'source': 'bkg', 'conds': {'cellType': ['E','I']}, 'weight': 10.0, 'sec': 'soma', 'delay': 'max(1, normal(5,2))', 'synMech': 'exc'}

## Cell connectivity rules
netParams.connParams['E->all'] = {
  'preConds': {'cellType': 'E'}, 'postConds': {'y': [100,1000]},  #  E -> all (100-1000 um)
  'probability': 0.1 ,                  # probability of connection
  'weight': '5.0*post_ynorm',         # synaptic weight 
  'delay': 'dist_3D/propVelocity',      # transmission delay (ms) 
  #'sec': ['Bdend','Adend1', 'Adend2'],
  'synMech': 'exc'}                     # synaptic mechanism 

netParams.connParams['I->E'] = {
  'preConds': {'cellType': 'I'}, 'postConds': {'pop': ['E2','E4','E5']},       #  I -> E
  'probability': '0.4*exp(-dist_3D/probLengthConst)',   # probability of connection
  'weight': 1.0,                                      # synaptic weight 
  'delay': 'dist_3D/propVelocity',                      # transmission delay (ms) 
  #'sec': ['Bdend','Adend1', 'Adend2'],
  'synMech': 'inh'}                                     # synaptic mechanism 



# --------------------------------
# Simulation configuration
# --------------------------------
simConfig = specs.SimConfig()        # object of class SimConfig to store simulation configuration
simConfig.duration = 1.0*1e3           # Duration of the simulation, in ms
simConfig.hParams['v_init'] = -65  # set v_init to -65 mV
simConfig.dt = 0.1                # Internal integration timestep to use
simConfig.verbose = False            # Show detailed messages 
simConfig.recordStep = 1             # Step size in ms to save data (eg. V traces, LFP, etc)
simConfig.filename = 'net_lfp'   # Set file output name
simConfig.recordTraces = {'V_soma':{'sec': 'soma','loc': 0.5,'var': 'v'},
                          'cai_soma': {'sec': 'soma', 'loc':0.5, 'var': 'cai'},
                          'cao_soma': {'sec': 'soma', 'loc':0.5, 'var': 'cao'},
                          'ik_soma': {'sec': 'soma', 'loc':0.5, 'var': 'ik'}}  # Dict with traces to record
                          # 'V_Adend3':{'sec': 'Adend3','loc': 0.5,'var': 'v'},
                          # 'cai_Adend3': {'sec': 'Adend3', 'loc':0.5, 'var': 'cai'},
                          # 'ica_Adend3': {'sec': 'Adend3', 'loc':0.5, 'var': 'ica'}}  # Dict with traces to record

simConfig.recordLFP = [[-15, y, 1.0*netParams.sizeZ] for y in range(netParams.sizeY/5, netParams.sizeY, netParams.sizeY/5)]

simConfig.analysis['plotTraces']={'include': [0]}
simConfig.analysis['plotRaster'] = {'orderBy': 'y', 'orderInverse': True, 'saveFig':False, 'figSize': (9,3)}      # Plot a raster
#simConfig.analysis['plotLFP'] = {'includeAxon': False, 'figSize': (6,10), 'NFFT': 256, 'noverlap': 48, 'nperseg': 64, 'saveFig': False} 

createSimulate = True
if createSimulate:
    # --------------------------------
    # Instantiate network
    # --------------------------------
    sim.create()

    # --------------------------------
    # Add RxD
    # --------------------------------
    addRxD = True
    if addRxD:
        caDiff = 0.08
        ip3Diff = 1.41
        cac_init = 1e-5 # 1.e-4
        ip3_init = 0.0
        gip3r = 12040 * 1e3
        gserca = 0.3913
        gleak = 6.020 * 0.01 #1e6 #100
        kserca = 0.1
        kip3 = 0.15
        kact = 0.4
        ip3rtau = 2000 
        fc = 0.8
        fe = 0.2

        cyt = rxd.Region(h.allsec(), nrn_region='i', geometry=rxd.FractionalVolume(fc, surface_fraction=1))
        er = rxd.Region(h.allsec(), geometry=rxd.FractionalVolume(fe))
        cyt_er_membrane = rxd.Region(h.allsec(), geometry=rxd.ScalableBorder(1, on_cell_surface=False))

        ca = rxd.Species([cyt, er], d=caDiff, name='ca', charge=2, initial=cac_init)
        ip3 = rxd.Species(cyt, d=ip3Diff, name='ip3', initial=ip3_init)
        ip3r_gate_state = rxd.State(cyt_er_membrane, initial=0.8)

        h_gate = ip3r_gate_state[cyt_er_membrane]

        # serca = rxd.MultiCompartmentReaction(ca[cyt], ca[er], gserca / ((kserca / (1000. * ca[cyt])) ** 2 + 1), membrane=cyt_er_membrane, custom_dynamics=True)
        # leak = rxd.MultiCompartmentReaction(ca[er], ca[cyt], gleak, gleak, membrane=cyt_er_membrane)

        minf = ip3[cyt] * 1000. * ca[cyt] / (ip3[cyt] + kip3) / (1000. * ca[cyt] + kact)
        k = gip3r * (minf * h_gate) ** 3
        ip3r = rxd.MultiCompartmentReaction(ca[er], ca[cyt], k, k, membrane=cyt_er_membrane)
        ip3rg = rxd.Rate(h_gate, (1. / (1 + 1000. * ca[cyt] / (0.3)) - h_gate) / ip3rtau)

        # v_init and dt set via netpyne
        # h.finitialize(-65)  
        # h.dt *= 10



        def init_rxd(ca, ip3, cac_init, fc, fe):
            cae_init = (0.0017 - cac_init * fc) / fe 
            ca[er].concentration = cae_init

            # for node in ip3.nodes:
            #   if node.x > 0.5:
            #       node.concentration = 2

            # for node in ip3.nodes:
            #     print node.concentration

        sim.fih.append(h.FInitializeHandler((init_rxd, (ca, ip3, cac_init, fc, fe))))


  # ######################### start RYR ####################################################################################
  # ### RYR - based on Sneyd et al, 2003
  # if dconf['useRYR']:
  #   # constants
  #   k_a_pos = 1500000000000.0 # mM^-4/ms
  #   k_a_neg = 0.0288 # /ms
  #   k_b_pos = 1500000000.0 # mM^-3/ms
  #   k_b_neg = 0.3859 # /ms
  #   k_c_pos = 0.00175 # /ms
  #   k_c_neg = 0.0001 # /ms
  #   v1ryr = dconf['v1ryr'] # /ms
  #   Ka_4 = k_a_neg / k_a_pos # Ka**4
  #   Kb_3 = k_b_neg / k_b_pos # Kb**3
  #   Kc = k_c_neg / k_c_pos
  #   # w_state is fraction of RYR not in C2 state (closed state), ie fraction of RYR that is open
  #   # w_infinity - equ: 29 
  #   #w_inf = (1+(Ka_4/(ca[cyt]**4))+((ca[cyt]**3)/Kb_3)) / (1+(1/Kc)+(Ka_4/(ca[cyt]**4)) + ((ca[cyt]**3)/Kb_3))
  #   c3ryr = (ca[cyt]**3)/Kb_3; 
  #   c4ryr = Ka_4/(ca[cyt]**4);
  #   w_inf = (1.0 + c4ryr + c3ryr) / (1.0+(1.0/Kc)+ c4ryr + c3ryr)
  #   w_state = rxd.State(cyt_er_membrane, initial=0.9999) # 0)#0.9999) # check if initial == 0???? or can put it as w_inf
  #   # equ:  8 (which is the same as equ 22)
  #   #w_rate = rxd.Rate(w_state, k_c_neg * (w_inf - w_state[cyt_er_membrane]) / w_inf)
  #   w_rate = rxd.Rate(w_state, 1.0 - w_state[cyt_er_membrane] / w_inf)
  #   # P_ryr - gating variable - equ: 7 (which is the same as 27)
  #   # (open probability)
  #   #ryr_gate = w_state[cyt_er_membrane] * (1 + (ca[cyt]**3 / Kb_3)) / (1+(Ka_4/ca[cyt]**4) + (ca[cyt]**3/Kb_3))
  #   ryr_gate = w_state[cyt_er_membrane] * (1.0 + c3ryr) / (1.0 + c4ryr + c3ryr)
  #   # the following is extracted from equ 9 and 15
  #   k_ryr = v1ryr*ryr_gate
  #   ryr = rxd.MultiCompartmentReaction(ca[er]<>ca[cyt], k_ryr, k_ryr, membrane=cyt_er_membrane)
  # ######################### end RYR ####################################################################################



    # --------------------------------
    # Add extracellular
    # --------------------------------
    addExtra = False
    if addExtra:
        cyt = rxd.Region(h.allsec(), nrn_region='i')
        rxd.options.enable.extracellular = True
        extracellular = rxd.Extracellular(xlo=-2, ylo=-300, zlo=-2, xhi = 300, yhi =0, zhi =100, dx=5, volume_fraction=0.2, tortuosity=1.6) #vol_fraction and tortuosity associated w region 
        rxd_na = rxd.Species([extracellular,cyt], name= 'na', charge= 1, d=1.78)
        rxd_k = rxd.Species([extracellular, cyt], name = 'k', charge = 1, d =1.78)
        h.finitialize()
        print 'initial state %g' % rxd_na[extracellular].states3d.mean()
        na = rxd_na[cyt]
        k = rxd_k[cyt]
        na_ecs = rxd_na[extracellular]
        k_ecs = rxd_k[extracellular]
        na_ecs.states3d[:] = 140
        k_ecs.states3d[:] = 4
        rxd_na[extracellular].states3d[:] = h.nao0_na_ion
        rxd_k[extracellular].states3d[:] = h.ko0_k_ion


    # --------------------------------
    # Simulate and analyze network
    # --------------------------------

    sim.simulate()
    sim.analyze()


for node in ip3.nodes:
    print node.concentration

# Create network and run simulation
#sim.createSimulateAnalyze(netParams = netParams, simConfig = simConfig)    
