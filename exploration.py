# add robust points in polyhedron
import sys
sys.path.append('./msdfninfer/')

import porepy as pp
import numpy as np
import scipy.sparse as sps

from porepy.fracs.fracture_importer import network_3d_from_fab

# this works
dfn = network_3d_from_fab('./data/a2_stages.fab', return_all=False)
dfn_small = pp.FractureNetwork3d(dfn[0:2])

# experiment with meshing
# works with a very small network of fractures
mesh_args = {'mesh_size_frac': 100, 'mesh_size_min': 10}
mesh_small = dfn_small.mesh(mesh_args)
mesh_small.cell_centers()

# this works with paraview
dfn.to_file('a2_stages.vtu')

# get domain of all fractures
dfn

# get a single fracture
f0 = dfn[0]

# this works - finds intersections and generates
# non-intersecting polygons
dfn.split_intersections()