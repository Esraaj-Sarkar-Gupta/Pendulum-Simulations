print("Simulating a single pendulum...")

import numpy as np
from scipy.integrate import odeint
import time as tm
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# computing motion of pendulum:
def system(v, t, Omega):  # defining the eqation of motion where ω^2 = Ω
  theta, theta_dot = v # Unpack state vector
  d_theta_dot_dt = -Omega * np.sin(theta)  # Derivative of theta
  d_theta_dt = theta_dot
  return [d_theta_dt, d_theta_dot_dt]  # Return derivatives as a list

# Initial states:
theta0 = np.pi/2  #amplitude if theta_dot0 = 0
theta_dot0 = 0  # Initial angular velocity
v0 = [theta0, theta_dot0]

Omega = 2 # value of ω^2
FPS = 40 # set frames per second
sim_time = 30 # total simulated 

t = np.linspace(0, sim_time , sim_time*FPS )

st_1 = tm.time()
sol = odeint(system, v0, t, args=(Omega,))
et_1 = tm.time()
print(f"> Non-linear second order differential equation solved in {et_1 - st_1:.4f} seconds.")

theta = sol[:, 0]
theta_dot = sol[:, 1]

# tracing path in cartesian coordinates:
ex = []  # x coordinates
why = [] # y coordinates
for i in theta:
    ex.append(np.cos(i - np.pi/2))
    why.append(np.sin(i - np.pi/2))
xe = [-0.4 , 0.4]
yhw = [0 , 0]
radius = 0.2

# graphing results:
def graph(n): # plotting a graph for every frame n 
    a = np.cos(n - np.pi/2) # x coordinate 
    b = np.sin(n - np.pi/2) # y coordinate 
    
    center = (a , b)
    
    circle = Circle(xy=center, radius=radius)
    fig, ax = plt.subplots() # the pendulum with  its CG at its center
    
    plt.plot(a , b , color = 'green')
    ax.add_patch(circle)
    ax.set_aspect("equal")
    
    x = [0 , a]
    y = [0 , b]
    plt.plot(x , y , color = 'green') # line that joins origin to CG of pendulum (string)
    plt.plot(ex , why , color = 'grey') # plotting path to be traced
    plt.plot(xe , yhw , color = 'purple') #so that the string isn't hanging from nothing
    
    plt.xlim(-1.5 , 1.5) # static limits
    plt.ylim(-1.5 , 0.5) 
    plt.title(f"Simulation of a pendulum  d²θ/dt² + {Omega}sin(θ) = 0 with initial conditions θ(0) = {theta0:.4f} and θ'(0) = {theta_dot0}")
    plt.grid()
    plt.show()
 
st_2 = tm.time()
for n in theta: # make graph for every value of theta 
    graph(n)
et_2 = tm.time()

delta_t2 = et_2 - st_2 

print(f"> All {sim_time*FPS} graphs (frames) have been generated.")
print(f"> Real time taken to generate {sim_time} seconds of simulated time is {delta_t2:.4f} seconds. Ratio = {delta_t2 / sim_time}, the real time taken to generate 1 second of simulated time.")
    

    
    
    

