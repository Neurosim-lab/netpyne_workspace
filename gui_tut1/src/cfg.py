from netpyne import specs

# Simulation options
cfg = specs.SimConfig()		# object of class SimConfig to store simulation configuration

cfg.duration = 0.2*1e3 			# Duration of the simulation, in ms
cfg.dt = 0.1 				# Internal integration timestep to use
cfg.verbose = False  			# Show detailed messages 
cfg.recordTraces = {'V_soma':{'sec':'soma','loc':0.5,'var':'v'},
						 'V_dend': {'sec': 'dend', 'loc': 1.0, 'var':'v'}}  # Dict with traces to record
cfg.recordCells = [0]
cfg.recordStep = 0.1 			# Step size in ms to save data (eg. V traces, LFP, etc)
cfg.filename = 'gui_tut1'  # Set file output name
cfg.saveJson = False		# Save params, network and sim output to pickle file
cfg.analysis['iplotTraces'] = {'include': [0], 'overlay': True}
cfg.analysis['iplotRaster'] = {'markerSize': 5, 'showFig': True}
