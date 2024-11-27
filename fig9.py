import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np 
import math 
import matplotlib.ticker as ticker


matplotlib.rcParams.update({'font.size': 12})
matplotlib.rcParams["font.family"] = "Times New Roman"

def cond_median(i_set):
    ''' i_set - is the set current in microamperes'''
    a = 3.99      # interval (3.863, 4.118)
    b = 0.7713    # interval (0.7655, 0.77711)
    return a*pow(i_set, b)


def cond_sd_(i_set):
    '''percentage standard deviation as a function of i_set'''
    c = 2509
    d = -1.38
    return (c*pow(i_set, d)/100)

array_length = 64
array_width = 32
array_size = array_length * array_width


def conductance_map(i_set, array_size):
    mu = cond_median(i_set)
    sigma = mu * cond_sd_(i_set)
    conductances = np.random.normal(mu, sigma, array_size)
    return conductances

x1 = conductance_map(25, array_size)
x2 = conductance_map(25, array_size)
z1 = conductance_map(35, array_size)
z2 = conductance_map(35, array_size)
x = x1 - x2						# final conductances in the differential configuration
z = z1 - z2						# calculated by doing Gpos - Gneg

y = np.reshape(x, (array_length, array_width))
a = np.reshape(z, (array_length, array_width))

# figure(figsize=(4,3))
fig, (ax1, ax2) = plt.subplots(1, 2, constrained_layout=True)
im1 = ax1.imshow(y, cmap='RdBu')
im2 = ax2.imshow(a, cmap='RdBu')
cbar_1 = plt.colorbar(im1, ax=ax1, fraction=0.1)
cbar_2 = plt.colorbar(im2, ax=ax2, fraction=0.1)

cbar_1.set_label(f'Conductance ($\mu$s)')
cbar_2.set_label(f'Conductance ($\mu$s)')

# plt.savefig("random_conductance_maps.pdf", transparent=True, dpi=300, bbox_inches='tight')
plt.show() 