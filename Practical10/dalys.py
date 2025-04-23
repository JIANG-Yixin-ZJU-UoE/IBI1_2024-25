# Goals: to analyze a public health dataset (csv. file) in Python
# Procedures/Tasks:
# 1. import the libraries and the file
# 2. print out the first ten rows of the column "Year"
# 3. show all the DALYs in 1990
# 4. compare the mean DALYs of the UK and the France
# 5. use a graph to show how DALYs changes over the years in the UK
# 6. draw a a boxplot of DALYs across countries in 1990

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("C:/Users/22365/Desktop/Hainingmaterials/IBI/IBI1_PARCTICAL/IBI1_2024-25/Practical10")

dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv") # import the .csv file 

# showing the third column (the year) for the first 10 rows (inclusive)
column = [False, False, True, False]
print(dalys_data.iloc[0:10, column]) # the 10th year of the recording is 1999

# used a Boolean to show DALYs for all countries in 1990
year_Boolean_1990 = []
for i in dalys_data.loc[:, "Year"]:
    if i == 1990:
        flag = True
        year_Boolean_1990.append(flag)
    else:
        flag = False
        year_Boolean_1990.append(flag)

row = dalys_data.loc[year_Boolean_1990, "Year"]
print(dalys_data.loc[row.index, ["Entity", "Code", "Year", "DALYs"]])

# compute the mean DALYs in the UK and France, it turn out that the mean DALYs in the UK was greater than France
print(dalys_data.loc[dalys_data.Entity == "United Kingdom", "DALYs"].describe()["mean"])
print(dalys_data.loc[dalys_data.Entity == "France", "DALYs"].describe()["mean"])

# create a graph showing the DALYS changes over time in the UK
uk = dalys_data.loc[dalys_data.Entity == "United Kingdom", ["DALYs", "Year"]]
plt.figure(figsize = (8, 6))
plt.title("the DALYS changes over time in the UK")
plt.plot(uk.Year, uk.DALYs, 'b+')
plt.xticks(uk.Year, rotation = -90)
plt.xlabel("Years")
plt.ylabel("DALYs in the UK")
plt.show()

# draw a a boxplot of DALYs across countries in 1990 (answer the question stated in file question.txt)
DALYs_1990 = dalys_data.loc[dalys_data["Year"] == 1990, "DALYs"]
data_list = DALYs_1990.tolist()
n = 228
plt.title("DALYs across countries in 1990")
plt.xlabel("228 countries in 1990")
plt.ylabel("DALYs across countries")
plt.boxplot(data_list,
            vert = True, 
            whis = 1.5, 
            patch_artist = True, 
            meanline = True, 
            showbox = True, 
            showcaps = True,
            showfliers = True, 
            notch = False)
plt.show()