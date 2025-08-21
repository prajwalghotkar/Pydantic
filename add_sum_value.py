# Data Valiadtion
from pydantic import BaseModel

class Patient(BaseModel):
    name: str
    age: int
    weight: float

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)   
    print("inserted")

def updated_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)   
    print("updated")

patient_data = {"name": "Prajwal", "age": '24', "weight":59.9} # age is string but pydantic will convert it to int pydantic is smart enough 

patient1 = Patient(**patient_data)

updated_patient_data(patient1)