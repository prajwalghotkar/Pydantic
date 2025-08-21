# TypeValiadtion

from pydantic import BaseModel

class Patient(BaseModel):
    name: str
    age: int

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)   
    print("inserted")

def updated_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)   
    print("updated")

patient_data = {"name": "Prajwal", "age": 24}

patient1 = Patient(**patient_data)

updated_patient_data(patient1)