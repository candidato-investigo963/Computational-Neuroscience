# Population Vector Decoding of a Directional Stimulus

## Description

This project decodes the direction of an unknown sensory stimulus using a population vector method. Instead of relying on a single neuron, the model combines the responses of multiple neurons, each characterized by a preferred direction and a stimulus-dependent firing rate, to recover a single population-level estimate of stimulus direction.

---

## Methods

### Dataset

Two Python (`.pickle`) files are used:

- **Population coding data**  
  Contains firing rate responses (`r1`–`r4`) of four neurons to an unknown stimulus across multiple trials, along with their preferred direction vectors (`c1`–`c4`).

- **Tuning curve data**  
  Contains firing rates of the same neurons across known stimulus directions, used to compute the maximum mean firing rate for each neuron.

---

### Population Vector Decoding

The decoding process follows three main steps:

- Compute the **mean firing rate** of each neuron across trials for the unknown stimulus.
- Normalize each response by the neuron's **maximum tuning curve value**, producing a weight for its contribution.
- Sum the **weighted preferred direction vectors** to form a single population vector.

The resulting vector is converted from Cartesian coordinates to an angular estimate, following the convention:
- **0° = North (positive y-axis)**  
- **90° = East (positive x-axis)**

---

## Results

The decoded population vector is **112°**, providing a single estimate of the unknown stimulus direction. This value reflects the combined influence of all neurons, demonstrating how unequal neural activity can be transformed into a meaningful sensory estimate at the population level.

---

## Files

- `_e96f8f1cf1f8256c8595dcb9668fee4f_pop_coding_3.4.pickle`  
  Population coding dataset containing firing rates and preferred direction vectors.

- `_e96f8f1cf1f8256c8595dcb9668fee4f_tuning_3.4.pickle`  
  Tuning curve dataset used to compute normalization values for each neuron.

- `population_vector_decoding.py`  
  Python script implementing the population vector decoding method.

