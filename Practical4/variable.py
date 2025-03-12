a = 15 # The walk to the bus stop is 15	mins
b = 75 # The bus journey takes 1 hr and	15 mins
c = a + b # c is the total length of time of the bus commute
d = 90 # the drive takes 1hr and 30 mins
e = 5 # the driver needs 5 mins to walk to the final destination
f = d + e # f is the total time of time of the car commute
if c > f: # compare c with e to find out the shortest way of commute 
    print(f"the car travel takes {f} mins,", "the car travel is faster") # if c > f, the car travel is faster.
elif c < f: # compare c with e to find out the shortest way of commute 
    print(f"the bus travel takes {c} mins,", "the bus travel is faster") # if c < f, the bus travel is faster.
else: # compare c with e to find out the shortest way of commute
    print("the two methods are the same") # if c = f, the two methods are the same.
# The bus ride is quiker and needs shorter time.

X = True # the value of X is True
Y = False # the value of Y is False
W = X and Y # the value of W is X and Y
print(W) # print the outcome of W. Because X is True and Y is False, W (X and Y) is False.
#    X     |     Y      |      W
#   True   |    True    |     True
#   True   |    False   |     False
#   False  |    True    |     False
#   False  |    False   |     False 