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


# 自定义颜色映射
color_mapping = {
    0: [0.18, 0.80, 0.44, 1],  # 绿色：易感者
    1: [0.91, 0.30, 0.24, 1],  # 红色：感染者
    2: [0.20, 0.60, 0.86, 1]   # 蓝色：康复者
}

# 将数字矩阵转换为颜色矩阵
def generate_colors(grid):
    return np.array([[color_mapping[val] for val in row] for row in grid])

# 初始绘图
img = plt.imshow(generate_colors(population))
plt.axis('off')
plt.title(f"SIR Spatial Spread - Step 0 (Initial Clusters: {I})")

# 动态更新循环
for step in range(timesteps):
    new_pop = population.copy()
    
    # 处理感染者康复
    infected = np.argwhere(population == 1)
    for i, j in infected:
        if np.random.rand() < gamma:
            new_pop[i, j] = 2
    
    # 传播感染（优化后的邻域检查）
    for i in range(100):
        for j in range(100):
            if population[i, j] == 1:
                # 检查周围8邻域
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        if 0 <= i+di < 100 and 0 <= j+dj < 100:
                            if new_pop[i+di, j+dj] == 0:
                                if np.random.rand() < beta:
                                    new_pop[i+di, j+dj] = 1
    
    # 更新数据和可视化
    population = new_pop.copy()
    img.set_data(generate_colors(population))
    plt.title(f"SIR Spatial Spread - Step {step+1}")
    plt.draw()
    plt.pause(0.2)  # 调整动画速度
    
    # 检查窗口是否关闭
    if not plt.get_fignums():
        break

plt.show()
