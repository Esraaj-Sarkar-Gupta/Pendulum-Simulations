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
theta0 = np.pi/6  #amplitude if theta_dot0 = 0
theta_dot0 = 0  # Initial angular velocity
v0 = [theta0, theta_dot0]

g = 9.81
l = 6.9377

Omega = g/l # value of ω^2
FPS = 60 # set frames per second
sim_time = 30 # total simulated 

mass = 2

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
    ex.append(l*np.cos(i - np.pi/2))
    why.append(l*np.sin(i - np.pi/2))
xe = [-5 , 5]
yhw = [0 , 0]

radius = 1

# graphing results:
def graph(n , m): # plotting a graph for every frame n 
    a = l*np.cos(n - np.pi/2) # x coordinate 
    b = l*np.sin(n - np.pi/2) # y coordinate 
    
    PE = mass*g*(l+b) # potential energy of system
    KE = 0.5*mass*(theta_dot[m]*l)**2  # kinetic enegry of system 
    TE = KE + PE # total energy of system 
    
    
    
    center = (a , b) # CG of pendulum
    theta_deg = theta[m]*180/np.pi # value of theta in degrees
    
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
    
    plt.xlim(-8 , 8) # static limits
    plt.ylim(-8 , 0.5)
    plt.xlabel(f"θ = {theta_deg:.3f}° \n System Energy: \n Kinetic Enegery = {KE:.4f} \n Potential Enegery = {PE:.4f} \n Total Enegery = {TE:.4f}")
    plt.title(f"Simulation of a pendulum  d²θ/dt² + {Omega:.3f}sin(θ) = 0 with initial conditions θ(0) = {theta0:.3f} and θ'(0) = {theta_dot0} \n X - Y Space: ")
    plt.grid()
    plt.show()
 
st_2 = tm.time()
for n in range(len(theta)): # make graph for every value of theta 
    graph(theta[n] , n)
et_2 = tm.time()

delta_t2 = et_2 - st_2 

print(f"> All {sim_time*FPS} graphs (frames) have been generated.")
print(f"> Real time taken to generate {sim_time} seconds of simulated time is {delta_t2:.4f} seconds. Ratio = {delta_t2 / sim_time}, the real time taken to generate 1 second of simulated time.")
