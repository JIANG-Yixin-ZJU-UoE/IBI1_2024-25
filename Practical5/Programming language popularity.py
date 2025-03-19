# Program: to explore the popularity of different programming languages
# Procedures:
# 1.to create a dictionary to store programming language popularity
# 2.print percentages of users of all programming languages that can be modified (after which make some changes)
# 3.draw a bar graph using numpy and matplotlib.pyplot

code_info = {"Javascript": 62.3, "HTML": 52.9, "Python": 51, "SQL": 51, "TypeScript": 38.5} # create a dictionary to store programming language popularity
print(code_info) # print the dictionary

for i in code_info.values(): # iterating all values in the dictionary
    print(i) # print them out

print(code_info["HTML"]) # print a percentage of users of one particular programming language that can be modified

code_info1 = code_info # create a new dictionary called code_info1 that is the same as code_info
code_info1["Python"] = 80 # alter the value of the key "Python"
print(code_info1) # print the new dictionary

import numpy as np # import numpy and name it np
import matplotlib.pyplot as plt # import matplotlib.pyplot and name it plt
N = 5 # create 5 groups, which is in accordance with 5 programming language types
percentage_of_users = (62.3, 52.9, 51, 51, 38.5) # store the y-axis value
ind = np.arange(N) # the x locations for the groups 
width = 0.3 # the width of the bars
p1 = plt.bar(ind, percentage_of_users, width) # create a bar chart using the "bar" function in matplotlib.pyplot
plt.ylabel("percentage of users") # define the name of the y-axis
plt.title("percentage of users who use the top 5 programming languages globally") # define the name of the bar chart
plt.xticks(ind,("Javascript", "HTML", "Python", "SQL", "TypeScript")) # define the x-axis label
plt.yticks(np.arange(0, 70, 10)) # define the y-axis scale, ranging from 0 to 70, using 10 as a scale unit
plt.show() # show the bar chart
 


