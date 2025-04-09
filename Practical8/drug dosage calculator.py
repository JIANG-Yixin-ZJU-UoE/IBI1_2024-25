# goal: to calculate needed drug dosage according to the person
# procedure:
# 1. obtain the weight and strength
# 2. define a function called dosage with two parameters
# 3. tell if the weight is in range and the strength is 120 or 250
# 4. calculate the volume needed
# 5. if the weight or the strength do not meet the requirements, print out the error
# 6. use the function

weight = float(input('please enter your weight: '))
strength = float(input('please choose one strength from 120mg/5ml and 250mg/5ml: '))
def dosage(weight, strength):
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
    
print(dosage(weight, strength))
