from pydantic import BaseModel

class Patient(BaseModel):
    name: str
    age: int

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)   # this code is right
    print("inserted")

patient_data = {"name": "Prajwal", "age": 24}

patient1 = Patient(**patient_data)

insert_patient_data(patient1)
