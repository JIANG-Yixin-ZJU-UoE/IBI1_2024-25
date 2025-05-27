# goal: to look at the effect of the vaccination
# procedures:
# 1. import necessary libraries
# 2. set initial parameters
# 3. set the time loop to pick susceptible people at random to be infected, pick infected people at random to be recovered and record every loop of the infected
# 4. draw a figure depicting the graph


import numpy as np # import numpy
import matplotlib.pyplot as plt # import matplotlib.pyplot

plt.figure(figsize=(6, 4), dpi=150) # determine the dimensions and resolution

# set the initial parameters and set a loop to iterate all possible vaccination rates from 0% to 100%
for i in range(0,110,10):
    N = 10000
    vacc_rate = i/100
    V = int(N*vacc_rate)
    I = 1
    R = V
    S = max(N - V - I, 0)
    beta = 0.3
    gamma = 0.05
    I_list = [I]


    time = 0
    while time < 1000: # loop 1000 times    
        L1 = np.random.choice(range(0,2), S, p=[1-beta*I/N, beta*I/N]) # pick susceptible people at random to be infected
        new_I = sum(L1) # calculate the number of people infected
        S = max(S - new_I, 0)  # to record the S value and ensure it is bigger than 0
        L2 = np.random.choice(range(0,2), I, p=[1-gamma, gamma]) # pick infected people at random to be recovered
        new_R = sum(L2) # calculate the number of people recovered
        I = min( (I + new_I - new_R),10000) # to record I value and ensure it is smaller than 10000
        R = R + new_R # renew the R value
        I_list.append(I) # store the I value into the list
        time += 1 # plus one to enter another loop


    plt.plot(I_list, label=f'{i}%') # set the label/legend for the plot
   

plt.xlabel('Time') # set the x label
plt.xticks(range(0,1200,200), ('0', '200', '400', '600', '800', '1000')) # set the x ticks from 0 to 1000
plt.ylabel('Number of People') # set the y label
plt.title('Basic SIR Model Simulation with different vaccination rates') # set the title of the graph
plt.legend(loc='upper right') # set the legend
plt.show() # show the graph


    
