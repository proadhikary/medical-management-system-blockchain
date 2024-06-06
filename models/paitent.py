class Patient:
    def __init__(self, patient_id, name, age, gender):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.medical_records = []

    def add_record(self, record):
        self.medical_records.append(record)

    def get_records(self):
        return self.medical_records
