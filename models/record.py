class MedicalRecord:
    def __init__(self, record_id, data_hash, timestamp, patient_id, doctor_id):
        self.record_id = record_id
        self.data_hash = data_hash
        self.timestamp = timestamp
        self.patient_id = patient_id
        self.doctor_id = doctor_id

    def add_record(self):
        # Logic to add the record
        pass

    def validate_record(self):
        # Logic to validate the record
        pass
