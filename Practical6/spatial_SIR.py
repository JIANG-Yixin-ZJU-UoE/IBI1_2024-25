# goal: Looking at disease spread in 2D
# procedures:
# 1. import necessary libraries
# 2. choose a random point in an array
# 3. deal with how to infect neighbors
# 4. deal with the recovery
# 5. plot four heat diagrams

import numpy as np # import numpy
import matplotlib. pyplot as plt # import matplotlib.pyplot
import random # import random

# make array of all susceptible population
population = np.zeros((100, 100)) # make a 100*100 matrix with all zeros
outbreak = np.random.choice(range(100), 2) # randomly choose two elements (the x and y coordinates)
population[outbreak[0], outbreak[1]] = 1 # define the infected coordinates

# set the initial parameters
I = 1
beta = 0.3
gamma = 0.05

# infect the neighbors and simulate the process of one person infecting others at a time
def step(population):
    infected = [] # store the infected information
    copy = population.copy() # copy the population to make the change, or the newly infected people will affect others in one step
    for i in range(100):
        for j in range(100): # iterate all members in the matrix
            if population[i, j] == 1: # find the infected
                # check the 8 neighbors
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]: # iterate the neighbors
                        if 0 <= i+di < 100 and 0 <= j+dj < 100: # make sure the coordinates are in the matrix
                            if population[i+di, j+dj] == 0: # find the neighbors that are not infected
                                if random.random() < beta: 
                                    copy[i+di, j+dj] = 1 # the neighbor has beta percent of being infected

                infected.append([i, j]) # add infected coordinates
    # iterate the infected to make possible reocvery
    for i, j in infected:
        if np.random.random() < gamma:
            copy[i, j] = 2 # the infected have gamma percent of recovery
    
    return copy

fig = plt.figure(figsize= (6, 4), dpi= 150) # determine the dimensions and resolution
ax = fig.add_subplot(221) # draw a subplot in the first place of a whole plot
ax2 = fig.add_subplot(222) # draw a subplot in the second place of a whole plot
ax3 = fig.add_subplot(223) # draw a subplot in the third place of a whole plot
ax4 = fig.add_subplot(224) # draw a subplot in the forth place of a whole plot


ax.imshow(population, cmap= 'viridis', interpolation= 'nearest') # draw the initial plot with one randomly choosed point
for i in range(10): 
    population = step(population) # use the step function 10 times  
ax2.imshow(population, cmap= 'viridis', interpolation= 'nearest') # draw the plot
for i in range(40):
    population = step(population) # use the function another 40 times 
ax3.imshow(population, cmap= 'viridis', interpolation= 'nearest') # draw the plot
for i in range(50):
    population = step(population) # use the function another 50 times
ax4.imshow(population, cmap= 'viridis', interpolation= 'nearest') # draw the plot

for ax in [ax, ax2, ax3, ax4]:
    ax.set_xticks(range(0, 100, 20), ("0", "20", "40", "60", "80")) # set the x ticks from 0 to 80
    ax.set_yticks(range(80 ,-20, -20), ('80', '60', '40', '20', '0')) # set the y ticks from 80 to 0
    ax.plot(population = 0, color = "purple") # make the susceptible points purple
    ax.plot(population = 1, color = "green") # make the infected points green
    ax.plot(population = 2, color = "yellow") # make the recovered points yellow

plt.show() # show the plot
