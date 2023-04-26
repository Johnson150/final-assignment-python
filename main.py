
# Johnson Giang 000886101 april 26th, 2023
# Danrel Lu 000882515 april 26th, 2023
# Chan Tsz Hei 000903980 april 26th, 2023

# This program is a database for ARH management.
# In this program the user will be able access doctor and patient information while moving through the menu directory.
# The menu directory will consist of matching doctor/patient by ID, displaying full patient/doctor list and edit existing information
# on top of that the user will be able to add new patients/doctors.
# updated information will over write existing patient.txt and doctor.txt files.
# Lastly, the program will also automatically print formatted statements in patient.txt and doctor.txt files


from doctor import Doctor
from patient import Patient


# General menu function for doctors and patient
def menu():
    print("ARH Management System")
    print("   Patient's Menu")
    print("1 - Doctor")
    print("2 - Patient")
    print("0 - Close Application")
    while True:
        menu_choice = input("Enter option: ")
        if menu_choice == "1":
            manage_dr()
            return menu_choice
        elif menu_choice == "2":
            manage_pat()
            return menu_choice
        elif menu_choice == "0":
            print("ARH Management System successully closed")
            return menu_choice
        else:
            menu_choice = input("Enter option: ")

# after inputting 1 program will display dr menu


def manage_dr():
    print("\nARH Management System")
    print("   Doctor's Menu")
    print("1 - List of Doctors")
    print("2 - Search for Doctor by ID")
    print("3 - Search for Doctor by Name/Partial Name")
    print("4 - Add new Doctor")
    print("5 - Edit Doctor Info")
    print("0 - Return to Main Menu")

    menu_choice = input("Enter option: ").replace(" ", "")

    while menu_choice != "0":
        if menu_choice == "1":
            doctorList = []
            read_doctors_file(doctorList)
            display_list_of_drs(doctorList)
            return manage_dr()
        elif menu_choice == "2":
            doctorList = []
            read_doctors_file(doctorList)
            find_dr_by_id(doctorList)
            return manage_dr()
        elif menu_choice == "3":
            doctorList = []
            read_doctors_file(doctorList)
            match_doctor_by_name(doctorList)
            return manage_dr()
        elif menu_choice == "4":
            doctorList = []
            read_doctors_file(doctorList)
            add_dr_to_list(doctorList)
            return manage_dr()
        elif menu_choice == "5":
            doctorList = []
            read_doctors_file(doctorList)
            edit_dr_info(doctorList)
            return manage_dr()

        else:
            menu_choice = input("Enter option: ")

    print()
    return menu()


# will read doctor file

def read_doctors_file(doctorList):
    doctorFile = open(
        r"doctors.txt")
    lines = doctorFile.readlines()
    print()
    for line in lines:
        items = line.rstrip().split("_")
        dr = Doctor(items[0], items[1], items[2], items[3], items[4], items[5])
        doctorList.append(dr)
    doctorFile.close()
    return doctorList

# allow users to search for dr by ID


def find_dr_by_id(doctorList):
    dr_id = input("Enter Dr ID: ")
    for dr in doctorList:
        if dr.get_doctor_id() == dr_id:
            return print(dr)
    print("Doctor with ID " + str(dr_id) + " was not found")
    return None


# allows users to search for dr by name
def match_doctor_by_name(doctorList):
    dr_name = input("Enter the doctor name: ")
    found = False
    for dr in doctorList:
        if dr_name.lower() in dr.get_name().lower():
            print(dr)
            found = True
    if not found:
        print("Doctor with the name '" + str(dr_name) + "' was not found")

# edit existing dr information


def edit_dr_info(doctorList):
    dr_id = input("Enter Dr ID: ")
    for dr in doctorList:
        if dr.get_doctor_id() == dr_id:
            print(dr)
            name = input("Name: ")
            specialist = input("Specialist: ")
            schedule = input("Schedule: ")
            qualifications = input("Qualifications: ")
            room_number = input("Room Number: ")
            dr.set_name(name)
            dr.set_specialist(specialist)
            dr.set_schedule(schedule)
            dr.set_qualifications(qualifications)
            dr.set_room_number(room_number)
            write_drs_list_to_file(doctorList)
            print("Doctor with ID " + str(dr_id) +
                  " was successfully modified")
            display_list_of_drs(doctorList)
            return None
    print("Doctor with ID " + str(dr_id) + " was not found")
    display_list_of_drs(doctorList)

# will display doctor file


def display_list_of_drs(doctorList):
    for dr in doctorList:
        print(dr)
    return None

# allows user to write new drs into doctor.txt file


def write_drs_list_to_file(doctorList):
    doctorFile = open(
        r"doctors.txt", 'w')
    for doctor in doctorList:
        doctorFile.write(doctor.format_file_layout() + "\n")
    doctorFile.close()
    return None

# add drs into doctor.txt file


