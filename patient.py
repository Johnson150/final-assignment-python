class Patient:
    def __init__(self, patient_id, name, diagnosis, gender, age):
        self.patient_id = patient_id
        self.name = name
        self.diagnosis = diagnosis
        self.gender = gender
        self.age = age

    def get_patient_id(self):
        return self.patient_id

    def set_patient_id(self, patient_id):
        self.patient_id = patient_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_diagnosis(self):
        return self.diagnosis

    def set_diagnosis(self, diagnosis):
        self.diagnosis = diagnosis

    def get_gender(self):
        return self.gender

    def set_gender(self, gender):
        self.gender = gender

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def format_file_layout(self):
        return str(self.patient_id) + "_" + str(self.name) + "_" + str(self.diagnosis) + "_" + str(self.gender) + "_" + str(self.age)

    def __str__(self):
        return "{:<10} {:<20} {:<20} {:<10}".format(str(self.patient_id), str(self.name), str(self.diagnosis), str(self.gender), str(self.age))
