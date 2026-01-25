# -*- coding: utf-8 -*-
"""
Created on Mon Jan 19 05:34:34 2026

"""

import pickle
import numpy as np
import matplotlib.pyplot as plt

# Load the data
with open('_e96f8f1cf1f8256c8595dcb9668fee4f_tuning_3.4.pickle', 'rb') as f:
    data = pickle.load(f)

# Check keys
print(data.keys())  # Should show something like: dict_keys(['stim', 'neuron1', 'neuron2', 'neuron3', 'neuron4'])

neuron1 = data['neuron1']
print(neuron1)

# Extract stimuli
stim = data['stim']
print(stim)

# Function to compute mean firing rate and plot tuning curve for a neuron
def plot_tuning(neuron_data, neuron_name):
    mean_firing = np.mean(neuron_data, axis=0)  # Mean over trials for each stimulus
    plt.plot(stim, mean_firing, 'o-', label=neuron_name)
    plt.xlabel('Stimulus (air direction)')
    plt.ylabel('Mean firing rate (Hz)')
    plt.title(f'Tuning curve of {neuron_name}')
    plt.legend()

# Plot tuning curves for all neurons
plt.figure(figsize=(10,6))
plot_tuning(data['neuron1'], 'Neuron 1')
plot_tuning(data['neuron2'], 'Neuron 2')
plot_tuning(data['neuron3'], 'Neuron 3')
plot_tuning(data['neuron4'], 'Neuron 4')
plt.show()


def check_poisson(neuron_data, neuron_name):
    mean_r = np.mean(neuron_data, axis=0)
    var_r = np.var(neuron_data, axis=0)
    
    # Evitamos dividir por cero donde la tasa es 0
    ratio = np.divide(var_r, mean_r, out=np.zeros_like(var_r), where=mean_r!=0)
    
    print(f"--- {neuron_name} ---")
    print(f"Media de los ratios (Var/Mean): {np.mean(ratio[ratio>0]):.4f}")
    # Si es Poisson, la desviación estándar del ratio debería ser casi 0
    print(f"Consistencia (Std Dev del ratio): {np.std(ratio[ratio>0]):.4f}\n")

for i in range(1, 5):
    check_poisson(data[f'neuron{i}'], f'Neuron {i}')

