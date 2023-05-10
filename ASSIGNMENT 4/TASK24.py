class Hospital:

    def __init__(self, hospital_name):

        self.hospital_name = hospital_name
        self.doctors = {}
        self.patients = {}

    def addDoctor(self, doctor):

        if type(doctor) != Doctor:
            print("Invalid object passed. Please try again.")
            return
        else:
            self.doctors[doctor.id_number] = [doctor.name, doctor.speciality]

    def getDoctorByID(self, reference_id):

        if reference_id in self.doctors:

            summary = ""
            summary += f"Doctor's ID: {reference_id} \n"
            summary += f"Name: {self.doctors[reference_id][0]} \n"
            summary += f"Speciality: {self.doctors[reference_id][1]}"
            return summary

        else:
            print(f"No doctor found with ID {reference_id}")

    def allDoctors(self):

        print("All Doctors:")
        number_of_doctors = len(self.doctors)
        print(f"Number of Doctors: {number_of_doctors}")
        print(self.doctors)

    def addPatient(self, patient):

        if type(patient) != Patient:
            print("Invalid object passed. Please try again.")
            return
        else:
            self.patients[patient.id_number] = [patient.name, patient.age, patient.cell_no]

    def getPatientByID(self, reference_id):

        if reference_id in self.patients:

            summary = ""
            summary += f"Patient's ID: {reference_id} \n"
            summary += f"Name: {self.patients[reference_id][0]} \n"
            summary += f"Age: {self.patients[reference_id][1]} \n"
            summary += f"Phone no.: {self.patients[reference_id][2]}"

            return summary

        else:
            print(f"No Patient found with ID {reference_id}")

    def allPatients(self):

        print("All Patients:")
        number_of_patients = len(self.patients)
        print(f"Number of Patients: {number_of_patients}")
        print(self.patients)


class Doctor:

    def __init__(self, id_no, identity, name, speciality):

        self.id_number = id_no
        self.identity = identity
        self.name = name
        self.speciality = speciality


class Patient:

    def __init__(self, id_no, identity, name, age, cell_no):

        self.id_number = id_no
        self.identity = identity
        self.name = name
        self.age = age
        self.cell_no = cell_no


h = Hospital("Evercare")
d1 = Doctor("1d", "Doctor", "Samar Kumar", "Neurologist")
h.addDoctor(d1)
print("=================================")
print(h.getDoctorByID("1d"))
print("=================================")
p1 = Patient("1p", "Patient", "Kashem Ahmed", 35, 12345)
h.addPatient(p1)
print("=================================")
print(h.getPatientByID("1p"))
print("=================================")
p2 = Patient("2p", "Patient", "Tanina Haque", 26, 33456)
h.addPatient(p2)
print("=================================")
print(h.getPatientByID("2p"))
print("=================================")
h.allDoctors()
h.allPatients()
