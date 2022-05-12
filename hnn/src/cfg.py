"""
cfg.py 

Simulationg configuration for NetPyNE-based HNN network model

Contributors: salvadordura@gmail.com
"""

from netpyne import specs

cfg = specs.SimConfig()

cfg.checkErrors = False # True # leave as False to avoid extra printouts


# ############################################################################
#
# SIMULATION CONFIGURATION
#
# ############################################################################

# ----------------------------------------------------------------------------
#
# NetPyNE config parameters (not part of original HNN implementation)
#
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# Run parameters
# ----------------------------------------------------------------------------
cfg.duration = 170
cfg.dt = 0.025
cfg.seeds = {'conn': 4321, 'stim': 1234, 'loc': 4321} 
cfg.hParams['v_init'] = -65  
cfg.verbose = 0
cfg.cvode_active = False
cfg.printRunTime = 0.1
cfg.printPopAvgRates = True
cfg.distributeSynsUniformly = False  # one syn per section in list of sections
cfg.allowSelfConns = False  # allow connections from a cell to itself
cfg.allowConnsWithWeight0 = False  # do not allow conns with weight 0 (faster)
cfg.oneSynPerNetcon = False  # allow using the same synapse for multiple netcons


# ----------------------------------------------------------------------------
# Recording 
# ----------------------------------------------------------------------------
cfg.recordTraces = {'V_soma': {'sec': 'soma', 'loc': 0.5, 'var': 'v'}}
cfg.recordCells = [('L2Basket',0), ('L2Pyr',0), ('L5Basket',0), ('L5Pyr',0)]  
cfg.recordStims = False  
cfg.recordStep = 0.025
cfg.recordDipoles = {'L2': ['L2Pyr'], 'L5': ['L5Pyr']}

# cfg.recordLFP = [[50, 50, 50], [50, 1300, 50]]

# ----------------------------------------------------------------------------
# Saving
# ----------------------------------------------------------------------------
cfg.sim_prefix = cfg.simLabel = 'default'

cfg.saveFolder = '.'
cfg.savePickle = False
cfg.saveJson = False
cfg.saveDataInclude = ['simData', 'simConfig'] #, 'netParams', 'net']

# ----------------------------------------------------------------------------
# Analysis and plotting 
# ----------------------------------------------------------------------------
pops = ['L2Basket', 'L2Pyr', 'L5Basket', 'L5Pyr']
evprox = ['evokedProximal_1_L2Basket', 'evokedProximal_1_L2Pyr', 'evokedProximal_1_L5Basket', 'evokedProximal_1_L5Pyr',
  'evokedProximal_2_L2Basket', 'evokedProximal_2_L2Pyr', 'evokedProximal_2_L5Basket', 'evokedProximal_2_L5Pyr']
evdist = ['evokedDistal_1_L2Basket', 'evokedDistal_1_L2Pyr', 'evokedDistal_1_L5Basket', 'evokedDistal_1_L5Pyr']

popColors = {'L2Basket': [0.0, 0.0, 0.0], 'L2Pyr': [0.0, 0.6, 0.0], 'L5Basket': [0.0, 0.0, 1.0], 'L5Pyr': [1.0, 0.0, 0.0],
    'Evoked proximal': [0.0, 1.0, 1.0], 'Evoked distal': [1.0, 1.0, 0.0]}

cfg.analysis['iplotTraces'] = {'include': [('L5Pyr',0) ], 'oneFigPer': 'cell', 'saveFig': False, 
							  'showFig': True, 'timeRange': [0, cfg.duration]}

cfg.analysis['iplotRaster'] = {'include': pops, 'showFig': True, 'popColors': popColors, 'markerSize': 6, 'orderInverse': True}

cfg.analysis['iplotSpikeHist'] = {'include': [*pops, evprox, evdist, 'extRhythmicProximal', 'extRhythmicDistal'], 'legendLabels': pops + ['Evoked proximal', 'Evoked distal', 'Rhythmic proximal', 'Rhythmic distal'], 'popColors': popColors, 'yaxis': 'count', 'showFig': True}

cfg.analysis['iplotDipole'] = {'showFig': True}

cfg.analysis['iplotDipolePSD'] = {'showFig': True, 'maxFreq': 80}  # change freq to 40 for alpha&beta tut

cfg.analysis['iplotDipoleSpectrogram'] = {'showFig': True, 'maxFreq': 80} # change freq to 40 for alpha&beta tut

