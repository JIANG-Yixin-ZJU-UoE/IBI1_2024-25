# import necessary libraries
import numpy as np
import matplotlib. pyplot as plt

# make array of all susceptible population
population = np.zeros( ( 100 , 100 ) )
outbreak = np.random.choice( range(100) , 2 )
population[ outbreak[ 0 ] , outbreak[ 1 ] ] = 1
plt.figure( figsize = ( 6 , 4 ) , dpi =150)
plt.imshow( population , cmap= 'viridis', interpolation= 'nearest')

timesteps = 100
I = 1
beta = 0.3
gamma = 0.05


# define the color
color_mapping = {
    0: [0.18, 0.80, 0.44, 1], 
    1: [0.91, 0.30, 0.24, 1], 
    2: [0.20, 0.60, 0.86, 1]  
}
def generate_colors(grid):
    return np.array([[color_mapping[val] for val in row] for row in grid])

# draw the plot
img = plt.imshow(generate_colors(population))
plt.axis('off')
plt.title(f"SIR Spatial Spread - Step 0 (Initial Clusters: {I})")

# renew the loop
for step in range(timesteps):
    new_pop = population.copy()
    
    # recovery
    infected = np.argwhere(population == 1)
    for i, j in infected:
        if np.random.rand() < gamma:
            new_pop[i, j] = 2
    
    # check the neighbers' infection(spread of the disease)
    for i in range(100):
        for j in range(100):
            if population[i, j] == 1:
                # check the 8 neighbors
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        if 0 <= i+di < 100 and 0 <= j+dj < 100:
                            if new_pop[i+di, j+dj] == 0:
                                if np.random.rand() < beta:
                                    new_pop[i+di, j+dj] = 1
    
    population = new_pop.copy()
    img.set_data(generate_colors(population))
    plt.title(f"SIR Spatial Spread - Step {step+1}")
    plt.draw()
    plt.pause(0.2)
    
    if not plt.get_fignums():
        break

plt.show()
