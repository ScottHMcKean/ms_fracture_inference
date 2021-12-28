# add robust points in polyhedron
import sys
sys.path.append('./msdfninfer/')

import porepy as pp
import numpy as np
import scipy.sparse as sps

from porepy.fracs.fracture_importer import network_3d_from_fab, network_3d_from_csv

# you can import a dfn from a .csv or .fab file
dfn = network_3d_from_fab('./data/stage_dfn.fab', return_all=False, tol=1E-3)
dfn = network_3d_from_csv('./data/stage_dfn.csv', return_all=False, tol=1E-3)

# you get set the boundary information by imposing the convex hull of the
# fractures, once all fractures are loaded
dfn.impose_external_boundary()

# see the bounding box here
dfn.bounding_box()

# we can export the fracture network to paraview for 3d visualization
dfn.to_file('a2_stages.vtu')

# call an individual fracture like this
frac = dfn._fractures[6]

# some numerical checks
frac.is_planar()
frac.check_convexity()
 
# dfn to 2D
dfn._fractures[0]

# point to plane distance

# make random point off frac center
point = np.random.normal([0,0,0],[1,1,1]).reshape(3,1) + frac.center

# calculate vector from plane point to center
v = point - frac.center

# dot product gives shortest distance
dist = np.dot(v.reshape(1,3), frac.normal)

# use this distance + vector to calculate likelihood
v_norm = v/np.linalg.norm(v)

# distance components for gaussian
dist_comp = np.abs(dist*v_norm)

# and the probability of the event being on the plane
from scipy.stats import multivariate_normal
# we put the uncertainties of the microseismic event as the covariances
# on the diagonal - assuming independent axes, which is true for microseismic
# events
prob = multivariate_normal.pdf(
    x=dist_comp, 
    mean=[0,0,0], 
    cov=[[1,0,0],[0,1,0],[0,0,100]])

# get probability
# either
np.sum(np.log(prob))
# or
np.log(np.prod(prob))



v_norm

# utility functions
dfn.split_intersections()

# can write out subsetted or modified fracture networks
dfn.to_file('test_dfn.vtu')
dfn.to_csv('test_dfn.csv')
dfn.to_fab('test_dfn.fab')

