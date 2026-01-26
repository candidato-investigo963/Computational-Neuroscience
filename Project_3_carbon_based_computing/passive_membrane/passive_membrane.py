from __future__ import print_function
"""
Created on Wed Apr 22 15:53:00 2015

Charging and discharging curves for passive membrane patch

"""

# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Input current (in nanoamps)
I = 10 #

C = 0.1 # Membrane capacitance in nF
R = 100 # Leak resistance in MOhms

# Theoretical membrane time constant tau = R * C
tau = R*C
print('C = %.3f nF' % C)
print('R = %.3f M ohms' % R)
print('tau = %.3f ms' % tau)
print('(Theoretical)')

# Membrane equation:
# dV/dt = -V/(R*C) + I/C

# Total simulation time in ms
tstop = 150 

# Theoretical steady-state voltage
V_inf = I * R  # Peak membrane voltage in mV

# Variable to store experimentally measured time constant
tau = 0 # Experimental tau (ms)


# Time step for numerical integration
h = 0.2  # ms

V = 0  # Initial membrane voltage in mV
V_trace = [V]  # Store voltage values over time


for t in np.arange(h, tstop, h):

   # Euler method to update membrane voltage
   # dV/dt = -V/(R*C) + I/C
   V = V +h*(- (V/(R*C)) + (I/C))

   # Estimate the experimental time constant
   # Tau is reached when voltage reaches ~63.2% of V_inf
   if (not tau and (V > 0.6321*V_inf)):
     tau = t
     print('tau = %.3f ms' % tau)
     print('(Experimental)')

   # Turn off the input current after 60% of the simulation time
   if t >= 0.6*tstop:
     I = 0
      
   # Store voltage value
   V_trace += [V]
   
   # Plot the voltage trace every 10 ms
   if t % 10 == 0:
       plt.plot(np.arange(0,t+h, h), V_trace, color='r')
       plt.xlim(0, tstop)
       plt.ylim(0, V_inf)
       plt.draw()
       
plt.show()
