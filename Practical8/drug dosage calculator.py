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
