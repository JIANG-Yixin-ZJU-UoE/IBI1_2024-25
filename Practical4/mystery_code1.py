# What does this piece of code do?
# Answer: count how many times the computer tries to produce two same values

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

progress=0  # initialize progress, which means times used to produce two same numbers.
while progress>=0:  # enter cycle 
	progress+=1  # count times used
	first_n = randint(1,6)  # produce the first number
	second_n = randint(1,6)  # produce the second number
	if first_n == second_n:  # check is the first number is equal to the second number 
		print(progress)  # show our times used
		break  # go out of the cycle

