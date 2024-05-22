import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

print("Comparing the solutions of linear and non-linear differnetial euqations for small θ such that sin(θ) ≈ θ for the equation d²θ/dt² + ω²sin(θ) = 0.")

def system_simple(v, t, Omega):  # ω^2 = Ω
  theta, theta_dot = v # Unpack state vector
  d_theta_dot_dt = -Omega * theta  # Derivative of theta
  d_theta_dt = theta_dot
  return [d_theta_dt, d_theta_dot_dt]  # Return derivatives as a list

# Initial states:
theta0 = np.pi/2 # amplitude if theta_dot0 = 0 !!!!
theta_dot0 = 0  # Initial angular velocity
v0 = [theta0, theta_dot0]

Omega = 4 # value of ω^2


def system(v, t, Omega):  # defining the eqation of motion where ω^2 = Ω
  theta, theta_dot = v # Unpack state vector
  d_theta_dot_dt = -Omega * np.sin(theta)  # Derivative of theta
  d_theta_dt = theta_dot
  return [d_theta_dt, d_theta_dot_dt]  # Return derivatives as a list

t = np.linspace(0, 30, 3000) # setting bounds for simulated time

sol_simple = odeint(system_simple, v0, t, args=(Omega,)) # solving simple DE solution
theta = sol_simple[:, 0] # assigning theta values from solution of linear system 
plt.plot(t , theta , color = 'blue' , label = 'Simple system') # plotting simple solution

plt.xlabel("Time (t)")
plt.ylabel("Position (θ)")
plt.title(f"Comparing the solution of d²θ/dt² + {Omega}sin(θ) = 0 to d²θ/dt² + {Omega}θ = 0 with θ(0) = {theta0} and θ'(0) = {theta_dot0}")

sol = odeint(system, v0, t, args=(Omega,)) # solving system
theta = sol[: , 0] # assigning theta values from non-linear system 
plt.plot(t , theta , color = 'red' , label = 'Non-linear sytem')

plt.grid()
plt.legend(loc = 'upper left' , title = "Solutions: ")
plt.show()




