# goal: to create a class called patients to store people information
# 1. create the class
# 2. use init to initialize data attributes
# 3. use a function to print out the patient's information
# 4. make an example to use the class


class patients:
    def __init__(self, name, age, date_of_latest_admission, mediacal_history): # initialize data attributes
        self.name = name
        self.age = age
        self.date_of_latest_admission = date_of_latest_admission
        self.mediacal_history = mediacal_history
    def record(name, age, date_of_latest_admission, mediacal_history): # print out the patient's information
        patients_record = f"{name}, {age}, {date_of_latest_admission}, {mediacal_history}"
        return patients_record
    
# this is an example of using the class and the function to print out patients' information
print(patients.record("kate", "32", "2024.11.23", "none"))