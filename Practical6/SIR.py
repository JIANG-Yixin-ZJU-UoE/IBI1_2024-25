# goal: to make a simple SIR model
# procedures:
# 1. import necessary libraries
# 2. set initial parameters
# 3. use the time loop to pick susceptible people at random to be infected, pick infected people at random to be recovered and record every loop in the according list
# 4. draw a figure depicting the graph

import numpy as np # import numpy
import matplotlib.pyplot as plt # import matplotlib.pyplot

# set the number of S, I, R, N, beta, gamma and needed lists
S = 9999
I = 1
R = 0
SIR_array = np.array([S, I, R])
N = S + I + R
beta = 0.3
gamma = 0.05
S_list = [S]
I_list = [I]
R_list = [R]

time = 0
while time < 1000: # loop 1000 times
    L1 = np.random.choice(range(0,2), S, p=[1-beta*I/N, beta*I/N]) # pick susceptible people at random to be infected
    new_I = sum(L1) # calculate the number of people infected
    L2 = np.random.choice(range(0,2), I, p=[1-gamma, gamma]) # pick infected people at random to be recovered
    new_R = sum(L2) # calculate the number of people recovered
    # renew the new S, I, R
    S = S - new_I # minus the new infected
    I = I + new_I - new_R # plus new infected and minus new recovered
    R = R + new_R # plus the new recovered
    # store the number into the list created
    S_list.append(S)
    I_list.append(I)
    R_list.append(R)
    time += 1 # plus one to enter another loop


# plot the three curves S,I,R
plt.figure(figsize=(6, 4), dpi=150) # determine the dimensions and resolution
plt.plot(S_list, label="Susceptible", color='blue') # plot the S curve with color blue
plt.plot(I_list, label="Infected", color='red') # plot the I curve with color red
plt.plot(R_list, label="Recovered", color='green') # plot the R curve with color green
plt.xlabel('Time') # set the x label
plt.xticks(range(0, 1200, 200), ('0', '200', '400', '600', '800', '1000')) # set the x ticks from 0 to 1000
plt.ylabel('Number of People') # set the y label
plt.title('Basic SIR Model Simulation') # set the title of the graph
plt.legend(loc= "upper right") # set the legend
plt.show() # show the graph
plt.savefig('simple SIR image') # save the image

    
