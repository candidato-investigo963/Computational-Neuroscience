# Population Tuning and Poisson Model Validation

## Description

This project analyzes the response properties of a small neural population to a directional sensory stimulus (air flow direction). The goal is to characterize how individual neurons encode stimulus information through their firing rates and to evaluate whether their spike count variability follows a Poisson statistical model.

The study focuses on two main aspects of neural coding:

- **Sensory tuning**: How selectively each neuron responds to different stimulus directions.  
- **Spike statistics**: Whether the variability of neural firing can be explained by a Poisson process.

---

## Methods

### Dataset

The dataset is stored in a Python (`.pickle`) file and contains:

- A vector of stimulus values representing air direction angles.  
- Neural response matrices for four neurons.

Each matrix is structured as:
- **Rows**: repeated trials  
- **Columns**: stimulus conditions

---

### Tuning Curve Analysis

For each neuron, the mean firing rate is computed across trials for every stimulus direction. This produces a tuning curve that describes the neuron's stimulus preference and selectivity.

The tuning curves are plotted together to allow direct comparison between neurons in terms of:

- Preferred stimulus direction  
- Response amplitude  
- Tuning width (Narrow tuning indicates high selectivity, while broad tuning suggests a more general response profile)

---

### Poisson Model Validation

To evaluate whether neural firing follows Poisson-like statistics, the variance-to-mean ratio (Fano Factor) is computed for each stimulus condition:

$$F = \frac{\text{Variance}}{\text{Mean}}$$

For a Poisson process, this ratio is expected to be close to 1. The script computes:

- The average Fano Factor across stimuli  
- The standard deviation of the ratio

---

## Results

### Tuning Curves

![Tuning Curves](tuning_curves.png)

The tuning curves show that each neuron is selectively responsive to a different range of stimulus directions, indicating distributed sensory encoding across the population.

- Neuron 1 and Neuron 4 exhibit strong and well-defined tuning peaks. Specifically, Neuron 1 is highly selective for low air-flow directions, with a preferred stimulus around **50°**. In contrast, Neuron 4 shows an opposite preference, reaching its maximum response when the stimulus approaches **320°**.

- Neurons 2 and 3 complete the coverage of the sensory space by showing tuning in intermediate ranges, with preferred directions around **140°** and **230°**, respectively. Together, these response profiles suggest a population-level representation in which different neurons specialize in different regions of the stimulus domain.

---

### Poisson Statistics

The variance-to-mean ratios reveal different statistical regimes across the neural population.

Because the data are provided as firing rates rather than raw spike counts, the Fano Factor is not expected to be exactly equal to 1. However, a truly Poisson process should still exhibit a stable and proportional relationship between variance and mean across stimulus conditions.

- Neurons 1, 2, and 4 display very low and highly consistent variance-to-mean ratios, indicating that their variability is compatible with Poisson-like firing statistics.

- In contrast, Neuron 3 shows both a higher variance-to-mean ratio and much greater variability of this ratio across stimuli. This makes Neuron 3 the neuron that deviates most strongly from Poisson behavior.

Overall, these results highlight heterogeneity in firing reliability within the neural population, with most neurons exhibiting highly regular responses and one neuron displaying increased variability.

---

## Files

- `_e96f8f1cf1f8256c8595dcb9668fee4f_tuning_3.4.pickle`  
  Serialized dataset containing stimulus values and neural response matrices.

- `population_tuning_and_poisson_model_validation.py`  
  Python script for loading the data, plotting tuning curves, and validating Poisson firing statistics.


