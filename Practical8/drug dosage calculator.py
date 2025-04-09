# goal: to calculate needed drug dosage according to the person
# procedure:
# 1. obtain the weight and strength
# 2. define a function called dosage with two parameters
# 3. tell if the weight is in range and the strength is 120 or 250
# 4. calculate the volume needed
# 5. if the weight or the strength do not meet the requirements, print out the error
# 6. use the function

def dosage(weight, strength):

    """ tell if the weight is in range and the strength is 120 or 250
        calculate the volume needed
        if the weight or the strength do not meet the requirements, print out the error """
    
    if weight >= 10 and weight <= 100:
        if strength == 120 or strength == 250:
            recommend = 15
            total = recommend * weight
            volume = total / strength * 5
            return volume
        else:
            ValueError1 = "error: strength does not match"
            return ValueError1
    else:
        ValueError2 = "error: the weight out of range"
        return ValueError2
    
# this is where an example is given to call the function
print(dosage(weight = 20, strength = 120))  
