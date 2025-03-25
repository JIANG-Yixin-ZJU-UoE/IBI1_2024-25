# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

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

# time loop:
# 1. pick susceptible people at random to be infected
# 2. pick infected people at random to be recovered
# 3. record every loop in the according list
time = 0
while time <= 1000:
    L1 = np.random.choice(range(0,2), S, p=[1-beta*I/N, beta*I/N])
    new_I = sum(L1)
    L2 = np.random.choice(range(0,2), I, p=[1-gamma, gamma])
    new_R = sum(L2)
    S = S - new_I
    I = I + new_I - new_R
    R = R + new_R
    S_list.append(S)
    I_list.append(I)
    R_list.append(R)
    time += 1

# draw a figure depicting the graph
# 1. plot the three curves S,I,R, using different colors
# 2. set x/y axis parameters
plt.figure(figsize=(6, 4), dpi=150)
plt.plot(S_list, label='Susceptible', color='blue')
plt.plot(I_list, label='Infected', color='red')
plt.plot(R_list, label='Recovered', color='green')
plt.xlabel('Time')
plt.xticks(range(0,1200,200), ('0', '200', '400', '600', '800', '1000'))
plt.ylabel('Number of People')
plt.title('Basic SIR Model Simulation')
plt.legend()
plt.show()
    
