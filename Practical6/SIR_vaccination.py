# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(6, 4), dpi=150)

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

    # time loop:
    # 1. pick susceptible people at random to be infected
    # 2. pick infected people at random to be recovered
    # 3. record every loop in the according list
    time = 0
    while time <= 1000:
                 
        L1 = np.random.choice(range(0,2), S, p=[1-beta*I/N, beta*I/N])
        new_I = sum(L1)
        S = max(S - new_I, 0)  
        L2 = np.random.choice(range(0,2), I, p=[1-gamma, gamma])
        new_R = sum(L2)
        I = min( (I + new_I - new_R),10000)
        R = R + new_R 
        I_list.append(I)
        time += 1

# draw a figure depicting the graph
# 1. plot the three curves S,I,R, using different colors
# 2. set x/y axis parameters
    plt.plot(I_list, label=f'Vaccination {i}%')
   

plt.xlabel('Time')
plt.xticks(range(0,1200,200), ('0', '200', '400', '600', '800', '1000'))
plt.ylabel('Number of People')
plt.title('Basic SIR Model Simulation with different vaccination rate')
plt.legend(loc='upper right')
plt.show()


    
