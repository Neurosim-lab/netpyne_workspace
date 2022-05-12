from netpyne import specs

# Simulation options
cfg = specs.SimConfig()           # object of class SimConfig to store simulation configuration

cfg.duration = 1*1e3                      # Duration of the simulation, in ms
cfg.dt = 0.025                            # Internal integration timestep to use
cfg.verbose = False                       # Show detailed messages
cfg.recordTraces = {'V_soma': {'sec':'soma','loc':0.5, 'var':'v'}}  # Dict with traces to record
cfg.recordStep = 0.1                      # Step size in ms to save data (e.g. V traces, LFP, etc)
cfg.filename = 'model_output'             # Set file output name
cfg.savePickle = False                    # Save params, network and sim output to pickle file

cfg.analysis['plotTraces'] = {'include': [1]}                           # Plot recorded traces for this list of cells
cfg.analysis['plotRaster'] = {'orderInverse': True, 'syncLines': True}  # Plot a raster
cfg.analysis['plotSpikeHist'] = {'include': ['E', 'I']}                 # Plot spike histogram
cfg.analysis['plotRateSpectrogram'] = {'include': ['allCells']}         # Plot binned spiking rate spectrogram
