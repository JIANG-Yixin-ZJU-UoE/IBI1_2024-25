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


def step(population):
    infected = []
    copy = population.copy()
    for i in range(100):
        for j in range(100):
            if population[i, j] == 1:
                # check the 8 neighbors
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        if 0 <= i+di < 100 and 0 <= j+dj < 100:
                            if population[i+di, j+dj] == 0:
                                if random.random() < beta:
                                    copy[i+di, j+dj] = 1

                # recovery
                #1记录所有的感染者2对感染者执行概率康复

                infected.append([i, j])
    for i, j in infected:
        if np.random.random() < gamma:
            copy[i, j] = 2
    
    return copy


fig = plt.figure(figsize = (6, 4), dpi =150)
ax = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)


ax.imshow(population, cmap= 'viridis', interpolation= 'nearest')
for i in range(10):
    population = step(population)
ax2.imshow(population, cmap= 'viridis', interpolation= 'nearest')
for i in range(40):
    population = step(population)
ax3.imshow(population, cmap= 'viridis', interpolation= 'nearest')
for i in range(50):
    population = step(population)
ax4.imshow(population, cmap= 'viridis', interpolation= 'nearest')

for ax in [ax, ax2, ax3, ax4]:
    ax.set_xticks(range(0, 100, 20), ("0", "20", "40", "60", "80"))
    ax.set_yticks(range(80 ,-20, -20), ('80', '60', '40', '20', '0'))
    ax.plot(population = 0, color = "purple")
    ax.plot(population = 1, color = "green")
    ax.plot(population = 2, color = "yellow")

plt.show()
