# Project 1 – Spike-Triggered Average (STA)

## Description
This project implements a Spike-Triggered Average (STA) analysis to investigate neural encoding mechanisms. The STA is a classical technique in computational neuroscience used to estimate the linear temporal filter of a neuron by averaging the stimulus segments that precede each spike.

The dataset contains:
- A stimulus time series (`stim`)
- A binary spike train (`rho`), where 1 indicates a spike

The sampling rate of the data is 500 Hz.

## Method
- Sampling period: 2 ms (1 / 500 Hz)
- Time window: 300 ms before each spike
- Number of time steps: 150

Spikes occurring before the first 300 ms are excluded to ensure that all stimulus segments have equal length.

For each remaining spike, the stimulus segment immediately preceding the spike is extracted. These segments are summed and averaged across all spikes to compute the Spike-Triggered Average (STA), providing an estimate of the neuron’s linear temporal filter.

## Results
The computed STA shows a smooth temporal structure with a gradual increase in stimulus amplitude leading up to the spike, followed by a sharp drop immediately before spike time.

![Spike-Triggered Average](sta_plot.png)

## Interpretation
The shape of the STA is consistent with a leaky integrator model of neuronal processing. The neuron integrates incoming stimulus over time, but the influence of past stimuli decays progressively due to the passive properties of the membrane. As a result, recent stimuli contribute more strongly to spike generation than older inputs

## Files
- `compute_sta.py`: function to compute the spike-triggered average
- `quiz.py`: main script that loads data, computes the STA and plots results
- `c1p8.pickle`: dataset used in the analysis

