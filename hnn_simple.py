
"""
netParams.py 

High-level specifications for HNN network model using NetPyNE

Contributors: salvadordura@gmail.com
"""

from netpyne import specs


import numpy as np
import itertools as it


"""
cfg.py 

Simulationg configuration for NetPyNE-based HNN network model

Contributors: salvadordura@gmail.com
"""

from netpyne import specs

cfg = specs.SimConfig()  
simConfig = cfg

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







# ----------------------------------------------------------------------------
# Cell parameters
# ----------------------------------------------------------------------------

# dictionary to store cellParams (cell property rules)
cellParams = specs.CellParams()

# ------------------------------------------------------------------------------------
# L2 Pyr cell rule
# ------------------------------------------------------------------------------------
cellParams['L2Pyr'] = {
        'secLists': {
            'apical': ['apical_trunk', 'apical_1', 'apical_tuft', 'apical_oblique'],
            'basal': ['basal_1', 'basal_2', 'basal_3']},
        'secs': {
            'soma': {
                'geom': {'L': cfg.L2Pyr_soma_L, 
                        'Ra': cfg.L2Pyr_soma_Ra, 
                        'cm': cfg.L2Pyr_soma_cm, 
                        'diam': cfg.L2Pyr_soma_diam, 
                        'nseg': 1,
                    'pt3d': [[0.0, 0.0, 0.0, cfg.L2Pyr_soma_diam],
                        [0.0, 0.0+cfg.L2Pyr_soma_L, 0.0, cfg.L2Pyr_soma_diam]]},
                'ions': {
                    'k': {'e': -77.0, 'i': 54.4, 'o': 2.5},
                    'na': {'e': 50.0, 'i': 10.0, 'o': 140.0}
                },
                'mechs': {
                    'dipole': {},
                    'hh2': {'el': cfg.L2Pyr_soma_el_hh2, 
                            'gkbar': cfg.L2Pyr_soma_gkbar_hh2, 
                            'gl': cfg.L2Pyr_soma_gl_hh2, 
                            'gnabar': cfg.L2Pyr_soma_gnabar_hh2},
                    'km': {'gbar': cfg.L2Pyr_soma_gbar_km}},
                'topol': {}
            },
            'apical_1': {
                'geom': {'L': cfg.L2Pyr_apical1_L, 
                        'Ra': cfg.L2Pyr_dend_Ra, 
                        'cm': cfg.L2Pyr_dend_cm, 
                        'diam': cfg.L2Pyr_apical1_diam, 
                        'nseg': 7,
                    'pt3d': [
                        [0.0, 48.0, 0.0, cfg.L2Pyr_apical1_diam],
                        [0.0, 48.0+cfg.L2Pyr_apical1_L, 0.0, cfg.L2Pyr_apical1_diam]]},
                'topol': {'childX': 0.0, 'parentSec': 'apical_trunk', 'parentX': 1.0}
            },
            'apical_oblique': {
                'geom': {'L': cfg.L2Pyr_apicaloblique_L, 
                        'Ra': cfg.L2Pyr_dend_Ra, 
                        'cm': cfg.L2Pyr_dend_cm, 
                        'diam': cfg.L2Pyr_apicaloblique_diam, 
                        'nseg': 7,
                    'pt3d': [[0.0, 48.0, 0.0, cfg.L2Pyr_apicaloblique_diam],
                        [0.0-cfg.L2Pyr_apicaloblique_L, 48.0, 0.0, cfg.L2Pyr_apicaloblique_diam]]},
                'topol': {'childX': 0.0, 'parentSec': 'apical_trunk', 'parentX': 1.0}
            },
            'apical_trunk': {
                'geom': {'L': cfg.L2Pyr_apicaltrunk_L, 
                        'Ra': cfg.L2Pyr_dend_Ra, 
                        'cm': cfg.L2Pyr_dend_cm, 
                        'diam': cfg.L2Pyr_apicaltrunk_diam, 
                        'nseg': 1,
                    'pt3d': [
                        [0.0, 13.0, 0.0, cfg.L2Pyr_apicaltrunk_diam],
                        [0.0, 13.0+cfg.L2Pyr_apicaltrunk_L, 0.0, cfg.L2Pyr_apicaltrunk_diam]]},
                'topol': {'childX': 0.0, 'parentSec': 'soma', 'parentX': 1.0}
            },
            'apical_tuft': {
                'geom': {'L': cfg.L2Pyr_apicaltuft_L, 
                        'Ra': cfg.L2Pyr_dend_Ra, 
                        'cm': cfg.L2Pyr_dend_cm, 
                        'diam': cfg.L2Pyr_apicaltuft_diam, 
                        'nseg': 5,
                    'pt3d': [[0.0, 228.0, 0.0, cfg.L2Pyr_apicaltuft_diam],
                        [0.0, 228.0+cfg.L2Pyr_apicaltuft_L, 0.0, cfg.L2Pyr_apicaltuft_diam]]},
                'topol': {'childX': 0.0, 'parentSec': 'apical_1', 'parentX': 1.0}
            },
            'basal_1': {
                'geom': {'L': cfg.L2Pyr_basal1_L, 
                        'Ra': cfg.L2Pyr_dend_Ra, 
                        'cm': cfg.L2Pyr_dend_cm, 
                        'diam': cfg.L2Pyr_basal1_diam, 
                        'nseg': 1,
                    'pt3d': [[0.0, 0.0, 0.0, cfg.L2Pyr_basal1_diam],
                        [0.0, 0.0-cfg.L2Pyr_basal1_L, 0.0, cfg.L2Pyr_basal1_diam]]},
                'topol': {'childX': 0.0, 'parentSec': 'soma', 'parentX': 0.0}
            },
            'basal_2': {
                'geom': {
                    'L': cfg.L2Pyr_basal2_L, 
                            'Ra': cfg.L2Pyr_dend_Ra, 
                            'cm': cfg.L2Pyr_dend_cm, 
                            'diam': cfg.L2Pyr_basal2_diam, 
                            'nseg': 5,
                    'pt3d': [[0.0, -50.0, 0.0, cfg.L2Pyr_basal2_diam],
                        [0.0-cfg.L2Pyr_basal2_L/np.sqrt(2), -50.0-cfg.L2Pyr_basal2_L/np.sqrt(2), 0.0, cfg.L2Pyr_basal2_diam]]},
                'topol': {'childX': 0.0, 'parentSec': 'basal_1', 'parentX': 1.0}
            },
            'basal_3': {
                'geom': {'L': cfg.L2Pyr_basal3_L, 
                        'Ra': cfg.L2Pyr_dend_Ra, 
                        'cm': cfg.L2Pyr_dend_cm, 
                        'diam': cfg.L2Pyr_basal3_diam, 
                        'nseg': 5,
                    'pt3d': [[0.0, -50.0, 0.0, cfg.L2Pyr_basal3_diam],
                        [float(0.0+cfg.L2Pyr_basal3_L/np.sqrt(2)), float(-50.0-cfg.L2Pyr_basal3_L/np.sqrt(2)), 0.0, cfg.L2Pyr_basal3_diam]]},
                'topol': {'childX': 0.0, 'parentSec': 'basal_1', 'parentX': 1.0}
        }}}

## add biophysics (ions and mechs) to L2Pyr dendrites
somaL = cellParams['L2Pyr']['secs']['soma']['geom']['L']

for sec in [sec for secName, sec in cellParams['L2Pyr']['secs'].items() if secName != 'soma']:
    sec['ions'] = {
        'k': {'e': -77.0, 'i': 54.4, 'o': 2.5},
        'na': {'e': 50.0, 'i': 10.0, 'o': 140.0}}
    
    sec['mechs'] = {
        'dipole': {},
        'hh2': {'el': cfg.L2Pyr_dend_el_hh2, 
                'gkbar': cfg.L2Pyr_dend_gkbar_hh2, 
                'gl': cfg.L2Pyr_dend_gl_hh2, 
                'gnabar': cfg.L2Pyr_dend_gnabar_hh2},
        'km': {'gbar': cfg.L2Pyr_dend_gbar_km}}

## set vinit
for sec in cellParams['L2Pyr']['secs'].values():
    sec['vinit'] = -71.46


# ------------------------------------------------------------------------------------
# L2 Basket cell rule
# ------------------------------------------------------------------------------------
cellParams['L2Basket'] = {
        'secs': {
            'soma': {
                'geom': {'L': 39.0, 
                        'Ra': 200.0, 
                        'cm': 0.85, 
                        'diam': 20.0, 
                        'nseg': 1},
                'ions': {
                    'k': {'e': -77.0, 'i': 54.4, 'o': 2.5},
                    'na': {'e': 50.0, 'i': 10.0,'o': 140.0}},
                'mechs': {
                    'hh2': {'el': -54.3, 
                            'gkbar': 0.036, 
                            'gl': 0.0003, 
                            'gnabar': 0.12}},
                'topol': {}
        }}}

