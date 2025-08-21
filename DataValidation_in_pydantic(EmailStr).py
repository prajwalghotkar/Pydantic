from pydantic import BaseModel, EmailStr
from typing import List, Dict, Optional

class Patient(BaseModel):
    name: str 
    email: EmailStr  # Email validation
    age: int  
    weight: float
    married: Optional[bool] = None  
    allergies: Optional[List[str]] = None 
    contact_details: Dict[str, str]  

def insert_patient_data(patient: Patient):
    print("Insert Patient Data")
    print("Name:", patient.name)
    print("Email:", patient.email)
    print("Age:", patient.age)
    print("Married:", patient.married)
    print("Allergies:", patient.allergies)
    print("Inserted \n")

def updated_patient_data(patient: Patient):
    print("Update Patient Data")
    print("Name:", patient.name)
    print("Email:", patient.email)
    print("Age:", patient.age)
    print("Weight:", patient.weight)
    print("Married:", patient.married)
    print("Allergies:", patient.allergies)
    print("Contact Details:", patient.contact_details)
    print("Updated")

patient_data = {
    "name": "Prajwal",
    "email": "pmg@gmail.com",
    "age": 24,
    "weight": 59.9,
    "contact_details": {"phone": "2984789207"}
}

patient1 = Patient(**patient_data)

insert_patient_data(patient1)
updated_patient_data(patient1)
