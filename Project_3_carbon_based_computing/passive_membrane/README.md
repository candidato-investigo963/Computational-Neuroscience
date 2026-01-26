# Passive Membrane Dynamics (RC Model)

## Description

This project models the electrical behavior of a passive neuronal membrane using its equivalent RC circuit representation. The membrane is treated as a capacitor and a leak resistance connected in parallel, and its voltage response is simulated under a constant injected current.

The goal is to study how membrane voltage evolves over time, how quickly it reaches a steady-state value, and how this behavior depends on the physical properties of the membrane, such as resistance and capacitance. This analysis provides a direct link between basic electrical circuit theory and the biophysical foundations of neuronal dynamics.

---

## Methods

### Dataset

This project does not rely on an external dataset. Instead, all data are generated through numerical simulation based on a biophysical model of a passive membrane.

The model uses the differential equation:

$$\frac{dV}{dt} = -\frac{V}{RC} + \frac{I}{C}$$

Where:
- **V** is the membrane voltage  
- **R** is the membrane resistance  
- **C** is the membrane capacitance  
- **I** is the injected current  

The equation is solved numerically using the **Euler integration method**, which updates the membrane voltage at small time steps to approximate the continuous-time solution.

### Simulation Parameters

- Input current: **10 nA**  
- Membrane resistance: **100 MΩ**  
- Membrane capacitance: **0.1 nF**  
- Time step: **0.2 ms**  
- Total simulation time: **150 ms**

The injected current is turned off after 60% of the simulation time to observe both the **charging** and **discharging** phases of the membrane.

---

## Results

### Voltage Dynamics

The membrane voltage exhibits a characteristic **exponential rise** while the current is applied, followed by an **exponential decay** once the current is turned off.

![Passive membrane response](passive_membrane_RC.png)

During the charging phase, the voltage approaches a steady-state value determined by:

$$V_{\infty} = I \cdot R$$

The simulation also measures the membrane time constant experimentally by recording the time at which the voltage reaches approximately 63.2% of its maximum value. The output shows:

- C = 0.100 nF
- R = 100.000 M ohms
- tau = 10.000 ms
  (Theoretical)
- tau = 10.000 ms
  (Experimental)


This confirms that the experimentally measured time constant matches the theoretical prediction:

$$\tau = R \cdot C = 10 \text{ ms}$$

---

## Interpretation

### Question 1 — Steady-State Voltage  
If the input current is never turned off, the membrane voltage will continue rising until it reaches a stable value where the injected current is exactly balanced by the leak current through the resistance. This steady-state voltage is given by:

$$V_{\infty} = I \cdot R$$

Using the parameters in the script, the membrane converges to **1000 mV**.

---

### Question 2 — Effect of Increasing Resistance  
Multiplying the resistance by 5 increases the membrane time constant:

$$\tau = R \cdot C$$

This causes the membrane to reach its steady-state voltage **more slowly**, because the system responds more sluggishly to changes in input current.

---

### Question 3 — Effect of Decreasing Capacitance  
Dividing the capacitance by 10 reduces the membrane time constant. This allows the voltage to change more rapidly, so the membrane reaches steady state **more quickly**.

---

### Question 4 — Combined Change in R and C  
Multiplying resistance by 10 and dividing capacitance by 10 leaves the product $$\tau = R \cdot C$$ unchanged. As a result, the membrane reaches steady state at **the same rate**, even though the individual electrical properties have changed.

---

### Question 5 — Theoretical Justification of the Time Constant Method  

Solving the membrane equation:

$$\frac{dV}{dt} = -\frac{V}{RC} + \frac{I}{C}, \quad V(0) = 0$$

yields the solution:

$$V(t) = IR \left(1 - e^{-t/\tau} \right)$$

$$\text{where } \tau = RC$$

At $t = \tau$, this becomes:

$$V(\tau) = IR \left(1 - e^{-1} \right) \approx 0.6321 \cdot IR$$

This explains why measuring the time at which the voltage reaches **63.2% of its peak value** provides a direct and reliable experimental estimate of the membrane time constant, independent of the injected current.

---

## Files

- `passive_membrane.py`  
  Python script that simulates membrane charging and discharging using an RC model and estimates the membrane time constant.

- `passive_membrane_RC.png`  
  Plot showing the exponential rise and decay of membrane voltage over time.