## set vinit
for secName,sec in cellParams['L2Basket']['secs'].items():
    sec['vinit'] = -64.9737

# ------------------------------------------------------------------------------------
# L5 Pyramidal cell rule
# ------------------------------------------------------------------------------------

cellParams['L5Pyr'] = {
        'secLists': {
            'apical': ['apical_trunk', 'apical_1', 'apical_2', 'apical_tuft', 'apical_oblique'],
            'basal': ['basal_1', 'basal_2', 'basal_3']},
        'secs': {
            'soma': {
                'geom': {'L': cfg.L5Pyr_soma_L, 
                        'Ra': cfg.L5Pyr_soma_Ra, 
                        'cm': cfg.L5Pyr_soma_cm, 
                        'diam': cfg.L5Pyr_soma_diam, 
                        'nseg': 1,
                    'pt3d': [[0.0, 0.0, 0.0, cfg.L5Pyr_soma_diam],
                        [0.0, 0.0+cfg.L5Pyr_soma_L, 0.0, cfg.L5Pyr_soma_diam]]},
                'ions': {
                    'ca': {'e': 132.4579341637009, 'i': 5e-05, 'o': 2.0},
                    'k': {'e': -77.0, 'i': 54.4, 'o': 2.5},
                    'na': {'e': 50.0, 'i': 10.0, 'o': 140.0}},
                'mechs': {
                    'ar_hnn': {'gbar': cfg.L5Pyr_soma_gbar_ar}, 
                    'ca_hnn': {'gbar': cfg.L5Pyr_soma_gbar_ca},
                    'cad': {'taur': cfg.L5Pyr_soma_taur_cad},
                    'cat_hnn': {'gbar': cfg.L5Pyr_soma_gbar_cat},
                    'dipole': {},
                    'hh2': {'el': cfg.L5Pyr_soma_el_hh2, 
                            'gkbar': cfg.L5Pyr_soma_gkbar_hh2, 
                            'gl': cfg.L5Pyr_soma_gl_hh2, 
                            'gnabar': cfg.L5Pyr_soma_gnabar_hh2},
                    'kca': {'gbar': cfg.L5Pyr_soma_gbar_kca},
                    'km': {'gbar': cfg.L5Pyr_soma_gbar_km}},
                'topol': {}
            },
            'apical_1': {
                'geom': {'L': cfg.L5Pyr_apical1_L, 
                        'Ra': cfg.L5Pyr_dend_Ra, 
                        'cm': cfg.L5Pyr_dend_cm, 
                        'diam': cfg.L5Pyr_apical1_diam, 
                        'nseg': 13,
                    'pt3d': [[0.0, 83.0, 0.0, cfg.L5Pyr_apical1_diam],
                        [0.0, 83.0+cfg.L5Pyr_apical1_L, 0.0, cfg.L5Pyr_apical1_diam]]},
                'topol': {'childX': 0.0, 'parentSec': 'apical_trunk','parentX': 1.0}
            },
            'apical_2': {
                'geom': {'L': cfg.L5Pyr_apical2_L, 
                        'Ra': cfg.L5Pyr_dend_Ra, 
                        'cm': cfg.L5Pyr_dend_cm, 
                        'diam': cfg.L5Pyr_apical2_diam, 
                        'nseg': 13,
                    'pt3d': [[0.0, 483.0, 0.0, cfg.L5Pyr_apical2_diam],
                        [0.0, 483.0+cfg.L5Pyr_apical2_L, 0.0, cfg.L5Pyr_apical2_diam]]},
                'topol': {'childX': 0.0, 'parentSec': 'apical_1', 'parentX': 1.0}
            },
            'apical_oblique': {
                'geom': {'L': cfg.L5Pyr_apicaloblique_L, 
                        'Ra': cfg.L5Pyr_dend_Ra, 
                        'cm': cfg.L5Pyr_dend_cm, 
                        'diam': cfg.L5Pyr_apicaloblique_diam, 
                        'nseg': 5,
                    'pt3d': [[0.0, 83.0, 0.0, cfg.L5Pyr_apicaloblique_diam],
                        [0.0-cfg.L5Pyr_apicaloblique_L, 83.0, 0.0, cfg.L5Pyr_apicaloblique_diam]]},
                'topol': {'childX': 0.0, 'parentSec': 'apical_trunk', 'parentX': 1.0}
            },
            'apical_trunk': {
                'geom': {'L': cfg.L5Pyr_apicaltrunk_L, 
                        'Ra': cfg.L5Pyr_dend_Ra, 
                        'cm': cfg.L5Pyr_dend_cm, 
                        'diam': cfg.L5Pyr_apicaltrunk_diam, 
                        'nseg': 3,
                    'pt3d': [[0.0, 23.0, 0.0, cfg.L5Pyr_apicaltrunk_diam ],
                        [0.0, 23.0+cfg.L5Pyr_apicaltrunk_L, 0.0, cfg.L5Pyr_apicaltrunk_diam]]},
                'topol': {'childX': 0.0, 'parentSec': 'soma', 'parentX': 1.0}
            },
            'apical_tuft': {
                'geom': {'L': cfg.L5Pyr_apicaltuft_L, 
                        'Ra': cfg.L5Pyr_dend_Ra, 
                        'cm': cfg.L5Pyr_dend_cm, 
                        'diam': cfg.L5Pyr_apicaltuft_diam, 
                        'nseg': 9,
                    'pt3d': [[0.0, 883.0, 0.0, cfg.L5Pyr_apicaltuft_diam],
                        [0.0, 883.0+cfg.L5Pyr_apicaltuft_L, 0.0, cfg.L5Pyr_apicaltuft_diam]]},
                'topol': {'childX': 0.0, 'parentSec': 'apical_2', 'parentX': 1.0}
            },
            'basal_1': {
                'geom': {'L': cfg.L5Pyr_basal1_L, 
                        'Ra': cfg.L5Pyr_dend_Ra, 
                        'cm': cfg.L5Pyr_dend_cm, 
                        'diam': cfg.L5Pyr_basal1_diam, 
                        'nseg': 1,
                    'pt3d': [[0.0, 0.0, 0.0, cfg.L5Pyr_basal1_diam],
                        [0.0, 0.0-cfg.L5Pyr_basal1_L, 0.0, cfg.L5Pyr_basal1_diam]]},
                'topol': {'childX': 0.0, 'parentSec': 'soma', 'parentX': 0.0}
            },
            'basal_2': {
                'geom': {'L': cfg.L5Pyr_basal2_L, 
                        'Ra': cfg.L5Pyr_dend_Ra, 
                        'cm': cfg.L5Pyr_dend_cm, 
                        'diam': cfg.L5Pyr_basal2_diam, 
                        'nseg': 5,
                    'pt3d': [[0.0, -50.0, 0.0, cfg.L5Pyr_basal2_diam],
                        [float(0.0-cfg.L5Pyr_basal2_L/np.sqrt(2)), float(-50-cfg.L5Pyr_basal2_L/np.sqrt(2)), 0.0, cfg.L5Pyr_basal2_diam]]},
                'topol': {'childX': 0.0, 'parentSec': 'basal_1', 'parentX': 1.0}
            },
            'basal_3': {
                'geom': {'L': cfg.L5Pyr_basal3_L, 
                        'Ra': cfg.L5Pyr_dend_Ra, 
                        'cm': cfg.L5Pyr_dend_cm, 
                        'diam': cfg.L5Pyr_basal3_diam, 
                        'nseg': 5,
                    'pt3d': [[0.0, -50.0, 0.0, cfg.L5Pyr_basal3_diam],
                        [float(0.0+cfg.L5Pyr_basal2_L/np.sqrt(2)), float(-50-cfg.L5Pyr_basal2_L/np.sqrt(2)), 0.0, cfg.L5Pyr_basal3_diam]]},
                'topol': {
                    'childX': 0.0,
                    'parentSec': 'basal_1',
                    'parentX': 1.0}
        }}}

## add biophysics (ions and mechs) to L5Pyr dendrites

