# -*- coding: utf-8 -*-
"""
Population Tuning and Poisson Model Validation
Created on Mon Jan 19 05:34:34 2026

"""

# Import required libraries
import pickle
import numpy as np
import matplotlib.pyplot as plt

# Open the pickle file that contains the stimulus and neural response data
with open('_e96f8f1cf1f8256c8595dcb9668fee4f_tuning_3.4.pickle', 'rb') as f:
    data = pickle.load(f)

# Print the available keys in the dataset to check its contents
print(data.keys()) 

# Extract the responses of neuron 1
neuron1 = data['neuron1']
print(neuron1)

# Extract the stimulus values 
stim = data['stim']
print(stim)

# Function to compute mean firing rate and plot tuning curve for a neuron
def plot_tuning(neuron_data, neuron_name):
    mean_firing = np.mean(neuron_data, axis=0)  # Compute the mean firing rate across trials for each stimulus
    plt.plot(stim, mean_firing, 'o-', label=neuron_name)  # Plot the tuning curve
    plt.xlabel('Stimulus (air direction)')  # Label the ploT
    plt.ylabel('Mean firing rate (Hz)')
    plt.title(f'Tuning curve of {neuron_name}')
    plt.legend()

# Plot tuning curves for each neuron
plt.figure(figsize=(10,6))
plot_tuning(data['neuron1'], 'Neuron 1')
plot_tuning(data['neuron2'], 'Neuron 2')
plot_tuning(data['neuron3'], 'Neuron 3')
plot_tuning(data['neuron4'], 'Neuron 4')
plt.show()

# Function to computes the variance-to-mean ratio (Fano Factor) for each stimulusto evaluate whether the neuron follows Poisson-like firing statistics.
def check_poisson(neuron_data, neuron_name):
    mean_r = np.mean(neuron_data, axis=0) # Compute mean firing rate for each stimulus
    var_r = np.var(neuron_data, axis=0) # Compute variance of firing rate for each stimulus
    
    # Compute variance-to-mean ratio (Fano Factor)
    # Avoid division by zero by only dividing where mean is not zero
    ratio = np.divide(var_r, mean_r, out=np.zeros_like(var_r), where=mean_r!=0)

    # Print results for this neuron
    print(f"--- {neuron_name} ---")
    print(f"Media de los ratios (Var/Mean): {np.mean(ratio[ratio>0]):.4f}")
    # Si es Poisson, la desviación estándar del ratio debería ser casi 0
    print(f"Consistencia (Std Dev del ratio): {np.std(ratio[ratio>0]):.4f}\n")
    
# Loop through all neurons and evaluate their firing statistics
for i in range(1, 5):
    check_poisson(data[f'neuron{i}'], f'Neuron {i}')

