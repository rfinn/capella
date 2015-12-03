
# coding: utf-8

# This program calculates R200 in degrees given the central velocity and velocity dispersion.

# In[27]:

from astropy.cosmology import FlatLambdaCDM
import numpy as np
cosmo = FlatLambdaCDM(H0=70, Om0=0.3)
OmL=.7
Om0=.3
H0=70.
def getr200(recessionvel,sigma):
    redshift=recessionvel/3.e5
    r200=2.02*(sigma)/1000./np.sqrt(OmL+Om0*(1.+redshift)**3)*H0/70. # in Mpc
    r200deg=r200/cosmo.angular_diameter_distance(redshift)*180./np.pi
    return r200deg.value