gbar_ar = {  # values calculated for each segment as: seg.gbar_ar = 1e-6 * np.exp(3e-3 * h.distance(seg.x)) (from orig HNN)
    'apical_trunk': [1.1829366e-06, 1.3099645e-06, 1.450633e-06],
    'apical_1': [1.6511327e-06, 1.9316694e-06, 2.2598709e-06, 2.6438357e-06, 3.0930382e-06, 3.6185628e-06, 4.2333769e-06, 4.9526514e-06, 5.7941347e-06, 6.7785908e-06, 7.9303114e-06, 9.2777159e-06, 1.0854052e-05],
    'apical_2': [1.2698216e-05, 1.4855715e-05, 1.7379784e-05, 2.0332707e-05, 2.3787348e-05, 2.7828952e-05, 3.2557247e-05, 3.8088907e-05, 4.4560426e-05, 5.2131493e-05, 6.0988926e-05, 7.1351287e-05, 8.3474272e-05],
    'apical_tuft': [9.6914906e-05, 0.00011166463, 0.00012865915, 0.00014824011, 0.00017080115, 0.0001967958, 0.00022674665, 0.0002612558, 0.00030101698], 'apical_oblique': [1.6478971e-06, 1.9203357e-06, 2.2378151e-06, 2.6077819e-06, 3.0389133e-06],
    'basal_1': [1.1359849e-06],
    'basal_2': [1.3930561e-06, 1.6233631e-06, 1.8917456e-06, 2.2044984e-06, 2.5689571e-06],
    'basal_3': [1.3930561e-06, 1.6233631e-06, 1.8917456e-06, 2.2044984e-06, 2.5689571e-06]}


somaL = cellParams['L5Pyr']['secs']['soma']['geom']['L']

for secName, sec in [(secName, sec) for secName, sec in cellParams['L5Pyr']['secs'].items() if secName != 'soma']:
    sec['ions'] = {
        'ca': {'e': 132.4579341637009, 'i': 5e-05, 'o': 2.0},
        'k': {'e': -77.0, 'i': 54.4, 'o': 2.5},
        'na': {'e': 50.0, 'i': 10.0, 'o': 140.0}}

    L = sec['geom']['L']
    nseg = sec['geom']['nseg']
    
    sec['mechs'] = {
        # gbar_ar value depends of distance from soma 
        'ar_hnn': {'gbar': gbar_ar[secName]}, #[1e-6*np.exp(3e-3 * ((L/nseg)*i+(L/nseg)/2)) for i in range(nseg)]}, 
        'ca_hnn': {'gbar': cfg.L5Pyr_dend_gbar_ca},
        'cad': {'taur': cfg.L5Pyr_dend_taur_cad},
        'cat_hnn': {'gbar': cfg.L5Pyr_dend_gbar_cat},
        'dipole': {},
        'hh2': {'el': cfg.L5Pyr_dend_el_hh2, 
                'gkbar': cfg.L5Pyr_dend_gkbar_hh2, 
                'gl': cfg.L5Pyr_dend_gl_hh2, 
                'gnabar': cfg.L5Pyr_dend_gnabar_hh2},
        'kca': {'gbar': cfg.L5Pyr_dend_gbar_kca},
        'km': {'gbar': cfg.L5Pyr_dend_gbar_km}}

## set vinit
for secName,sec in cellParams['L5Pyr']['secs'].items():
    if secName == 'apical_1':
        sec['vinit'] = -71.32
    elif secName == 'apical_2':
        sec['vinit'] = -69.08
    elif secName == 'apical_tuft':
        sec['vinit'] = -67.30
    else:
        sec['vinit'] = -72.


# ------------------------------------------------------------------------------------
# L5 Basket cell rule
# ------------------------------------------------------------------------------------
cellParams['L5Basket'] = {
        'secs': {
            'soma': {
                'geom': {'L': 39.0, 
                        'Ra': 200.0, 
                        'cm': 0.85, 
                        'diam': 20.0, 
                        'nseg': 1},
                'ions': {
                    'k': {'e': -77.0, 'i': 54.4, 'o': 2.5},
                    'na': {'e': 50.0, 'i': 10.0,'o': 140.0}},
                'mechs': {
                    'hh2': {'el': -54.3, 
                            'gkbar': 0.036, 
                            'gl': 0.0003, 
                            'gnabar': 0.12}},
                'topol': {}
        }}}

## set vinit
for secName,sec in cellParams['L5Basket']['secs'].items():
    sec['vinit'] = -64.9737






# ----------------------------------------------------------------------------
#
# NETWORK PARAMETERS
#
# ----------------------------------------------------------------------------

netParams = specs.NetParams()  # object of class NetParams to store the network parameters

#------------------------------------------------------------------------------
# General network parameters
#------------------------------------------------------------------------------
netParams.sizeX = ((cfg.N_pyr_x * cfg.gridSpacingPyr) - 1) * cfg.xzScaling  # x-dimension (horizontal length) size in um
netParams.sizeY = cfg.sizeY # y-dimension (vertical height or cortical depth) size in um
netParams.sizeZ = ((cfg.N_pyr_y * cfg.gridSpacingPyr) - 1) * cfg.xzScaling # z-dimension (horizontal depth) size in um
netParams.shape = 'cuboid'

netParams.cellsVisualizationSpacingMultiplierX = 50 
netParams.cellsVisualizationSpacingMultiplierY = 1
netParams.cellsVisualizationSpacingMultiplierZ = 50 


# ----------------------------------------------------------------------------
# Cell parameters
# ----------------------------------------------------------------------------
netParams.cellParams = cellParams

# ----------------------------------------------------------------------------
# Population parameters
# ----------------------------------------------------------------------------

# layer locations
layersE = {'L2': [0.0*cfg.sizeY, 0.0*cfg.sizeY], 'L5': [0.654*cfg.sizeY, 0.654*cfg.sizeY]} # 0.654 = 1308/2000
layersI = {'L2': [0.0*cfg.sizeY-00.0, 0.0*cfg.sizeY-00.0], 'L5': [0.654*cfg.sizeY-00.0, 0.654*cfg.sizeY-00.0]}

# Create list of locations for Basket cells based on original ad hoc rules 
# define relevant x spacings for basket cells
xzero = np.arange(0, cfg.N_pyr_x, 3)
xone = np.arange(1, cfg.N_pyr_x, 3)
yeven = np.arange(0, cfg.N_pyr_y, 2)
yodd = np.arange(1, cfg.N_pyr_y, 2)
coords = [pos for pos in it.product(xzero, yeven)] + [pos for pos in it.product(xone, yodd)]
coords_sorted = sorted(coords, key=lambda pos: pos[1])
L2BasketLocs = [{'x': int(coord[0]*cfg.xzScaling), 'y': int(layersI['L2'][0]), 'z': int(coord[1]*cfg.xzScaling)} for coord in coords_sorted]
L5BasketLocs = [{'x': int(coord[0]*cfg.xzScaling), 'y': int(layersI['L5'][0]), 'z': int(coord[1]*cfg.xzScaling)} for coord in coords_sorted]

# create popParams
netParams.popParams['L2Basket'] = {'cellType':  'L2Basket', 'cellModel': 'HH_simple', 'numCells': len(L2BasketLocs), 'cellsList': L2BasketLocs} 
netParams.popParams['L2Pyr'] =    {'cellType':  'L2Pyr',    'cellModel': 'HH_reduced', 'yRange': layersE['L2'],  'gridSpacing': cfg.gridSpacingPyr*cfg.xzScaling} 
netParams.popParams['L5Basket'] = {'cellType':  'L5Basket', 'cellModel': 'HH_simple',  'numCells': len(L5BasketLocs), 'cellsList': L5BasketLocs} 
netParams.popParams['L5Pyr'] =    {'cellType':  'L5Pyr',    'cellModel': 'HH_reduced', 'yRange': layersE['L5'],  'gridSpacing': cfg.gridSpacingPyr*cfg.xzScaling} 

# create variables useful for connectivity
pops = list(netParams.popParams.keys())
cellsPerPop = {}
cellsPerPop['L2Pyr'] = cellsPerPop['L5Pyr'] = int(cfg.N_pyr_x * cfg.N_pyr_x)
cellsPerPop['L2Basket'] = cellsPerPop['L5Basket'] = int(np.ceil(cfg.N_pyr_x * cfg.N_pyr_x / cfg.gridSpacingBasket[2]) + 1)


#------------------------------------------------------------------------------
# Synaptic mechanism parameters
#------------------------------------------------------------------------------

netParams.synMechParams['L2Pyr_AMPA'] = {'mod':'Exp2Syn', 'tau1': cfg.L2Pyr_ampa_tau1, 'tau2': cfg.L2Pyr_ampa_tau2, 'e': cfg.L2Pyr_ampa_e}
netParams.synMechParams['L2Pyr_NMDA'] = {'mod': 'Exp2Syn', 'tau1': cfg.L2Pyr_nmda_tau1, 'tau2': cfg.L2Pyr_nmda_tau2, 'e': cfg.L2Pyr_nmda_e}
netParams.synMechParams['L2Pyr_GABAA'] = {'mod':'Exp2Syn', 'tau1': cfg.L2Pyr_gabaa_tau1, 'tau2': cfg.L2Pyr_gabaa_tau2, 'e': cfg.L2Pyr_gabaa_e}
netParams.synMechParams['L2Pyr_GABAB'] = {'mod':'Exp2Syn', 'tau1': cfg.L2Pyr_gabab_tau1, 'tau2': cfg.L2Pyr_gabab_tau2, 'e': cfg.L2Pyr_gabab_e}

