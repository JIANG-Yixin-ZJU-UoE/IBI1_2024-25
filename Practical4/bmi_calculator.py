# Goal: to calculate the BMI values for the input height and weight
# Procedure:
# 1. display the formula and calculate the BMI
# 2. judge which category the input is in

height = 1.63  # stating the person's height 
weight = 55  # stating the person's weight
BMI = weight/height**2  # using the formula to calculate the person's BMI
print("the person's BMI is:", BMI)  # show the person's BMI
if BMI > 30:  # compare the person's BMI with 30
    print("the person is obese")  # if the BMI > 30, the person is obese
elif BMI < 18.5:  # compare the person's BMI with 18.5
    print("the person is underweight") # if the BMI < 18.5, the person is underweight
else:  # the person's BMI is neither over 30 nor less than 18.5
    print("the person is in the normal weight")  # show that the person is in the normal weight
