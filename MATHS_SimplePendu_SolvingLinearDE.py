import numpy as np
from scipy.integrate import odeint

def system(v, t, Omega):  # ω^2 = Ω
  theta, theta_dot = v # Unpack state vector
  d_theta_dot_dt = -Omega * theta  # Derivative of theta
  d_theta_dt = theta_dot
  return [d_theta_dt, d_theta_dot_dt]  # Return derivatives as a list

# Initial states:
theta0 = 10 #amplitude if theta_dot0 = 0
theta_dot0 = 0  # Initial angular velocity
v0 = [theta0, theta_dot0]

Omega = 4 # value of ω^2

# Solve the system
t = np.linspace(0, 10, 1000)

sol = odeint(system, v0, t, args=(Omega,))

theta = sol[:, 0]
theta_dot = sol[:, 1]
# Plot the solution
import matplotlib.pyplot as plt
# plot 1:
plt.plot(t, theta , color = 'blue')
plt.xlabel("Time (t)")
plt.ylabel("Position (θ)")  # Use theta for position
plt.title(f"Solution of d²θ/dt² + {Omega}θ = 0 with θ(0) = {theta0} and θ'(0) = {theta_dot0}")
plt.grid()
plt.show()

# plot 2:
plt.plot(theta , theta_dot , color = 'red')
plt.xlabel("Position (θ)")
plt.ylabel("Angular velocity (dθ/dt)")
plt.title(f"Solution of d²θ/dt² + {Omega}θ = 0 with θ(0) = {theta0} and θ'(0) = {theta_dot0}")
plt.grid()
plt.show()