netParams.synMechParams['L5Pyr_AMPA'] = {'mod':'Exp2Syn', 'tau1': cfg.L5Pyr_ampa_tau1, 'tau2': cfg.L5Pyr_ampa_tau2, 'e': cfg.L5Pyr_ampa_e}
netParams.synMechParams['L5Pyr_NMDA'] = {'mod': 'Exp2Syn', 'tau1': cfg.L5Pyr_nmda_tau1, 'tau2': cfg.L5Pyr_nmda_tau2, 'e': cfg.L5Pyr_nmda_e}
netParams.synMechParams['L5Pyr_GABAA'] = {'mod':'Exp2Syn', 'tau1': cfg.L5Pyr_gabaa_tau1, 'tau2': cfg.L5Pyr_gabaa_tau2, 'e': cfg.L5Pyr_gabaa_e}
netParams.synMechParams['L5Pyr_GABAB'] = {'mod':'Exp2Syn', 'tau1': cfg.L5Pyr_gabab_tau1, 'tau2': cfg.L5Pyr_gabab_tau2, 'e': cfg.L5Pyr_gabab_e}

netParams.synMechParams['AMPA'] = {'mod':'Exp2Syn', 'tau1': 0.5, 'tau2': 5.0, 'e': 0}
netParams.synMechParams['NMDA'] = {'mod': 'Exp2Syn', 'tau1': 1, 'tau2': 20, 'e': 0}
netParams.synMechParams['GABAA'] = {'mod':'Exp2Syn', 'tau1': 0.5, 'tau2': 5, 'e': -80}
netParams.synMechParams['GABAB'] = {'mod':'Exp2Syn', 'tau1': 1, 'tau2': 20, 'e': -80}


#------------------------------------------------------------------------------
# Local connectivity parameters 
#------------------------------------------------------------------------------

# Weight and delay distance-dependent functions (as strings) to use in conn rules
weightDistFunc = '{A_weight} * exp(-(dist_2D**2) / ({lamtha}**2))'
delayDistFunc = '{A_delay} / exp(-(dist_2D**2) / ({lamtha}**2))'

if cfg.localConn:

    # L2 Pyr -> L2 Pyr
    synParamsList = [{'synMech': 'L2Pyr_AMPA',
                'A_weight': cfg.EEgain * cfg.gbar_L2Pyr_L2Pyr_ampa,
                'A_delay': 1.,
                'lamtha': 3.},

                {'synMech': 'L2Pyr_NMDA',
                'A_weight': cfg.EEgain * cfg.gbar_L2Pyr_L2Pyr_nmda,
                'A_delay': 1.,
                'lamtha': 3.}]

    for i,synParams in enumerate(synParamsList):
        netParams.connParams['L2Pyr->L2Pyr_%d'%(i)] = { 
            'preConds': {'pop': 'L2Pyr'}, 
            'postConds': {'pop': 'L2Pyr'},
            'synMech': synParams['synMech'],
            'weight': weightDistFunc.format(**synParams), # equivalent to weightDistFunc.format(A_weight=cfg.gbar_L2Pyr_L2Pyr_ampa, lamtha=1.)
            'delay': delayDistFunc.format(**synParams),
            'synsPerConn': 3,
            'sec': ['basal_2', 'basal_3','apical_oblique', ]}
                    

    # L2 Basket -> L2 Pyr
    synParamsList = [{'synMech': 'L2Pyr_GABAA',
                'A_weight': cfg.IEgain * cfg.gbar_L2Basket_L2Pyr_gabaa,
                'A_delay': 1.,
                'lamtha': 50.},

                {'synMech': 'L2Pyr_GABAB',
                'A_weight': cfg.IEgain * cfg.gbar_L2Basket_L2Pyr_gabab,
                'A_delay': 1.,
                'lamtha': 50.}]

    for i,synParams in enumerate(synParamsList):
        netParams.connParams['L2Basket->L2Pyr_%d'%(i)] = { 
            'preConds': {'pop': 'L2Basket'}, 
            'postConds': {'pop': 'L2Pyr'},
            'synMech': synParams['synMech'],
            'weight': weightDistFunc.format(**synParams),
            'delay': delayDistFunc.format(**synParams),
            'synsPerConn': 1,
            'sec': ['soma']}


    # L2 Pyr -> L2 Basket 
    synParams = {'synMech': 'AMPA',
                'A_weight': cfg.EIgain * cfg.gbar_L2Pyr_L2Basket,
                'A_delay': 1.,
                'lamtha': 3.}

    netParams.connParams['L2Pyr->L2Basket_%s'%(synParams['synMech'])] = { 
        'preConds': {'pop': 'L2Pyr'}, 
        'postConds': {'pop': 'L2Basket'},
        'synMech': synParams['synMech'],
        'weight': weightDistFunc.format(**synParams),
        'delay': delayDistFunc.format(**synParams),
        'synsPerConn': 1,
        'sec': ['soma']}


    # L2 Basket -> L2 Basket 
    synParams = {'synMech': 'GABAA',
                'A_weight': cfg.IIgain * cfg.gbar_L2Basket_L2Basket,
                'A_delay': 1.,
                'lamtha': 20.}

    netParams.connParams['L2Basket->L2Basket'] = { 
        'preConds': {'pop': 'L2Basket'}, 
        'postConds': {'pop': 'L2Basket'},
        'synMech': synParams['synMech'],
        'weight': weightDistFunc.format(**synParams),
        'delay': delayDistFunc.format(**synParams),
        'synsPerConn': 1,
        'sec': ['soma']}


    # L5 Pyr -> L5 Pyr
    synParamsList = [{'synMech': 'L5Pyr_AMPA',
                'A_weight': cfg.EEgain * cfg.gbar_L5Pyr_L5Pyr_ampa,
                'A_delay': 1.,
                'lamtha': 3.},

                {'synMech': 'L5Pyr_NMDA',
                'A_weight': cfg.EEgain * cfg.gbar_L5Pyr_L5Pyr_nmda,
                'A_delay': 1.,
                'lamtha': 3.}]

    for i,synParams in enumerate(synParamsList):
        netParams.connParams['L5Pyr->L5Pyr_%d'%(i)] = { 
            'preConds': {'pop': 'L5Pyr'}, 
            'postConds': {'pop': 'L5Pyr'},
            'synMech': synParams['synMech'],
            'weight': weightDistFunc.format(**synParams),
            'delay': delayDistFunc.format(**synParams),
            'synsPerConn': 3,
            'sec': ['basal_2', 'basal_3', 'apical_oblique']}
                

    # L5 Basket -> L5 Pyr
    synParamsList = [{'synMech': 'L5Pyr_GABAA',
                'A_weight': cfg.IEgain * cfg.gbar_L5Basket_L5Pyr_gabaa,
                'A_delay': 1.,
                'lamtha': 70.},

                {'synMech': 'L5Pyr_GABAB',
                'A_weight': cfg.IEgain * cfg.gbar_L5Basket_L5Pyr_gabab,
                'A_delay': 1.,
                'lamtha': 70.}]

    for i,synParams in enumerate(synParamsList):
        netParams.connParams['L5Basket->L5Pyr_%d'%(i)] = { 
            'preConds': {'pop': 'L5Basket'}, 
            'postConds': {'pop': 'L5Pyr'},
            'synMech': synParams['synMech'],
            'weight': weightDistFunc.format(**synParams),
            'delay': delayDistFunc.format(**synParams),
            'synsPerConn': 1,
            'sec': ['soma']}


    # L2 Pyr -> L5 Pyr
    synParams = {'synMech': 'L5Pyr_AMPA',
                'A_weight': cfg.EEgain * cfg.gbar_L2Pyr_L5Pyr,
                'A_delay': 1.,
                'lamtha': 3.}

    netParams.connParams['L2Pyr->L5Pyr'] = { 
        'preConds': {'pop': 'L2Pyr'}, 
        'postConds': {'pop': 'L5Pyr'},
        'synMech': synParams['synMech'],
        'weight': weightDistFunc.format(**synParams),
        'delay': delayDistFunc.format(**synParams),
        'synsPerConn': 4,
        'sec': ['basal_2', 'basal_3', 'apical_tuft', 'apical_oblique']}
                

    # L2 Basket -> L5 Pyr
    synParams = {'synMech': 'L5Pyr_GABAA',
                'A_weight': cfg.IEgain * cfg.gbar_L2Basket_L5Pyr,
                'A_delay': 1.,
                'lamtha': 50.}

    netParams.connParams['L2Basket->L5Pyr'] = { 
        'preConds': {'pop': 'L2Basket'}, 
        'postConds': {'pop': 'L5Pyr'},
        'synMech': synParams['synMech'],
        'weight': weightDistFunc.format(**synParams),
        'delay': delayDistFunc.format(**synParams),
        'synsPerConn': 1,
        'sec': ['apical_tuft']}
        

    # L5 Pyr -> L5 Basket 
    synParams = {'synMech': 'AMPA',
                'A_weight': cfg.EIgain * cfg.gbar_L5Pyr_L5Basket,
                'A_delay': 1.,
                'lamtha': 3.}

    netParams.connParams['L5Pyr->L5Basket'] = { 
        'preConds': {'pop': 'L5Pyr'}, 
        'postConds': {'pop': 'L5Basket'},
        'synMech': synParams['synMech'],
        'weight': weightDistFunc.format(**synParams),
        'delay': delayDistFunc.format(**synParams),
        'synsPerConn': 1,
        'sec': ['soma']}


    # L2 Pyr -> L5 Basket 
    synParams = {'synMech': 'AMPA',
                'A_weight': cfg.EIgain * cfg.gbar_L2Pyr_L5Basket,
                'A_delay': 1.,
                'lamtha': 3.}

    netParams.connParams['L2Pyr->L5Basket'] = { 
        'preConds': {'pop': 'L2Pyr'}, 
        'postConds': {'pop': 'L5Basket'},
        'synMech': synParams['synMech'],
        'weight': weightDistFunc.format(**synParams),
        'delay': delayDistFunc.format(**synParams),
        'synsPerConn': 1,
        'sec': ['soma']}


    # L5 Basket -> L5 Basket 
    synParams = {'synMech': 'GABAA',
                'A_weight': cfg.IIgain * cfg.gbar_L5Basket_L5Basket,
                'A_delay': 1.,
                'lamtha': 20.}

    netParams.connParams['L5Basket->L5Basket'] = { 
        'preConds': {'pop': 'L5Basket'}, 
        'postConds': {'pop': 'L5Basket'},
        'synMech': synParams['synMech'],
        'weight': weightDistFunc.format(**synParams),
        'delay': delayDistFunc.format(**synParams),
        'synsPerConn': 1,
        'sec': ['soma']}

