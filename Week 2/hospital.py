class Surgeon:
    def __init__(self, surgeon_id, name, surgeon_type):
        self.surgeon_id = surgeon_id
        self.name = name
        self.surgeon_type = surgeon_type
        self.hospitals = []
        self.operated_patients = []

    def add_hospital(self, hospital):
        self.hospitals.append(hospital)

    def operate_patient(self, patient):
        self.operated_patients.append(patient)

    def get_operated_patients(self):
        return self.operated_patients

class Patient:
    def __init__(self, patient_id, name):
        self.patient_id = patient_id
        self.name = name

    def __str__(self):
        return f"Patient[id={self.patient_id}, name={self.name}]"

class Ward:
    def __init__(self, ward_no):
        self.ward_no = ward_no
        self.patients = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def get_patients(self):
        return self.patients

class Hospital:
    def __init__(self, name):
        self.name = name
        self.wards = {}

    def add_patient_to_ward(self, patient, ward_no):
        if ward_no not in self.wards:
            self.wards[ward_no] = Ward(ward_no)
        self.wards[ward_no].add_patient(patient)

    def get_patients_in_ward(self, ward_no):
        if ward_no in self.wards:
            return self.wards[ward_no].get_patients()
        return []

class HospitalController:
    def __init__(self, surgeons):
        self.surgeons = surgeons

    def total_patients_operated(self):
        total = 0
        for surgeon in self.surgeons:
            total += len(surgeon.operated_patients)
        return total

    def patients_operated_by_surgeon(self, surgeon):
        return surgeon.get_operated_patients()


#main
# Hospitals
h1 = Hospital("Apollo")
h2 = Hospital("Fortis")

# Surgeon
s1 = Surgeon(1, "Dr. Rao", "Senior")
s1.add_hospital(h1)
s1.add_hospital(h2)

# Patients
p1 = Patient(101, "Ananya")
p2 = Patient(102, "XYZ")
p3 = Patient(103, "ABC")

# Admit patients
h1.add_patient_to_ward(p1, 1)
h1.add_patient_to_ward(p2, 1)
h2.add_patient_to_ward(p3, 2)

# Operations
s1.operate_patient(p1)
s1.operate_patient(p3)

# Controller
controller = HospitalController([s1])

# Outputs
print("Total patients operated:", controller.total_patients_operated())

print("Patients operated by Dr. Rao:")
for p in controller.patients_operated_by_surgeon(s1):
    print(p)

print("Patients in ward 1 of Apollo:")
for p in h1.get_patients_in_ward(1):
    print(p)
