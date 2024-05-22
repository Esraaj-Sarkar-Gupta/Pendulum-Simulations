# Example of how to solve first order differential equations using odeint from scipy.

import numpy as np
from scipy.integrate import odeint

def D(x,t,k):
    sigma = x**2
    return k*(-x)
k = 5

x0 = 2

t = np.linspace(0, 5, 500)
    
x = odeint(D , x0 , t , args=(k,))
print(f"The first 5 solution values for x are: {x[:5]}")
#print(f"The numerical solution to x is {x}")

import matplotlib.pyplot as plt
plt.plot(t, x)
plt.xlabel("Time (t)")
plt.ylabel("y(t)")
title = f"Solution of dx/dt = -{k}x with x(0) = 2"
plt.title(title)
plt.grid()
plt.show()
