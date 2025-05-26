# Program: to explore the popularity of different programming languages
# Procedures:
# 1.to create a dictionary to store programming language popularity
# 2.print percentages of users of all programming languages that can be modified (after which make some changes)
# 3.draw a bar graph using numpy and matplotlib.pyplot

code_info = {"Javascript": 62.3, "HTML": 52.9, "Python": 51, "SQL": 51, "TypeScript": 38.5} # create a dictionary to store programming language popularity
print(code_info) # print the dictionary

input_variable = "Python" # use a variable to store the name of a programming language (e.g. Python)
if input_variable in code_info: # check if the input_variable is in the dictionary code_info
    print(f"The percentage of users of {input_variable} is {code_info[input_variable]}%") # print the percentage of users using the programming language
else:
    print(f"{input_variable} is not in the dictionary")

import numpy as np # import numpy and name it np
import matplotlib.pyplot as plt # import matplotlib.pyplot and name it plt
N = len(code_info) # create 5 groups, which is in accordance with 5 programming language types
percentage_of_users = (code_info.values()) # store the y-axis value
ind = np.arange(N) # the x locations for the groups 
width = 0.3 # the width of the bars
plt.bar(ind, percentage_of_users, width) # create a bar chart using the "bar" function in matplotlib.pyplot
plt.ylabel("percentage of users") # define the name of the y-axis
plt.title("percentage of users who use the top 5 programming languages globally") # define the name of the bar chart
plt.xticks(ind,code_info.keys()) # define the x-axis label
plt.yticks(np.arange(0, 110, 10)) # define the y-axis scale, ranging from 0 to 70, using 10 as a scale unit
plt.show() # show the bar chart




