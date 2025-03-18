# store and show the population in UK countries and Zhejiang-neighboring provinces
# 1.create two lists to store infomation about the population and sort them
# 2.draw a pie chart for population in uk
# 3.draw a pie chart for population in provinces in China

uk_countries_population = [57.11, 3.13, 1.91, 5.45] # store population infomation in uk
china_countries_population = [65.77, 41.88, 45.28, 61.27, 85.15] # store population infomation in Zhejiang-neighboring
print(sorted(uk_countries_population))
print(sorted(china_countries_population))



import matplotlib.pyplot as plt
plt.figure()
labels = "England", "Wales", "Northern Ireland", "Scotland"
sizes = [57.11, 3.13, 1.91, 5.45]
explode = (0.2,0,0,0)
plt.pie(sizes, explode = explode, labels = labels, autopct = "%.1f%%", shadow = True, startangle = 0)
plt.title("population in countries in uk")
plt.axis("equal")


plt.figure()
labels = "Zhejiang", "Fujian", "Jiangxi", "Anhui", "Jiangsu"
sizes = [65.77, 41.88, 45.28, 61.27, 85.15]
explode = (0,0,0,0,0)
plt.pie(sizes, explode = explode, labels = labels, autopct = "%.1f%%", shadow = True, startangle = 90)
plt.title("population in Zhejiang-neighboring provinces in China")
plt.axis("equal")

plt.show()