cfg.analysis['iplotConn'] = {'includePre': pops, 'includePost': pops, 'feature': 'strength'}

# cfg.analysis['iplotLFP'] = {'showFig': True}

#cfg.analysis['iplotRatePSD'] = {'include': pops, 'showFig': True}


# ----------------------------------------------------------------------------
# Network parameters
# ----------------------------------------------------------------------------
cfg.gridSpacingPyr = 1  # 50
cfg.gridSpacingBasket = [1, 1, 3]  
cfg.xzScaling = 1 #100
cfg.sizeY = 2000 

cfg.localConn = True
cfg.rhythmicInputs = True
cfg.evokedInputs = True
cfg.tonicInputs = True
cfg.poissonInputs = True
cfg.gaussInputs = True


# ----------------------------------------------------------------------------
#
# HNN original config parameters (adapted to NetPyNE)
#
# ----------------------------------------------------------------------------

# Params from 'ERPYes100Trials.param'; copied from cfg.__dict__
cfg.__dict__.update({
 'duration': 170.0,
 'tstop': 170,
 'dt': 0.05,
 'hParams': {'celsius': 37, 'v_init': -65, 'clamp_resist': 0.001},
 'cache_efficient': False,
 'cvode_active': False,
 'cvode_atol': 0.001,
 'seeds': {'conn': 4321, 'stim': 1234, 'loc': 4321},
 'rand123GlobalIndex': None,
 'createNEURONObj': True,
 'createPyStruct': True,
 'addSynMechs': True,
 'includeParamsLabel': True,
 'gatherOnlySimData': False,
 'compactConnFormat': False,
 'connRandomSecFromList': True,
 'distributeSynsUniformly': False,
 'pt3dRelativeToCellLocation': True,
 'invertedYCoord': True,
 'allowSelfConns': False,
 'allowConnsWithWeight0': False,
 'oneSynPerNetcon': False,
 'saveCellSecs': True,
 'saveCellConns': True,
 'timing': True,
 'saveTiming': False,
 'printRunTime': 0.1,
 'printPopAvgRates': True,
 'printSynsAfterRule': False,
 'verbose': 0,
 'recordCells': [('L2Basket', 0), ('L2Pyr', 0), ('L5Basket', 0), ('L5Pyr', 0)],
 'recordTraces': {'V_soma': {'sec': 'soma', 'loc': 0.5, 'var': 'v'}},
 'recordCellsSpikes': -1,
 'recordStim': False,
 'recordLFP': [],
 'recordDipoles': {'L2': ['L2Pyr'], 'L5': ['L5Pyr']},
 'saveLFPCells': False,
 'recordStep': 0.05,
 'recordTime': True,
 'simLabel': 'default',
 'saveFolder': '.',
 'filename': './default',
 'saveDataInclude': ['simData', 'simConfig'],
 'timestampFilename': False,
 'savePickle': False,
 'saveJson': False,
 'saveMat': False,
 'saveCSV': False,
 'saveDpk': False,
 'saveHDF5': False,
 'saveDat': False,
 'backupCfgFile': [],
 'checkErrors': False,
 'checkErrorsVerbose': False,
 'recordStims': False,
 'sim_prefix': 'ERPYes100Trials',
 'gridSpacingPyr': 1,
 'gridSpacingBasket': [1, 1, 3],
 'xzScaling': 1,
 'sizeY': 2000,
 'localConn': True,
 'rhythmicInputs': True,
 'evokedInputs': True,
 'tonicInputs': True,
 'poissonInputs': True,
 'gaussInputs': True,
 'EEgain': 1.0,
 'EIgain': 1.0,
 'IEgain': 1.0,
 'IIgain': 1.0,
 'celsius': 37.0,
 'threshold': 0.0,
 'L2Pyr_soma_L': 22.1,
 'L2Pyr_soma_diam': 23.4,
 'L2Pyr_soma_cm': 0.6195,
 'L2Pyr_soma_Ra': 200.0,
 'L2Pyr_dend_cm': 0.6195,
 'L2Pyr_dend_Ra': 200.0,
 'L2Pyr_apicaltrunk_L': 59.5,
 'L2Pyr_apicaltrunk_diam': 4.25,
 'L2Pyr_apical1_L': 306.0,
 'L2Pyr_apical1_diam': 4.08,
 'L2Pyr_apicaltuft_L': 238.0,
 'L2Pyr_apicaltuft_diam': 3.4,
 'L2Pyr_apicaloblique_L': 340.0,
 'L2Pyr_apicaloblique_diam': 3.91,
 'L2Pyr_basal1_L': 85.0,
 'L2Pyr_basal1_diam': 4.25,
 'L2Pyr_basal2_L': 255.0,
 'L2Pyr_basal2_diam': 2.72,
 'L2Pyr_basal3_L': 255.0,
 'L2Pyr_basal3_diam': 2.72,
 'L2Pyr_ampa_e': 0.0,
 'L2Pyr_ampa_tau1': 0.5,
 'L2Pyr_ampa_tau2': 5.0,
 'L2Pyr_nmda_e': 0.0,
 'L2Pyr_nmda_tau1': 1.0,
 'L2Pyr_nmda_tau2': 20.0,
 'L2Pyr_gabaa_e': -80.0,
 'L2Pyr_gabaa_tau1': 0.5,
 'L2Pyr_gabaa_tau2': 5.0,
 'L2Pyr_gabab_e': -80.0,
 'L2Pyr_gabab_tau1': 1.0,
 'L2Pyr_gabab_tau2': 20.0,
 'L2Pyr_soma_gkbar_hh2': 0.01,
 'L2Pyr_soma_gnabar_hh2': 0.18,
 'L2Pyr_soma_el_hh2': -65.0,
 'L2Pyr_soma_gl_hh2': 4.26e-05,
 'L2Pyr_soma_gbar_km': 250.0,
 'L2Pyr_dend_gkbar_hh2': 0.01,
 'L2Pyr_dend_gnabar_hh2': 0.15,
 'L2Pyr_dend_el_hh2': -65.0,
 'L2Pyr_dend_gl_hh2': 4.26e-05,
 'L2Pyr_dend_gbar_km': 250.0,
 'L5Pyr_soma_L': 39.0,
 'L5Pyr_soma_diam': 28.9,
 'L5Pyr_soma_cm': 0.85,
 'L5Pyr_soma_Ra': 200.0,
 'L5Pyr_dend_cm': 0.85,
 'L5Pyr_dend_Ra': 200.0,
 'L5Pyr_apicaltrunk_L': 102.0,
 'L5Pyr_apicaltrunk_diam': 10.2,
 'L5Pyr_apical1_L': 680.0,
 'L5Pyr_apical1_diam': 7.48,
 'L5Pyr_apical2_L': 680.0,
 'L5Pyr_apical2_diam': 4.93,
 'L5Pyr_apicaltuft_L': 425.0,
 'L5Pyr_apicaltuft_diam': 3.4,
 'L5Pyr_apicaloblique_L': 255.0,
 'L5Pyr_apicaloblique_diam': 5.1,
 'L5Pyr_basal1_L': 85.0,
 'L5Pyr_basal1_diam': 6.8,
 'L5Pyr_basal2_L': 255.0,
 'L5Pyr_basal2_diam': 8.5,
 'L5Pyr_basal3_L': 255.0,
 'L5Pyr_basal3_diam': 8.5,
 'L5Pyr_ampa_e': 0.0,
 'L5Pyr_ampa_tau1': 0.5,
 'L5Pyr_ampa_tau2': 5.0,
 'L5Pyr_nmda_e': 0.0,
 'L5Pyr_nmda_tau1': 1.0,
 'L5Pyr_nmda_tau2': 20.0,
 'L5Pyr_gabaa_e': -80.0,
 'L5Pyr_gabaa_tau1': 0.5,
 'L5Pyr_gabaa_tau2': 5.0,
 'L5Pyr_gabab_e': -80.0,
 'L5Pyr_gabab_tau1': 1.0,
 'L5Pyr_gabab_tau2': 20.0,
 'L5Pyr_soma_gkbar_hh2': 0.01,
 'L5Pyr_soma_gnabar_hh2': 0.16,
 'L5Pyr_soma_el_hh2': -65.0,
 'L5Pyr_soma_gl_hh2': 4.26e-05,
 'L5Pyr_soma_gbar_ca': 60.0,
 'L5Pyr_soma_taur_cad': 20.0,
 'L5Pyr_soma_gbar_kca': 0.0002,
 'L5Pyr_soma_gbar_km': 200.0,
 'L5Pyr_soma_gbar_cat': 0.0002,
 'L5Pyr_soma_gbar_ar': 1e-06,
 'L5Pyr_dend_gkbar_hh2': 0.01,
 'L5Pyr_dend_gnabar_hh2': 0.14,
 'L5Pyr_dend_el_hh2': -71.0,
 'L5Pyr_dend_gl_hh2': 4.26e-05,
 'L5Pyr_dend_gbar_ca': 60.0,
 'L5Pyr_dend_taur_cad': 20.0,
 'L5Pyr_dend_gbar_kca': 0.0002,
 'L5Pyr_dend_gbar_km': 200.0,
 'L5Pyr_dend_gbar_cat': 0.0002,
 'L5Pyr_dend_gbar_ar': 1e-06,
 'N_pyr_x': 10,
 'N_pyr_y': 10,
 'gbar_L2Pyr_L2Pyr_ampa': 0.0005,
 'gbar_L2Pyr_L2Pyr_nmda': 0.0005,
 'gbar_L2Basket_L2Pyr_gabaa': 0.05,
 'gbar_L2Basket_L2Pyr_gabab': 0.05,
 'gbar_L2Pyr_L2Basket': 0.0005,
 'gbar_L2Basket_L2Basket': 0.02,
 'gbar_L5Pyr_L5Pyr_ampa': 0.0005,
 'gbar_L5Pyr_L5Pyr_nmda': 0.0005,
 'gbar_L2Pyr_L5Pyr': 0.00025,
 'gbar_L2Basket_L5Pyr': 0.001,
 'gbar_L5Basket_L5Pyr_gabaa': 0.025,
 'gbar_L5Basket_L5Pyr_gabab': 0.025,
 'gbar_L5Basket_L5Basket': 0.02,
 'gbar_L5Pyr_L5Basket': 0.0005,
 'gbar_L2Pyr_L5Basket': 0.00025,
 'L2Basket_Gauss_A_weight': 0.0,
 'L2Basket_Gauss_mu': 2000.0,
 'L2Basket_Gauss_sigma': 3.6,
 'L2Basket_Pois_A_weight_ampa': 0.0,
 'L2Basket_Pois_A_weight_nmda': 0.0,
 'L2Basket_Pois_lamtha': 0.0,
 'L2Pyr_Gauss_A_weight': 0.0,
 'L2Pyr_Gauss_mu': 2000.0,
 'L2Pyr_Gauss_sigma': 3.6,
 'L2Pyr_Pois_A_weight_ampa': 0.0,
 'L2Pyr_Pois_A_weight_nmda': 0.0,
 'L2Pyr_Pois_lamtha': 0.0,
 'L5Pyr_Gauss_A_weight': 0.0,
 'L5Pyr_Gauss_mu': 2000.0,
 'L5Pyr_Gauss_sigma': 4.8,
 'L5Pyr_Pois_A_weight_ampa': 0.0,
 'L5Pyr_Pois_A_weight_nmda': 0.0,
 'L5Pyr_Pois_lamtha': 0.0,
 'L5Basket_Gauss_A_weight': 0.0,
 'L5Basket_Gauss_mu': 2000.0,
 'L5Basket_Gauss_sigma': 2.0,
 'L5Basket_Pois_A_weight_ampa': 0.0,
 'L5Basket_Pois_A_weight_nmda': 0.0,
 'L5Basket_Pois_lamtha': 0.0,
 't0_pois': 0.0,
 'T_pois': -1,
 'distribution_prox': 'normal',
 't0_input_prox': 1000.0,
 'tstop_input_prox': 1001,
 'f_input_prox': 10.0,
 'f_stdev_prox': 20.0,
 'events_per_cycle_prox': 2,
 'repeats_prox': 10,
 't0_input_stdev_prox': 0.0,
 'distribution_dist': 'normal',
 't0_input_dist': 1000,
 'tstop_input_dist': 1001,
 'f_input_dist': 10.0,
 'f_stdev_dist': 20.0,
 'events_per_cycle_dist': 2,
 'repeats_dist': 10,
 't0_input_stdev_dist': 0.0,
 'input_prox_A_weight_L2Pyr_ampa': 0.0,
 'input_prox_A_weight_L2Pyr_nmda': 0.0,
 'input_prox_A_weight_L5Pyr_ampa': 0.0,
 'input_prox_A_weight_L5Pyr_nmda': 0.0,
 'input_prox_A_weight_L2Basket_ampa': 0.0,
 'input_prox_A_weight_L2Basket_nmda': 0.0,
 'input_prox_A_weight_L5Basket_ampa': 0.0,
 'input_prox_A_weight_L5Basket_nmda': 0.0,
 'input_prox_A_delay_L2': 0.1,
 'input_prox_A_delay_L5': 1.0,
 'input_dist_A_weight_L2Pyr_ampa': 0.0,
 'input_dist_A_weight_L2Pyr_nmda': 0.0,
 'input_dist_A_weight_L5Pyr_ampa': 0.0,
 'input_dist_A_weight_L5Pyr_nmda': 0.0,
 'input_dist_A_weight_L2Basket_ampa': 0.0,
 'input_dist_A_weight_L2Basket_nmda': 0.0,
 'input_dist_A_delay_L2': 5.0,
 'input_dist_A_delay_L5': 5.0,
 'dt_evprox0_evdist': (-1,),
 'dt_evprox0_evprox1': (-1,),
 'sync_evinput': 0,
 'inc_evinput': 0.0,
 'Itonic_A_L2Pyr_soma': 0.0,
 'Itonic_t0_L2Pyr_soma': 0.0,
 'Itonic_T_L2Pyr_soma': -1.0,
 'Itonic_A_L2Basket': 0.0,
 'Itonic_t0_L2Basket': 0.0,
 'Itonic_T_L2Basket': -1.0,
 'Itonic_A_L5Pyr_soma': 0.0,
 'Itonic_t0_L5Pyr_soma': 0.0,
 'Itonic_T_L5Pyr_soma': -1.0,
 'Itonic_A_L5Basket': 0.0,
 'Itonic_t0_L5Basket': 0.0,
 'Itonic_T_L5Basket': -1.0,
 'save_spec_data': 0,
 'f_max_spec': 100,
 'dipole_scalefctr': 3000,
 'dipole_smooth_win': 30,
 'save_figs': 0,
 'save_vsoma': 0,
 'N_trials': 100,
 'prng_state': None,
 'prng_seedcore_input_prox': 4,
 'prng_seedcore_input_dist': 4,
 'prng_seedcore_extpois': 4,
 'prng_seedcore_extgauss': 4,
 'expmt_groups': '{ERPYes100Trials}',
 'prng_seedcore_evprox_1': 4,
 'prng_seedcore_evdist_1': 4,
 'prng_seedcore_evprox_2': 4,
 'prng_seedcore_evdist_2': 0,
 't_evprox_1': 26.61,
 'sigma_t_evprox_1': 2.47,
 'numspikes_evprox_1': 1,
 'gbar_evprox_1_L2Pyr_ampa': 0.01525,
 'gbar_evprox_1_L2Pyr_nmda': 0.0,
 'gbar_evprox_1_L2Basket_ampa': 0.08831,
 'gbar_evprox_1_L2Basket_nmda': 0.0,
 'gbar_evprox_1_L5Pyr_ampa': 0.00865,
 'gbar_evprox_1_L5Pyr_nmda': 0.0,
 'gbar_evprox_1_L5Basket_ampa': 0.19934,
 'gbar_evprox_1_L5Basket_nmda': 0.0,
 't_evdist_1': 63.53,
 'sigma_t_evdist_1': 3.85,
 'numspikes_evdist_1': 1,
 'gbar_evdist_1_L2Pyr_ampa': 7e-06,
 'gbar_evdist_1_L2Pyr_nmda': 0.004317,
 'gbar_evdist_1_L2Basket_ampa': 0.006562,
 'gbar_evdist_1_L2Basket_nmda': 0.019482,
 'gbar_evdist_1_L5Pyr_ampa': 0.1423,
 'gbar_evdist_1_L5Pyr_nmda': 0.080074,
 't_evprox_2': 137.12,
 'sigma_t_evprox_2': 8.33,
 'numspikes_evprox_2': 1,
 'gbar_evprox_2_L2Pyr_ampa': 1.43884,
 'gbar_evprox_2_L2Pyr_nmda': 0.0,
 'gbar_evprox_2_L2Basket_ampa': 3e-06,
 'gbar_evprox_2_L2Basket_nmda': 0.0,
 'gbar_evprox_2_L5Pyr_ampa': 0.684013,
 'gbar_evprox_2_L5Pyr_nmda': 0.0,
 'gbar_evprox_2_L5Basket_ampa': 0.008958,
 'gbar_evprox_2_L5Basket_nmda': 0.0})
