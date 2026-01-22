"""
Created on Wed Apr 22 15:15:16 2015

Quiz 2 code.
"""

# Import necessary libraries
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import pickle

from compute_sta import compute_sta

# Load data
FILENAME = 'c1p8.pickle'

with open(FILENAME, 'rb') as f:
    data = pickle.load(f)

stim = data['stim']  # stimulus vector
rho = data['rho']    # spike-train (binary vector)

# PARAMETERS TO FILL IN BASED ON THE PROYECT:
# The dataset has a sampling rate of 500 Hz → sampling period = 1/500 s = 2 ms
sampling_period = 2

# We want 300 ms window before each spike, at 2 ms per step → num_timesteps = 300 / 2 = 150 ms
num_timesteps = 150

# Compute spike-triggered average using our function
sta = compute_sta(stim, rho, num_timesteps)

# Print total number of spikes considered
print("Total spikes counted:", len(rho[num_timesteps:].nonzero()[0]))

# Create time axis for plotting (-num_timesteps*sampling_period to 0)
time = (np.arange(-num_timesteps, 0) + 1) * sampling_period

# Plot STA
plt.plot(time, sta)
plt.xlabel('Time (ms)')
plt.ylabel('Stimulus')
plt.title('Spike-Triggered Average')
plt.savefig("sta_plot.png", dpi=300, bbox_inches="tight")
plt.show()
