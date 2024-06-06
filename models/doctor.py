class Doctor:
    def __init__(self, doctor_id, name, specialty):
        self.doctor_id = doctor_id
        self.name = name
        self.specialty = specialty
        self.patients = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def get_patient_records(self, patient_id):
        for patient in self.patients:
            if patient.patient_id == patient_id:
                return patient.get_records()
        return None
