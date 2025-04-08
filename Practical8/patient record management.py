class patients:
    def __init__(self, name, age, date_of_latest_admission, mediacal_history):
        self.name = name
        self.age = age
        self.date_of_latest_admission = date_of_latest_admission
        self.mediacal_history = mediacal_history
    def record(name, age, date_of_latest_admission, mediacal_history):
        patients_record = f"{name}, {age}, {date_of_latest_admission}, {mediacal_history}"
        print(patients_record)
        return patients_record
    
print(patients.record("kate","32", "2024.11.23", "none"))