def add_dr_to_list(doctorList):
    id = input("ID: ")
    doctorFile = open(
        r"doctors.txt", "r")
    for line in doctorFile:
        while id == line.strip().split("_")[0]:
            for dr in doctorList:
                if dr.get_doctor_id() == id:
                    print(dr)
                    print("Doctor with the ID " +
                          id + " already exists. - cannot add")
                    return manage_dr
                if id != line.strip().split("_")[0]:
                    break

    name = input("Name: ")
    specialist = input("Specialist: ")
    schedule = input("Schedule: ")
    qualifications = input("Qualifications: ")
    room_number = input("Room Number: ")
    dr = Doctor(id, name, specialist, schedule, qualifications, room_number)
    doctorList.append(dr)
    write_drs_list_to_file(doctorList)
    display_list_of_drs(doctorList)
    print("Doctor with the ID " + id + " successfully added")
    return manage_dr

# after inputting 2 program will display dr menu


def manage_pat():
    print("\nARH Management System")
    print("   Patient Menu")
    print("\n1 - List of Patients")
    print("2 - Search for patient by ID")
    print("3 - Add new Patient")
    print("4 - Edit Patient Info")
    print("0 - Return to Main Menu")

    menu_choice = (input("Enter option: ")).replace(" ", "")

    while menu_choice != "0":
        if menu_choice == "1":
            patientList = []
            read_patient_file(patientList)
            display_list_of_pats(patientList)
            return manage_pat()

        elif menu_choice == "2":
            patientList = []
            read_patient_file(patientList)
            find_pat_by_id(patientList)
            return manage_pat()

        elif menu_choice == "3":
            patientList = []
            read_patient_file(patientList)
            add_pat_to_list(patientList)
            return manage_pat()

        elif menu_choice == "4":
            patientList = []
            read_patient_file(patientList)
            edit_pat_info(patientList)
            return manage_pat()

        else:
            menu_choice = input("Enter option: ")

    print()
    return menu()

# will read patient file


def read_patient_file(patientList):
    patientFile = open(
        r"patients.txt")
    lines = patientFile.readlines()
    print()
    for line in lines:
        items = line.rstrip().split("_")
        pat = Patient(items[0], items[1], items[2], items[3], items[4])
        patientList.append(pat)
    patientFile.close()
    return patientList

# search for matching id of patient


def find_pat_by_id(patientList):
    pat_id = input("Enter Patient ID: ")
    for pat in patientList:
        if pat.get_patient_id() == pat_id:
            return print(pat)
    print("Patient with ID " + str(pat_id) + " was not found")
    return manage_pat

# search for matching name of patient


def match_patient_by_name(patientList):
    pat_name = input("Enter the Patient name: ")
    found = False
    for pat in patientList:
        if pat_name.lower() in pat.get_name().lower():
            print(pat)
            found = True
    if not found:
        print("Patient with the name '" + str(pat_name) + "' was not found")

# edit existing patient info


def edit_pat_info(patientList):
    pat_id = input("Enter Dr ID: ")
    for pat in patientList:
        if pat.get_patient_id() == pat_id:
            print(pat)
            name = input("Name: ")
            diagnosis = input("Diagnosis: ")
            gender = input("Gender: ")
            age = input("Age: ")
            pat.set_name(name)
            pat.set_diagnosis(diagnosis)
            pat.set_gender(gender)
            pat.set_age(age)
            write_pats_list_to_file(patientList)
            print("Patient with ID " + str(pat_id) +
                  " was successfully modified")
            display_list_of_pats(patientList)
            return None
    print("Doctor with ID " + str(pat_id) + " was not found")
    display_list_of_pats(patientList)

# display full list of patient from patient.txt


def display_list_of_pats(patientList):
    for pat in patientList:
        print(pat)
    return None

# writes the new patient information


def write_pats_list_to_file(patientList):
    patientFile = open(
        r"patients.txt", 'w')
    for patient in patientList:
        patientFile.write(patient.format_file_layout() + "\n")
    patientFile.close()
    return None

# adds the new written patient infromation


def add_pat_to_list(patientList):
    id = input("ID: ")
    patientFile = open(
        r"patients.txt", "r")
    for line in patientFile:
        while id == line.strip().split("_")[0]:
            for dr in patientList:
                if dr.get_patient_id() == id:
                    print(dr)
                    print("Doctor with the ID " +
                          id + " already exists. - cannot add")
                    return manage_pat
                if id != line.strip().split("_")[0]:
                    break

    name = input("Name: ")
    diagnosis = input("Diagnosis: ")
    gender = input("Gender: ")
    age = input("Age: ")
    pat = Patient(id, name, diagnosis, gender, age)
    patientList.append(pat)
    write_pats_list_to_file(patientList)
    display_list_of_pats(patientList)
    print("Patient with ID " + str(id) + " was successfully added")
    return manage_pat


# calls on menu function
menu()
