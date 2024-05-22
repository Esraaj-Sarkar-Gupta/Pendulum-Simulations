# Solving the secondary differential equation of a pendulum - plotting polar coordinates of possible locations of pendulum.
import numpy as np
from scipy.integrate import odeint
import time as tm
print("Solving the non linear second order differential equation for a single pendulum...")

def system(v, t, Omega):  # defining the eqation of motion where ω^2 = Ω
  theta, theta_dot = v # Unpack state vector
  d_theta_dot_dt = -Omega * np.sin(theta)  # Derivative of theta
  d_theta_dt = theta_dot
  return [d_theta_dt, d_theta_dot_dt]  # Return derivatives as a list

# Initial states:
theta0 = np.pi/2  #amplitude if theta_dot0 = 0
theta_dot0 = 0  # Initial angular velocity
v0 = [theta0, theta_dot0]

Omega = 4 # value of ω^2

# Solve the system
t = np.linspace(0, 30, 3000)

start_time = tm.time() # timing the operation

sol = odeint(system, v0, t, args=(Omega,)) # solving the DE

end_time = tm.time() # timing the operation

theta = sol[:, 0]
theta_dot = sol[:, 1]

# Plot the solution
import matplotlib.pyplot as plt

# plot 3 - polar plot of possible locations:

r = [10 for _ in range(3000)] # storing the value of radius (10m) 3000 times to match with each element in the list theta
    
ax = plt.subplot(111, projection='polar')
ax.set_theta_offset(np.pi*1.5)
ax.plot(theta , r , color = 'green')
plt.title(f"Polar Plot  - Postions of CG of pendulum")
plt.grid()
plt.show()

print(f"The operation took {end_time - start_time} seconds.")
