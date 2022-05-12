from netpyne import specs

# Simulation options
cfg = specs.SimConfig()		# object of class SimConfig to store simulation configuration

cfg.duration = 0.5*1e3 			# Duration of the simulation, in ms
cfg.dt = 0.1			# Internal integration timestep to use
cfg.hParams['celsius'] = 34
cfg.verbose = False  # Show detailed messages 
cfg.recordTraces = {'V_soma':{'sec':'soma','loc':0.5,'var':'v'}}  # Dict with traces to record
cfg.recordStep = 0.1 			# Step size in ms to save data (eg. V traces, LFP, etc)
cfg.filename = 'model_output'  # Set file output name
cfg.savePickle = False 		# Save params, network and sim output to pickle file

cfg.analysis['iplotRaster'] =  {'markerSize': 5, 'showFig': True}
cfg.analysis['iplotTraces'] = {'include': [0,2], 'oneFigPer': 'trace'}