'''
#------------------------------------------------------------------------------
# Rhythmic proximal and distal inputs parameters 
#------------------------------------------------------------------------------

# Location of external inputs
xrange = np.arange(cfg.N_pyr_x)
extLocX = int(xrange[int((len(xrange) - 1) // 2)])
zrange = np.arange(cfg.N_pyr_y)
extLocZ = int(xrange[int((len(zrange) - 1) // 2)])
extLocY = 650 # positive depth of L5 relative to L2; doesn't affect weight/delay calculations

conn1to1Pyr = np.array([range(0,cellsPerPop['L2Pyr']), range(0,cellsPerPop['L2Pyr'])]).T.tolist()
conn1to1Basket = np.array([range(0,cellsPerPop['L2Basket']), range(0,cellsPerPop['L2Basket'])]).T.tolist()

if cfg.rhythmicInputs:

    # Ad hoc rules copied from original code (need to improve!! -- maybe add to .param files?)

    ## "if stdev is zero, increase synaptic weights 5 fold to make"
    ## "single input equivalent to 5 simultaneous input to prevent spiking <<---- SN: WHAT IS THIS RULE!?!?!?"
    if cfg.f_stdev_prox == 0.0 and cfg.distribution_prox != 'uniform':
        for key in [k for k in cfg.__dict__ if k.startswith('input_prox_A_weight')]:
            cfg.__dict__[key] *= 5.0

    if cfg.f_stdev_dist == 0.0 and cfg.distribution_dist != 'uniform':
        for key in [k for k in cfg.__dict__ if k.startswith('input_dist_A_weight')]:
            cfg.__dict__[key] *= 5.0

    ## "if L5 delay is -1, use same delays as L2 unless L2 delay is 0.1 in which case use 1. <<---- SN: WHAT IS THIS RULE!?!?!?"
    if cfg.input_prox_A_delay_L5 == -1:
        if cfg.input_prox_A_delay_L2 != 0.1:
            cfg.input_prox_A_delay_L5 = cfg.input_prox_A_delay_L2
        else:
            cfg.input_prox_A_delay_L5 = 1.0

    if cfg.input_dist_A_delay_L5 == -1:
        if cfg.input_dist_A_delay_L2 != 0.1:
            cfg.input_dist_A_delay_L5 = cfg.input_dist_A_delay_L2
        else:
            cfg.input_dist_A_delay_L5 = 1.0
            
    # External Rhythmic proximal inputs (1 VecStim per cell for each cell population)
    netParams.popParams['extRhythmicProximal'] = {
        'cellModel': 'VecStim',
        'numCells': 1,
        'xRange': [extLocX, extLocX],
        'yRange': [extLocY, extLocY],
        'zRange': [extLocZ, extLocZ],
        'seed': int(cfg.prng_seedcore_input_prox),
        'spikePattern': {
                'type': 'rhythmic',
                'start': cfg.t0_input_prox,
                'startStd': cfg.t0_input_stdev_prox,
                'stop': cfg.tstop_input_prox,
                'freq': cfg.f_input_prox,
                'freqStd': cfg.f_stdev_prox,
                'eventsPerCycle': cfg.events_per_cycle_prox,
                'distribution': cfg.distribution_prox,
                'repeats': cfg.repeats_prox}}


    # External Rhythmic distal inputs (population of 1 VecStim)
    netParams.popParams['extRhythmicDistal'] = {
        'cellModel': 'VecStim',
        'numCells': 1,
        'xRange': [extLocX, extLocX],
        'yRange': [extLocY, extLocY],
        'zRange': [extLocZ, extLocZ],
        'seed': int(cfg.prng_seedcore_input_dist),
        'spikePattern': {
                'type': 'rhythmic',
                'start': cfg.t0_input_dist,
                'startStd': cfg.t0_input_stdev_dist,
                'stop': cfg.tstop_input_dist,
                'freq': cfg.f_input_dist,
                'freqStd': cfg.f_stdev_dist,
                'eventsPerCycle': cfg.events_per_cycle_dist,
                'distribution': cfg.distribution_dist,
                'repeats': cfg.repeats_dist}}


    # Rhytmic proximal -> L2 Pyr
    synParamsList = [{'synMech': 'L2Pyr_AMPA',
                'A_weight': cfg.input_prox_A_weight_L2Pyr_ampa,
                'A_delay': cfg.input_prox_A_delay_L2,
                'lamtha': 100.},

                {'synMech': 'L2Pyr_NMDA',
                'A_weight': cfg.input_prox_A_weight_L2Pyr_nmda,
                'A_delay': cfg.input_prox_A_delay_L2,
                'lamtha': 100.}]

    for i,synParams in enumerate(synParamsList):
        netParams.connParams['extRhythmicProx->L2Pyr_%d'%(i)] = { 
            'preConds': {'pop': 'extRhythmicProximal'}, 
            'postConds': {'pop': 'L2Pyr'},
            'synMech': synParams['synMech'],
            'weight': weightDistFunc.format(**synParams),
            'delay': delayDistFunc.format(**synParams),
            'synsPerConn': 3,
            'sec': ['basal_2', 'basal_3','apical_oblique']}


    # Rhythmic distal -> L2 Pyr
    synParamsList = [{'synMech': 'L2Pyr_AMPA',
                'A_weight': cfg.input_dist_A_weight_L2Pyr_ampa,
                'A_delay': cfg.input_dist_A_delay_L2,
                'lamtha': 100.},

                {'synMech': 'L2Pyr_NMDA',
                'A_weight': cfg.input_dist_A_weight_L2Pyr_nmda,
                'A_delay': cfg.input_dist_A_delay_L2,
                'lamtha': 100.}]

    for i,synParams in enumerate(synParamsList):
        netParams.connParams['extRhythmicDistal->L2Pyr_%d'%(i)] = { 
            'preConds': {'pop': 'extRhythmicDistal'}, 
            'postConds': {'pop': 'L2Pyr'},
            'synMech': synParams['synMech'],
            'weight': weightDistFunc.format(**synParams),
            'delay': delayDistFunc.format(**synParams),
            'synsPerConn': 1,
            'sec': ['apical_tuft']}


    # Rhythmic proximal -> L5 Pyr
    synParamsList = [{'synMech': 'L5Pyr_AMPA',
                'A_weight': cfg.input_prox_A_weight_L5Pyr_ampa,
                'A_delay': cfg.input_prox_A_delay_L5,
                'lamtha': 100.},

                {'synMech': 'L5Pyr_NMDA',
                'A_weight': cfg.input_prox_A_weight_L5Pyr_nmda,
                'A_delay': cfg.input_prox_A_delay_L5,
                'lamtha': 100.}]

    for i,synParams in enumerate(synParamsList):
        netParams.connParams['extRhythmicProx->L5Pyr_%d'%(i)] = { 
            'preConds': {'pop': 'extRhythmicProximal'}, 
            'postConds': {'pop': 'L5Pyr'},
            'synMech': synParams['synMech'],
            'weight': weightDistFunc.format(**synParams),
            'delay': delayDistFunc.format(**synParams),
            'synsPerConn': 3,
            'sec': ['basal_2', 'basal_3','apical_oblique']}


    # Rhythmic distal -> L5 Pyr
    synParamsList = [{'synMech': 'L5Pyr_AMPA',
                'A_weight': cfg.input_dist_A_weight_L5Pyr_ampa,
                'A_delay': cfg.input_dist_A_delay_L5,
                'lamtha': 100.},

                {'synMech': 'L5Pyr_NMDA',
                'A_weight': cfg.input_dist_A_weight_L5Pyr_nmda,
                'A_delay': cfg.input_dist_A_delay_L5,
                'lamtha': 100.}]

    for i,synParams in enumerate(synParamsList):
        netParams.connParams['extRhythmicDistal->L5Pyr_%d'%(i)] = { 
            'preConds': {'pop': 'extRhythmicDistal'}, 
            'postConds': {'pop': 'L5Pyr'},
            'synMech': synParams['synMech'],
            'weight': weightDistFunc.format(**synParams),
            'delay': delayDistFunc.format(**synParams),
            'synsPerConn': 1,
            'sec': ['apical_tuft']}


    # Rhytmic proximal -> L2 Basket
    synParamsList = [{'synMech': 'AMPA',
                'A_weight': cfg.input_prox_A_weight_L2Basket_ampa,
                'A_delay': cfg.input_prox_A_delay_L2,
                'lamtha': 100.},

                {'synMech': 'NMDA',
                'A_weight': cfg.input_prox_A_weight_L2Basket_nmda,
                'A_delay': cfg.input_prox_A_delay_L2,
                'lamtha': 100.}]

    for i,synParams in enumerate(synParamsList):
        netParams.connParams['extRhythmicProx->L2Basket_%d'%(i)] = { 
            'preConds': {'pop': 'extRhythmicProximal'}, 
            'postConds': {'pop': 'L2Basket'},
            'synMech': synParams['synMech'],
            'weight': weightDistFunc.format(**synParams),
            'delay': delayDistFunc.format(**synParams),
            'synsPerConn': 1,
            'sec': 'soma'}


    # Rhytmic proximal -> L5 Basket
    synParamsList = [{'synMech': 'AMPA',
                'A_weight': cfg.input_prox_A_weight_L5Basket_ampa,
                'A_delay': cfg.input_prox_A_delay_L5,
                'lamtha': 100.},

                {'synMech': 'NMDA',
                'A_weight': cfg.input_prox_A_weight_L5Basket_nmda,
                'A_delay': cfg.input_prox_A_delay_L5,
                'lamtha': 100.}]

    for i,synParams in enumerate(synParamsList):
        netParams.connParams['extRhythmicProx->L5Basket_%d'%(i)] = { 
            'preConds': {'pop': 'extRhythmicProximal'}, 
            'postConds': {'pop': 'L5Basket'},
            'synMech': synParams['synMech'],
            'weight': weightDistFunc.format(**synParams),
            'delay': delayDistFunc.format(**synParams),
            'synsPerConn': 1,
            'sec': 'soma'}


#------------------------------------------------------------------------------
# Evoked proximal and distal inputs parameters 
#------------------------------------------------------------------------------

if cfg.evokedInputs:

    # Evoked proximal inputs (population of 1 VecStim)
    nprox = len([k for k in cfg.__dict__ if k.startswith('t_evprox')])
    ndist = len([k for k in cfg.__dict__ if k.startswith('t_evdist')])

    # Evoked proximal inputs (population of 1 VecStim)
    for iprox in range(nprox):
        for pop in pops:
            skey = 'evprox_%d'%(iprox+1)
            netParams.popParams['evokedProximal_%d_%s'%(iprox+1, pop)] = {
                'cellModel': 'VecStim',
                'numCells': cellsPerPop[pop],
                'xRange': [extLocX, extLocX],
                'yRange': [extLocY, extLocY],
                'zRange': [extLocZ, extLocZ],
                'seed': int(getattr(cfg, 'prng_seedcore_' + skey)),
                'spikePattern': {
                        'type': 'evoked',
                        'start': getattr(cfg, 't_' + skey),
                        'startStd': getattr(cfg, 'sigma_t_' + skey),
                        'numspikes': getattr(cfg, 'numspikes_' + skey),
                        'sync': getattr(cfg, 'sync_evinput')}}


        # Evoked proximal -> L2 Pyr
        synParamsList = [{'synMech': 'L2Pyr_AMPA',
                    'A_weight': getattr(cfg, 'gbar_'+skey+'_L2Pyr_ampa'),
                    'A_delay': 0.1,
                    'lamtha': 3.},

                    {'synMech': 'L2Pyr_NMDA',
                    'A_weight': getattr(cfg, 'gbar_'+skey+'_L2Pyr_nmda'),
                    'A_delay': 0.1,
                    'lamtha': 3.}]

        for i,synParams in enumerate(synParamsList):
            netParams.connParams['evokedProx_%d->L2Pyr_%d'%(iprox+1, i)] = { 
                'preConds': {'pop': 'evokedProximal_%d_L2Pyr'%(iprox+1)}, 
                'postConds': {'pop': 'L2Pyr'},
                'synMech': synParams['synMech'],
                'weight': weightDistFunc.format(**synParams),
                'delay': delayDistFunc.format(**synParams),
                'connList': conn1to1Pyr,
                'synsPerConn': 3,
                'sec': ['basal_2', 'basal_3','apical_oblique']}

        # Evoked proximal -> L5 Pyr
        synParamsList = [{'synMech': 'L5Pyr_AMPA',
                    'A_weight': getattr(cfg, 'gbar_'+skey+'_L5Pyr_ampa'),
                    'A_delay': 1.0,
                    'lamtha': 3.},

                    {'synMech': 'L5Pyr_NMDA',
                    'A_weight': getattr(cfg, 'gbar_'+skey+'_L5Pyr_nmda'),
                    'A_delay': 1.0,
                    'lamtha': 3.}]

        for i,synParams in enumerate(synParamsList):
            netParams.connParams['evokedProx_%d->L5Pyr_%d'%(iprox+1, i)] = { 
                'preConds': {'pop': 'evokedProximal_%d_L5Pyr'%(iprox+1)}, 
                'postConds': {'pop': 'L5Pyr'},
                'synMech': synParams['synMech'],
                'weight': weightDistFunc.format(**synParams),
                'delay': delayDistFunc.format(**synParams),
                'connList': conn1to1Pyr,
                'synsPerConn': 3,
                'sec': ['basal_2', 'basal_3','apical_oblique']}

        # Evoked proximal -> L2 Basket
        synParamsList = [{'synMech': 'AMPA',
                    'A_weight': getattr(cfg, 'gbar_'+skey+'_L2Basket_ampa'),
                    'A_delay': 0.1,
                    'lamtha': 3.},

                    {'synMech': 'NMDA',
                    'A_weight': getattr(cfg, 'gbar_'+skey+'_L2Basket_nmda'),
                    'A_delay': 0.1,
                    'lamtha': 3.}]

        for i,synParams in enumerate(synParamsList):
            netParams.connParams['evokedProx_%d->L2Basket_%d'%(iprox+1, i)] = { 
                'preConds': {'pop': 'evokedProximal_%d_L2Basket'%(iprox+1)}, 
                'postConds': {'pop': 'L2Basket'},
                'synMech': synParams['synMech'],
                'weight': weightDistFunc.format(**synParams),
                'delay': delayDistFunc.format(**synParams),
                'connList': conn1to1Basket,
                'synsPerConn': 1,
                'sec': 'soma'}

        # Evoked proximal -> L5 Basket
        synParamsList = [{'synMech': 'AMPA',
                    'A_weight': getattr(cfg, 'gbar_'+skey+'_L5Basket_ampa'),
                    'A_delay': 1.0,
                    'lamtha': 3.},

                    {'synMech': 'NMDA',
                    'A_weight': getattr(cfg, 'gbar_'+skey+'_L5Basket_nmda'),
                    'A_delay': 1.0,
                    'lamtha': 3.}]

        for i,synParams in enumerate(synParamsList):
            netParams.connParams['evokedProx_%d->L5Basket_%d'%(iprox+1, i)] = { 
                'preConds': {'pop': 'evokedProximal_%d_L5Basket'%(iprox+1)}, 
                'postConds': {'pop': 'L5Basket'},
                'synMech': synParams['synMech'],
                'weight': weightDistFunc.format(**synParams),
                'delay': delayDistFunc.format(**synParams),
                'connList': conn1to1Basket,
                'synsPerConn': 1,
                'sec': 'soma'}


    # Evoked distal inputs (population of 1 VecStim)
    for idist in range(ndist):
        for pop in pops:
            skey = 'evdist_%d'%(idist+1)
            netParams.popParams['evokedDistal_%d_%s'%(idist+1, pop)] = {
            'cellModel': 'VecStim',
            'numCells': cellsPerPop[pop],
            'xRange': [extLocX, extLocX],
            'yRange': [extLocY, extLocY],
            'zRange': [extLocZ, extLocZ],
            'seed': int(getattr(cfg, 'prng_seedcore_' + skey)),
            'spikePattern': {
                    'type': 'evoked',
                    'start': getattr(cfg, 't_' + skey),
                    'startStd': getattr(cfg, 'sigma_t_' + skey),
                    'numspikes': getattr(cfg, 'numspikes_' + skey),
                    'sync': getattr(cfg, 'sync_evinput')}}


        # Evoked Distal -> L2 Pyr
        synParamsList = [{'synMech': 'L2Pyr_AMPA',
                    'A_weight': getattr(cfg, 'gbar_'+skey+'_L2Pyr_ampa'),
                    'A_delay': 0.1,
                    'lamtha': 3.},

                    {'synMech': 'L2Pyr_NMDA',
                    'A_weight': getattr(cfg, 'gbar_'+skey+'_L2Pyr_nmda'),
                    'A_delay': 0.1,
                    'lamtha': 3.}]

        for i,synParams in enumerate(synParamsList):
            netParams.connParams['evokedDistal_%d->L2Pyr_%d'%(idist+1, i)] = { 
                'preConds': {'pop': 'evokedDistal_%d_L2Pyr'%(idist+1)}, 
                'postConds': {'pop': 'L2Pyr'},
                'synMech': synParams['synMech'],
                'weight': weightDistFunc.format(**synParams),
                'delay': delayDistFunc.format(**synParams),
                'connList': conn1to1Pyr,
                'synsPerConn': 1,
                'sec': 'apical_tuft'}

        # Evoked Distal -> L5 Pyr
        synParamsList = [{'synMech': 'L5Pyr_AMPA',
                    'A_weight': getattr(cfg, 'gbar_'+skey+'_L5Pyr_ampa'),
                    'A_delay': 0.1,
                    'lamtha': 3.},

                    {'synMech': 'L5Pyr_NMDA',
                    'A_weight': getattr(cfg, 'gbar_'+skey+'_L5Pyr_nmda'),
                    'A_delay': 0.1,
                    'lamtha': 3.}]

        for i,synParams in enumerate(synParamsList):
            netParams.connParams['evokedDistal_%d->L5Pyr_%d'%(idist+1, i)] = { 
                'preConds': {'pop': 'evokedDistal_%d_L5Pyr'%(idist+1)}, 
                'postConds': {'pop': 'L5Pyr'},
                'synMech': synParams['synMech'],
                'weight': weightDistFunc.format(**synParams),
                'delay': delayDistFunc.format(**synParams),
                'connList': conn1to1Pyr,
                'synsPerConn': 1,
                'sec': 'apical_tuft'}

        # Evoked Distal -> L2 Basket
        synParamsList = [{'synMech': 'AMPA',
                    'A_weight': getattr(cfg, 'gbar_'+skey+'_L2Basket_ampa'),
                    'A_delay': 0.1,
                    'lamtha': 3.},

                    {'synMech': 'NMDA',
                    'A_weight': getattr(cfg, 'gbar_'+skey+'_L2Basket_nmda'),
                    'A_delay': 0.1,
                    'lamtha': 3.}]

        for i,synParams in enumerate(synParamsList):
            netParams.connParams['evokedDistal_%d->L2Basket_%d'%(idist+1, i)] = { 
                'preConds': {'pop': 'evokedDistal_%d_L2Basket'%(idist+1)}, 
                'postConds': {'pop': 'L2Basket'},
                'synMech': synParams['synMech'],
                'weight': weightDistFunc.format(**synParams),
                'delay': delayDistFunc.format(**synParams),
                'connList': conn1to1Basket,
                'synsPerConn': 1,
                'sec': 'soma'}


#------------------------------------------------------------------------------
# Tonic input parameters 
#------------------------------------------------------------------------------

if cfg.tonicInputs:

    # Tonic inputs (IClamp) -> L2Pyr
    if cfg.Itonic_T_L2Pyr_soma == -1:
        t_dur = cfg.duration - cfg.Itonic_t0_L2Pyr_soma
    else:
        t_dur = cfg.Itonic_T_L2Pyr_soma - cfg.Itonic_t0_L2Pyr_soma

    netParams.stimSourceParams['ITonic_L2Pyr'] = {'type': 'IClamp', 'del': cfg.Itonic_t0_L2Pyr_soma, 'dur': t_dur, 'amp': cfg.Itonic_A_L2Pyr_soma}
    netParams.stimTargetParams['ITonic->L2Pyr'] = {'source': 'ITonic_L2Pyr', 'sec':'soma', 'loc': 0.5, 'conds': {'pop': 'L2Pyr'}}


    # Tonic inputs (IClamp) -> L5Pyr
    if cfg.Itonic_T_L5Pyr_soma == -1:
        t_dur = cfg.duration - cfg.Itonic_t0_L5Pyr_soma
    else:
        t_dur = cfg.Itonic_T_L5Pyr_soma - cfg.Itonic_t0_L5Pyr_soma

    netParams.stimSourceParams['ITonic_L5Pyr'] = {'type': 'IClamp', 'del': cfg.Itonic_t0_L5Pyr_soma, 'dur': t_dur, 'amp': cfg.Itonic_A_L5Pyr_soma}
    netParams.stimTargetParams['ITonic->L5Pyr'] = {'source': 'ITonic_L5Pyr', 'sec':'soma', 'loc': 0.5, 'conds': {'pop': 'L5Pyr'}}


    # Tonic inputs (IClamp) -> L2Basket
    if cfg.Itonic_T_L2Basket == -1:
        t_dur = cfg.duration - cfg.Itonic_t0_L2Basket
    else:
        t_dur = cfg.Itonic_T_L2Basket - cfg.Itonic_t0_L2Basket

    netParams.stimSourceParams['ITonic_L2Basket'] = {'type': 'IClamp', 'del': cfg.Itonic_t0_L2Basket, 'dur': t_dur, 'amp': cfg.Itonic_A_L2Basket}
    netParams.stimTargetParams['ITonic->L2Basket'] = {'source': 'ITonic_L2Basket', 'sec':'soma', 'loc': 0.5, 'conds': {'pop': 'L2Basket'}}


    # Tonic inputs (IClamp) -> L5Basket
    if cfg.Itonic_T_L5Basket == -1:
        t_dur = cfg.duration - cfg.Itonic_t0_L5Basket
    else:
        t_dur = cfg.Itonic_T_L5Basket - cfg.Itonic_t0_L5Basket

    netParams.stimSourceParams['ITonic_L5Basket'] = {'type': 'IClamp', 'del': cfg.Itonic_t0_L5Basket, 'dur': t_dur, 'amp': cfg.Itonic_A_L5Basket}
    netParams.stimTargetParams['ITonic->L5Basket'] = {'source': 'ITonic_L5Basket', 'sec':'soma', 'loc': 0.5, 'conds': {'pop': 'L5Basket'}}


#------------------------------------------------------------------------------
# Poisson-distributed input parameters 
#------------------------------------------------------------------------------

if cfg.poissonInputs:

    # Poisson inputs -> L2 Pyr
    netParams.popParams['extPoisson_L2Pyr'] = {
        'cellModel': 'VecStim',
        'numCells': cellsPerPop['L2Pyr'],
        'xRange': [extLocX, extLocX],
        'yRange': [extLocY, extLocY],
        'zRange': [extLocZ, extLocZ],
        'seed': int(getattr(cfg, 'prng_seedcore_extpois')),
        'spikePattern': {
                'type': 'poisson',
                'start': getattr(cfg, 't0_pois'),
                'stop': getattr(cfg, 'T_pois'),
                'frequency': getattr(cfg, 'L2Pyr_Pois_lamtha')}}

    synParamsList = [{'synMech': 'L2Pyr_AMPA',
                'A_weight': getattr(cfg, 'L2Pyr_Pois_A_weight_ampa'),
                'A_delay': 0.1,
                'lamtha': 100.},

                {'synMech': 'L2Pyr_NMDA',
                'A_weight': getattr(cfg, 'L2Pyr_Pois_A_weight_nmda'),
                'A_delay': 0.1,
                'lamtha': 100.}]

    for i,synParams in enumerate(synParamsList):
        netParams.connParams['extPoisson->L2Pyr_%d'%(i)] = { 
            'preConds': {'pop': 'extPoisson_L2Pyr'}, 
            'postConds': {'pop': 'L2Pyr'},
            'synMech': synParams['synMech'],
            'weight': weightDistFunc.format(**synParams),
            'delay': delayDistFunc.format(**synParams),
            'connList': conn1to1Pyr,
            'synsPerConn': 3,
            'sec': ['basal_2', 'basal_3','apical_oblique']}


    # Poisson inputs -> L5 Pyr
    netParams.popParams['extPoisson_L5Pyr'] = {
        'cellModel': 'VecStim',
        'numCells': cellsPerPop['L5Pyr'],
        'xRange': [extLocX, extLocX],
        'yRange': [extLocY, extLocY],
        'zRange': [extLocZ, extLocZ],
        'seed': int(getattr(cfg, 'prng_seedcore_extpois')),
        'spikePattern': {
                'type': 'poisson',
                'start': getattr(cfg, 't0_pois'),
                'stop': getattr(cfg, 'T_pois'),
                'frequency': getattr(cfg, 'L5Pyr_Pois_lamtha')}}

    synParamsList = [{'synMech': 'L5Pyr_AMPA',
                'A_weight': getattr(cfg, 'L5Pyr_Pois_A_weight_ampa'),
                'A_delay': 0.1,
                'lamtha': 100.},

                {'synMech': 'L5Pyr_NMDA',
                'A_weight': getattr(cfg, 'L5Pyr_Pois_A_weight_nmda'),
                'A_delay': 0.1,
                'lamtha': 100.}]

    for i,synParams in enumerate(synParamsList):
        netParams.connParams['extPoisson->L5Pyr_%d'%(i)] = { 
            'preConds': {'pop': 'extPoisson_L5Pyr'}, 
            'postConds': {'pop': 'L5Pyr'},
            'synMech': synParams['synMech'],
            'weight': weightDistFunc.format(**synParams),
            'delay': delayDistFunc.format(**synParams),
            'connList': conn1to1Pyr,
            'synsPerConn': 3,
            'sec': ['basal_2', 'basal_3','apical_oblique']}


    # Poisson inputs -> L2 Basket
    netParams.popParams['extPoisson_L2Basket'] = {
        'cellModel': 'VecStim',
        'numCells': cellsPerPop['L2Basket'],
        'xRange': [extLocX, extLocX],
        'yRange': [extLocY, extLocY],
        'zRange': [extLocZ, extLocZ],
        'seed': int(getattr(cfg, 'prng_seedcore_extpois')),
        'spikePattern': {
                'type': 'poisson',
                'start': getattr(cfg, 't0_pois'),
                'stop': getattr(cfg, 'T_pois'),
                'frequency': getattr(cfg, 'L2Basket_Pois_lamtha')}}

    synParamsList = [{'synMech': 'AMPA',
                'A_weight': getattr(cfg, 'L2Basket_Pois_A_weight_ampa'),
                'A_delay': 1.0,
                'lamtha': 100.},

                {'synMech': 'NMDA',
                'A_weight': getattr(cfg, 'L2Basket_Pois_A_weight_nmda'),
                'A_delay': 1.0,
                'lamtha': 100.}]

    for i,synParams in enumerate(synParamsList):
        netParams.connParams['extPoisson->L2Basket_%d'%(i)] = { 
            'preConds': {'pop': 'extPoisson_L2Basket'}, 
            'postConds': {'pop': 'L2Basket'},
            'synMech': synParams['synMech'],
            'weight': weightDistFunc.format(**synParams),
            'delay': delayDistFunc.format(**synParams),
            'connList': conn1to1Basket,
            'synsPerConn': 1,
            'sec': ['soma']}


    # Poisson inputs -> L5 Basket
    netParams.popParams['extPoisson_L5Basket'] = {
        'cellModel': 'VecStim',
        'numCells': cellsPerPop['L5Basket'],
        'xRange': [extLocX, extLocX],
        'yRange': [extLocY, extLocY],
        'zRange': [extLocZ, extLocZ],
        'seed': int(getattr(cfg, 'prng_seedcore_extpois')),
        'spikePattern': {
                'type': 'poisson',
                'start': getattr(cfg, 't0_pois'),
                'stop': getattr(cfg, 'T_pois'),
                'frequency': getattr(cfg, 'L5Basket_Pois_lamtha')}}

    synParamsList = [{'synMech': 'AMPA',
                'A_weight': getattr(cfg, 'L5Basket_Pois_A_weight_ampa'),
                'A_delay': 1.0,
                'lamtha': 100.},

                {'synMech': 'NMDA',
                'A_weight': getattr(cfg, 'L5Basket_Pois_A_weight_nmda'),
                'A_delay': 1.0,
                'lamtha': 100.}]

    for i,synParams in enumerate(synParamsList):
        netParams.connParams['extPoisson->L5Basket_%d'%(i)] = { 
            'preConds': {'pop': 'extPoisson_L5Basket'}, 
            'postConds': {'pop': 'L5Basket'},
            'synMech': synParams['synMech'],
            'weight': weightDistFunc.format(**synParams),
            'delay': delayDistFunc.format(**synParams),
            'connList': conn1to1Basket,
            'synsPerConn': 1,
            'sec': ['soma']}


#------------------------------------------------------------------------------
# Gaussian-distributed inputs parameters 
#------------------------------------------------------------------------------

if cfg.gaussInputs:

    # Gaussian inputs -> L2 Pyr
    netParams.popParams['extGauss_L2Pyr'] = {
        'cellModel': 'VecStim',
        'numCells': 1,
        'xRange': [extLocX, extLocX],
        'yRange': [extLocY, extLocY],
        'zRange': [extLocZ, extLocZ],
        'seed': int(getattr(cfg, 'prng_seedcore_extgauss')),
        'spikePattern': {
                'type': 'gauss',
                'mu': getattr(cfg, 'L2Pyr_Gauss_mu'),
                'sigma': getattr(cfg, 'L2Pyr_Gauss_sigma')}}

    synParams = {'synMech': 'L2Pyr_AMPA',
                'A_weight': getattr(cfg, 'L2Pyr_Gauss_A_weight'),
                'A_delay': 0.1,
                'lamtha': 100.}

    netParams.connParams['extGauss->L2Pyr'] = { 
        'preConds': {'pop': 'extGauss_L2Pyr'}, 
        'postConds': {'pop': 'L2Pyr'},
        'synMech': synParams['synMech'],
        'weight': weightDistFunc.format(**synParams),
        'delay': delayDistFunc.format(**synParams),
        'synsPerConn': 3,
        'sec': ['basal_2', 'basal_3','apical_oblique']}


    # Gaussian inputs -> L5 Pyr
    netParams.popParams['extGauss_L5Pyr'] = {
        'cellModel': 'VecStim',
        'numCells': 1,
        'xRange': [extLocX, extLocX],
        'yRange': [extLocY, extLocY],
        'zRange': [extLocZ, extLocZ],
        'seed': int(getattr(cfg, 'prng_seedcore_extgauss')),
        'spikePattern': {
                'type': 'gauss',
                'mu': getattr(cfg, 'L5Pyr_Gauss_mu'),
                'sigma': getattr(cfg, 'L5Pyr_Gauss_sigma')}}

    synParams = {'synMech': 'L5Pyr_AMPA',
                'A_weight': getattr(cfg, 'L5Pyr_Gauss_A_weight'),
                'A_delay': 0.1,
                'lamtha': 100.}

    netParams.connParams['extGauss->L5Pyr'] = { 
        'preConds': {'pop': 'extGauss_L5Pyr'}, 
        'postConds': {'pop': 'L5Pyr'},
        'synMech': synParams['synMech'],
        'weight': weightDistFunc.format(**synParams),
        'delay': delayDistFunc.format(**synParams),
        'synsPerConn': 3,
        'sec': ['basal_2', 'basal_3','apical_oblique']}

'''