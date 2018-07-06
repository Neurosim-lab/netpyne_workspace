from neuron import h
from neuron import crxd as rxd
from matplotlib import pyplot as plt
from matplotlib_scalebar import scalebar

rxd.nthread(4)
intra = 1
extra = 1


# ---------------------
# rxd extracellular
# ---------------------
if extra:
    margin = 20
    naic_init, naoc_init = 10, 140
    kic_init, koc_init = 54.4, 2.5
    x, y, z = [0-margin, 100+margin], [-500-margin, 0+margin], [0-margin, 100+margin]
    #cytosol = rxd.Region(h.allsec(), nrn_region='i')
    rxd.options.enable.extracellular = True
    extracellular = rxd.Extracellular(xlo=x[0], ylo=y[0], zlo=z[0], xhi=x[1], yhi=y[1], zhi=z[1], dx=5, volume_fraction=0.2, tortuosity=1.6) #vol_fraction and tortuosity associated w region 
    
    #na = rxd.Species([extracellular,cytosol], name='na', charge=1, d=1.78, initial= lambda nd: naoc_init if isinstance(nd,rxd.node.NodeExtracellular) else naic_init)
    #k = rxd.Species([extracellular, cytosol], name='k', charge=1, d=2.62, initial= lambda nd: koc_init if isinstance(nd,rxd.node.NodeExtracellular) else kic_init)

    # plot funcs
    def plotExtracellularConcentration(species, extracellular=extracellular,  plane='xy'):
        plt.figure()
        plane2mean = {'xz': 1, 'xy': 2}
        plt.imshow(species[extracellular].states3d[:].mean(plane2mean[plane]).T, interpolation='nearest', origin='upper')  #  extent=k[extracellular].extent('xy')
        sb = scalebar.ScaleBar(1e-6)
        sb.location='lower left'
        ax = plt.gca()
        ax.xaxis.set_visible(False)
        ax.yaxis.set_visible(False)
        plt.xlabel(plane[0])
        plt.ylabel(plane[1])
        ax.add_artist(sb)
        plt.colorbar(label="$%s^+$ (mM)"%(species.name))
        plt.ion()
        plt.show()

    # other plotting func: http://docs.enthought.com/mayavi/mayavi/auto/example_volume_slicer.html


# ---------------------
# rxd intracellular 
# ---------------------
if intra:
    # parameters
    caDiff = 0.08
    ip3Diff = 1.41
    caci_init = 1e-4# 1e-4
    caco_init = 2.0
    ip3_init = 0 # 1
    gip3r = 12040 * 100
    gserca = 0.3913
    gleak = 6.020 
    kserca = 0.1
    kip3 = 0.15
    kact = 0.4
    ip3rtau = 2000 
    fc = 0.8
    fe = 0.2

    # create Regions
    cyt = rxd.Region(h.allsec(), nrn_region='i', geometry=rxd.FractionalVolume(fc, surface_fraction=1))
    er = rxd.Region(h.allsec(), geometry=rxd.FractionalVolume(fe))
    cyt_er_membrane = rxd.Region(h.allsec(), geometry=rxd.ScalableBorder(1, on_cell_surface=False))

    # create Species 
    ca = rxd.Species([cyt, er, extracellular], d=caDiff, name='ca', charge=2, 
        initial=lambda nd: caco_init if isinstance(nd,rxd.node.NodeExtracellular) else (0.0017 - caci_init * fc) / fe if nd.region == er else caci_init)
    ip3 = rxd.Species(cyt, d=ip3Diff, name='ip3', initial=ip3_init)
    ip3r_gate_state = rxd.State(cyt_er_membrane, initial=0.8)


    # naic_init, naoc_init = 10, 140
    # kic_init, koc_init = 54.4, 2.5
    # na = rxd.Species([cyt], name='na', charge=1, d=1.78, initial=naic_init)
    # k = rxd.Species([cyt], name='k', charge=1, d=2.62, initial=kic_init)


    # create Reactions 
    serca = rxd.MultiCompartmentReaction(ca[cyt], ca[er], gserca / ((kserca / (1000. * ca[cyt])) ** 2 + 1), membrane=cyt_er_membrane, custom_dynamics=True)
    leak = rxd.MultiCompartmentReaction(ca[er], ca[cyt], gleak, gleak, membrane=cyt_er_membrane)

    minf = ip3[cyt] * 1000. * ca[cyt] / (ip3[cyt] + kip3) / (1000. * ca[cyt] + kact)
    h_gate = ip3r_gate_state[cyt_er_membrane]
    kip3 = gip3r * (minf * h_gate) ** 3
    ip3r = rxd.MultiCompartmentReaction(ca[er], ca[cyt], kip3, kip3, membrane=cyt_er_membrane)
    ip3rg = rxd.Rate(h_gate, (1. / (1 + 1000. * ca[cyt] / (0.3)) - h_gate) / ip3rtau)


