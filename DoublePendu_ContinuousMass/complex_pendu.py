import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

import os
import time as tm

try: # Make directory to save the frames
    os.makedirs('./frames')
    print("Directory ./frames created")
except Exception as e:
    print(f"> Directory ./frames exists. Creation failure : {e}")
    
def mag(x): # Define magnitude function
    if x < 0:
        return (-x)
    else:
        return x

# Constants
rho = 1.74 # This value varies from mass 1 and mass 2, but we'll assume it doesn't
l1 = 0.245
l2 = 0.1778
m1 = 0.4263
m2 = 0.15486
g = 9.81

# The system of ODEs
def equations(t, y):
    theta1, omega1, theta2, omega2 = y
    
    # Coefficients
    A11 = (1/3) * rho * l1**3 + rho * l1**2 * l2
    A12 = (1/2) * l1 * l2**2 * rho
    A21 = (1/2) * l1 * l2**2 * rho
    A22 = (1/3) * l2**3 * rho

    # Right-hand side (gravitational forces)
    b1 = -g * l1 * np.sin(theta1) * (m1/2 + m2)
    b2 = -g * m2 * l2 * np.sin(theta2) / 2
    
    # Solve for angular accelerations (ddot_theta1, ddot_theta2)
    A = np.array([[A11, A12], [A21, A22]])
    b = np.array([b1, b2])
    
    ddot_theta = np.linalg.solve(A, b)
    
    return [omega1, ddot_theta[0], omega2, ddot_theta[1]]

# Initial conditions: [theta1, omega1, theta2, omega2]
y0 = [np.pi/2, 0 , 0, 0]  # initial angles and angular velocities

# Time span
t_span = (0, 50)
t_eval = np.linspace(*t_span, 1000)

# Solve the system of ODEs
start_time = tm.time()
solution = solve_ivp(equations, t_span, y0, t_eval=t_eval)
end_time = tm.time()
print(f"> System of equations solved in {end_time - start_time:.4f} seconds.")

# Plot the results
plt.figure(figsize=(10, 5))

plt.plot(solution.t, solution.y[0], label='theta1 (rad)' , color = 'green')
plt.plot(solution.t, solution.y[2], label='theta2 (rad)' , color = 'red')

plt.title('Double Pendulum Angles over Time')
plt.xlabel('Time (s)')
plt.ylabel('Angle (rad)')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize = (10, 5))

plt.plot(solution.y[0] , solution.y[1] , label = 'Mass 1' , color = 'green')
plt.plot(solution.y[2] , solution.y[3] , label = 'Mass 2' , color = 'red')

plt.title("Double Pendulum Phase Space")
plt.xlabel('Angle (rad)')
plt.ylabel('Angular velocity (rad/s)')
plt.legend()
plt.grid(True)
plt.show()

# Run Simulation

start_time_2 = tm.time()

coveredpoints = [[] , []]

for i in range(len(solution.t)):
    plt.figure(figsize=(10,10))
    plt.scatter(0 , 0 , color = 'black' , s = 50)
    theta1 = solution.y[0][i]
    theta2 = solution.y[2][i]
    
    plt.plot(np.array([0 , l1 * np.sin(theta1)]) , np.array([0 ,  - l1 * np.cos(theta1)]) , linewidth = 5 , color = 'green') # Continuous mass 1
    plt.plot(np.array([l1 * np.sin(theta1) , l1 * np.sin(theta1) + l2 * np.sin(theta2)]) , np.array([- l1 * np.cos(theta1) , - (l1 * np.cos(theta1) + l2 * np.cos(theta2))]) , linewidth = 5 , color = 'red') # Continuous mass 2
    
    plt.scatter(l1/2 * np.sin(theta1) , - l1/2 * np.cos(theta1) , color = 'blue') # Center of gravity of mass 1
    plt.scatter(l1 * np.sin(theta1) + l2/2 * np.sin(theta2) , -( l1 * np.cos(theta1) + l2/2 * np.cos(theta2)) , color = 'blue') # Center of gravity of mass 1
    
    coveredpoints[0].append(l1 * np.sin(theta1) + l2/2 * np.sin(theta2))
    coveredpoints[1].append(-( l1 * np.cos(theta1) + l2/2 * np.cos(theta2)))
    
    plt.plot(coveredpoints[0] , coveredpoints[1] , color = 'purple')

    
    d_limit = mag(l1) + mag(l2) + 0.5
    plt.xlim(-d_limit , d_limit)
    plt.ylim(-d_limit, d_limit)
    plt.grid(True)
    plt.savefig(f"./frames/frame_{i}.png")
    plt.close()

plt.figure(figsize = (10 , 10))
plt.scatter(0 , 0, color = 'red' , s = 50)
plt.plot(coveredpoints[0] , coveredpoints[1])
plt.title("System Path - Path covered by second mass")
plt.show()

end_time_2 = tm.time()

print(f"> Finished saving plots into directory in time {end_time_2 - start_time_2 :.4f} seconds.")