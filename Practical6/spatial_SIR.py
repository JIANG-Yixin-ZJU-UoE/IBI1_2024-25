# goal: Looking at disease spread in 2D
# procedures:
# 1. import necessary libraries
# 2. choose a random point in an array
# 3. deal with how to infect neighbors
# 4. deal with the recovery
# 5. plot four heat diagrams


# import necessary libraries
import numpy as np
import matplotlib. pyplot as plt
import random

# make array of all susceptible population
population = np.zeros((100, 100))
outbreak = np.random.choice(range(100), 2)
population[outbreak[0], outbreak[1]] = 1


timesteps = 100
I = 1
beta = 0.3
gamma = 0.05

# check the neighbers' infection(spread of the disease)
for i in range(100):
    for j in range(100):
        if population[i, j] == 1:
            # check the 8 neighbors
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    if 0 <= i+di < 100 and 0 <= j+dj < 100:
                        if population[i+di, j+dj] == 0:
                            if random.random() < beta:
                                population[i+di, j+dj] = 1

# recovery
infected = []
for people in population:
    if population[i, j] == 1:       
        infected.append([i, j])
        for di, dj in infected:
            if np.random.random() < gamma:
                population[i, j] = 2

for i in [0, 10, 50, 100]:
    plt.figure(figsize = (6, 4), dpi =150)
    plt.imshow(population, cmap= 'viridis', interpolation= 'nearest')
    plt.plot(population = 0, color = "purple")
    plt.plot(population = 1, color = "green")
    plt.plot(population = 2, color = "yellow")
    plt.show()