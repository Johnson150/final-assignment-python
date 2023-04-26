class Doctor:
    def __init__(self, doctor_id, name, specialist, schedule, qualifications, room_number):
        self.doctor_id = doctor_id
        self.name = name
        self.specialist = specialist
        self.schedule = schedule
        self.qualifications = qualifications
        self.room_number = room_number

    def get_doctor_id(self):
        return self.doctor_id

    def set_doctor_id(self, doctor_id):
        self.doctor_id = doctor_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_specialist(self):
        return self.specialist

    def set_specialist(self, specialist):
        self.specialist = specialist

    def get_schedule(self):
        return self.schedule

    def set_schedule(self, schedule):
        self.schedule = schedule

    def get_qualifications(self):
        return self.qualifications

    def set_qualifications(self, qualifications):
        self.qualifications = qualifications

    def get_qualifications(self):
        return self.room_number

    def set_room_number(self, room_number):
        self.room_number = room_number

    def format_file_layout(self):
        return str(self.doctor_id) + "_" + str(self.name) + "_" + str(self.specialist) + "_" + str(self.schedule) + "_" + str(self.qualifications) + "_" + str(self.room_number)

    def __str__(self):
        return "{:<10} {:<20} {:<20} {:<10} {:<10}".format(str(self.doctor_id), str(self.name), str(self.specialist), str(self.schedule), str(self.qualifications), str(self.room_number))
