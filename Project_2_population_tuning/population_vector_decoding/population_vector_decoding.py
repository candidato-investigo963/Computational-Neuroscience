# -*- coding: utf-8 -*-
"""
Created on Mon Jan 19 15:41:28 2026

"""

import numpy as np
import pickle

# Load population coding data
with open('_e96f8f1cf1f8256c8595dcb9668fee4f_pop_coding_3.4.pickle', 'rb') as f:
    pop = pickle.load(f)

# Load tuning data
with open('_e96f8f1cf1f8256c8595dcb9668fee4f_tuning_3.4.pickle', 'rb') as f:
    tuning = pickle.load(f)

# Compute r_max for each neuron
rmax = {}
for i in range(1, 5):
    mean_tuning = np.mean(tuning[f'neuron{i}'], axis=0)
    rmax[i] = np.max(mean_tuning)

# Population vector
Vx, Vy = 0.0, 0.0

for i in range(1, 5):
    r_mean = np.mean(pop[f'r{i}'])        # mean firing rate
    ci = pop[f'c{i}']                     # preferred direction vector
    weight = r_mean / rmax[i]
    
    Vx += weight * ci[0]
    Vy += weight * ci[1]

# Convert to angle (0° = north, 90° = east)
angle_rad = np.arctan2(Vx, Vy)
angle_deg = np.degrees(angle_rad)
angle_deg = angle_deg % 360

print(round(angle_deg))


