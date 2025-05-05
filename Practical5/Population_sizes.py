# store and show the population in UK countries and Zhejiang-neighboring provinces
# Procedures:
# 1.create two lists to store information about the population and sort them
# 2.draw a pie chart for population in the UK
# 3.draw a pie chart for population in provinces in China

uk_popu = [57.11, 3.13, 1.91, 5.45] # store population information in the UK
china_popu = [65.77, 41.88, 45.28, 61.27, 85.15] # store population information in Zhejiang-neighboring provinces
print(sorted(uk_popu)) # print sorted list of population in the UK
print(sorted(china_popu)) # print sorted list of population in Zhejiang-neighboring provinces

uk_countries_population = {"England": 57.11, "Wales": 3.13, "Norhtern Ireland": 1.91, "Scotland": 5.45} # store population information in the UK as dictionary
china_countries_population = {"Zhejiang": 65.77, "Fujian": 41.88, "Jiangxi": 45.28, "Anhui": 61.27, "Jiangsu": 85.15} # store population information in Zhejiang-neighboring provinces as dictionary

import matplotlib.pyplot as plt # import matplotlib.pyplot and name it plt
plt.figure(figsize = (12,5)) # show two pictures at the same time

plt.subplot(1,2,1) # create a subplot with 1 row and 2 columns, and draw this plot in the first column
labels = uk_countries_population.keys() # store the countries in the UK
sizes = uk_countries_population.values() # store the populations in countries in the UK
explode = (0.2,0,0,0) # specifies the fraction of the radius with which to offset each wedge (the population in England offsets 0.2 times of the radius)
plt.pie(sizes, explode = explode, labels = labels, autopct = "%.1f%%", shadow = True, startangle = 0) # draw the pie chart, with sizes/labels/explode as above, and the percentage is shown in fraction with one decimal place. Show the shadow and draw from the 0 angle
plt.title("population in countries in uk") # create a title called "population in countries in the UK"
plt.axis("equal") # ensure the pie chart is a perfect circle

plt.subplot(1,2,2) # create a subplot with 1 row and 2 columns, and draw this plot in the second column
labels = china_countries_population.keys() # store Zhejiang-neighboring provinces
sizes = china_countries_population.values() # store the populations in countries in Zhejiang-neighboring provinces
explode = (0,0,0,0,0) # # specifies the fraction of the radius with which to offset each wedge (no place is offset in this graph)
plt.pie(sizes, explode = explode, labels = labels, autopct = "%.1f%%", shadow = True, startangle = 90) # # draw the pie chart, with sizes/labels/explode as above, and the percentage is shown in fraction with one decimal place. Show the shadow and draw from the 90 angle
plt.title("population in Zhejiang-neighboring provinces in China") # create a title called "population in Zhejiang-neighboring provinces in China"
plt.axis("equal") # ensure the pie chart is a perfect circle

plt.show() # show the pie chart