# goal: to create a class called patients to store people information
# 1. create the class
# 2. use init to initialize data attributes
# 3. use a function to print out the patient's information
# 4. make an example to use the class


class Patients:
    def __init__(self, name, age, date_of_latest_admission, medical_history): # initialize data attributes
        self.name = name
        self.age = age
        self.date_of_latest_admission = date_of_latest_admission
        self.medical_history = medical_history
    
    def record(self): # print out the patient's information
        patients_record = f"Name: {self.name}, Age: {self.age}, Date of latest admission: {self.date_of_latest_admission}, Medical history: {self.medical_history}"
        return patients_record
    
# this is an example of using the class and the function to print out patients' information
patient = Patients(name = "Kate", age = "32", date_of_latest_admission = "2024.11.23", medical_history = "none")
print(patient.record())
