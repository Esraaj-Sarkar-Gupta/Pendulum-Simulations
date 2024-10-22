print("Simulating a double pendulum...")

import numpy as np
from scipy.integrate import odeint
import time as tm
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import os

print("- Imports complete")

def sys(state,t,m1,m2,l1,l2,g): # Defining the system mathematically (I messed this part up so many times :c )
    theta1 , theta2 , theta1_dot, theta2_dot = state
    theta1_ddot = (
    -g * (2*m1 + m2) * np.sin(theta1)
    - m2 * g * np.sin(theta1 - 2*theta2)
    - 2 * np.sin(theta1 - theta2) * m2 * (
        l2 * (theta2_dot**2) + l1 * (theta1_dot**2) * np.cos(theta1 - theta2)
    )
    ) / (l1 * (2*m1 + m2 - m2 * np.cos(2*theta1 - 2*theta2)))

    theta2_ddot = (
    2 * np.sin(theta1 - theta2) * (
        l1 * (theta1_dot**2) * (m1 + m2)
        + g * (m1 + m2) * np.cos(theta1)
        + (theta2_dot**2) * l2 * m2 * np.cos(theta1 - theta2)
    )
    ) / (l2 * (2*m1 + m2 - m2 * np.cos(2*theta1 - 2*theta2)))
    return np.array([theta1_dot , theta2_dot , theta1_ddot , theta2_ddot])

print("- System function defined")

# Initial states:
theta1_0 = 0
theta1_dot_0 = 0
theta2_0 = np.pi * 0.5
theta2_dot_0 = 0

state0 = np.array([theta1_0, theta1_dot_0, theta2_0, theta2_dot_0]) # Defining initial state vector
print("> Initial states defined")

# System praramters:
m1 = 10
m2 = 5
l1 = 4
l2 = 10
g = 9.81

T = 20 # Max time (seconds)
P = T * 30 # Number of data points (30 FPS)

t = np.linspace(0 , T , P) # Fefining time instances 
print("> System parameters defined")

s_time = tm.time() # Timing solving process
sol = odeint(sys , state0 , t , args=(m1,m2,l1,l2,g))
e_time = tm.time()

print(f"> Finished solving ODE for {T} simulated seconds, {P} data points in {e_time - s_time :.3f} real time seconds")

theta1 = sol[: , 0] # pulling solutions from 
theta2 = sol[: , 1]

plt.figure()
plt.plot(t, theta1 , color = 'lime' , label = 'θ₁')
plt.plot(t, theta2 , color = 'red' , label = 'θ₂')
plt.xlabel('Time (s)')
plt.ylabel('Angle (radians)')
plt.title('System Angles')
plt.legend()
plt.grid(True)
plt.show()
print("> Angles plotted against time")

plt.figure()
plt.plot(theta1 , sol[: , 2] , color = 'lime' , label = 'θ₁')
plt.plot(theta2 , sol[: , 3] , color = 'red' , label = 'θ₂')
plt.title('Angular Velocities Plotted Against Their Angles')
plt.xlabel('Angle (radians)')
plt.ylabel('Angular Velocities')
plt.legend()
plt.show()
print('> Angular velocities plotted against angles')

tm.sleep(2) # time to let program display plots

print("> Simulating physical system")
# Simulating physical system:
    
# Defining required coordinate lists:
X1 = []
Y1 = []
X2 = []
Y2 = []

dirc = str(input("Enter the name of the direction to save frames to: "))
try:
    os.mkdir(dirc)
    print("> Directory created")
except:
    print("> Directory already exsists")

print("- Iterating through angle values...")
for i in range(len(t)):
    X1.append(l1 * np.sin(theta1[i]))
    Y1.append(l1 *  (-1) * np.cos(theta1[i]) )
    X2.append(X1[i] + l2 * np.sin(theta2[i]))
    Y2.append(Y1[i] + l2* (-1) * np.cos(theta2[i]))
print("- Angle values listed")
print("- Generating path image...")

plt.figure()
plt.scatter(0 , 0 , color = 'grey')
plt.plot(X1 , Y1 , color = 'cyan' , linewidth = 2)
plt.plot(X2 , Y2 , color = 'purple' , linewidth = 2)
plt.title("Paths followed by masses over time")
plt.xlabel('X Space')
plt.ylabel("Y Space")
plt.grid(True)

print("- Plotting frames...")

s_time_2 = tm.time() # Timing plotting process
for I in range(len(t)):
    plt.figure()
    plt.scatter(0 , 0 , s = 20 , color = 'grey') # fixed pivot at origin

    # Get current coordinates from the coordinate lists.
    x1 = X1[I] 
    y1 = Y1[I]
    x2 = X2[I]
    y2 = Y2[I]
    
    plt.scatter(x1 , y1 , s = 80 , color = 'green') # Plotting position of ball 1
    plt.scatter(x2 , y2 , s = 80 , color = 'red') # Plotting position of ball 2
    
    l1x = [0 , x1]
    l1y = [0 , y1]
    l2x = [x1 , x2]
    l2y = [y1, y2]
    
    plt.plot(l1x , l1y  , linewidth = 0.5) # Graphing string 1
    plt.plot(l2x , l2y , linewidth = 0.5) # Graphing string 2
    
    plt.plot(X2[:I] , Y2[:I] , color ='purple') # Plotting the path covered by the second mass 
    
    plt.xlim(-10 , 10)
    plt.ylim(-15 , 5)
    
    plt.savefig(f"{dirc}/Frame_{I}")
    plt.close()
e_time_2 = tm.time()
print(f"> All {P} frames printed and saved to folder in {e_time_2 - s_time_2 :.3f} seconds.")
print("> End")

