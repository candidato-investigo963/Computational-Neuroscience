# Project 1 – Spike-Triggered Average (STA)

## Description
This project implements a Spike-Triggered Average (STA) analysis to study
neural encoding. The goal is to estimate the linear filter of a neuron by
averaging the stimulus preceding each spike.

The dataset contains:
- A stimulus time series (`stim`)
- A binary spike train (`rho`), where 1 indicates a spike

The sampling rate of the data is 500 Hz.

## Method
- Sampling period: 2 ms (1 / 500 Hz)
- Time window: 300 ms before each spike
- Number of time steps: 150

Spikes occurring before the first 300 ms are excluded.
For each spike, the stimulus segment preceding it is extracted and averaged
across all spikes to compute the STA.

## Results
The resulting STA represents the linear receptive field of the neuron.

![Spike-Triggered Average](sta_plot.png)

## Files
- `compute_sta.py`: function to compute the spike-triggered average
- `quiz.py`: main script that loads data, computes the STA and plots results
- `c1p8.pickle`: dataset used in the analysis

