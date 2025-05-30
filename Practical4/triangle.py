# Goal: to print the values for the first ten triangles
# Procedure:
# 1. initialize the sum and the counter
# 2. use a loop to calculate the ten values and print them out

sum = 0 # initialize the sum
n = 1 # starting from the first triangle
while n <= 10: # we need to count first 10 triangles, so n should be no more than 10
    sum += n # sum can be calculated as the sum of the n numbers from 1 to n
    print(sum) # we need to show the first ten values
    n += 1 # n should move on
