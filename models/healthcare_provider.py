class HealthcareProvider:
    def __init__(self, provider_id, name):
        self.provider_id = provider_id
        self.name = name
        self.doctors = []
        self.patients = []

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def add_patient(self, patient):
        self.patients.append(patient)

    def get_records(self, patient_id):
        for patient in self.patients:
            if patient.patient_id == patient_id:
                return patient.get_records()
        return None
