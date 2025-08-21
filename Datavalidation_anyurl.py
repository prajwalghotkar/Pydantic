from pydantic import BaseModel, EmailStr, AnyUrl
from typing import List, Dict, Optional

class Patient(BaseModel):
    name: str 
    email: EmailStr  # Email validation
    LinkedIn: AnyUrl # LinkedIn URL validation
    age: int  
    weight: float
    married: Optional[bool] = None  
    allergies: Optional[List[str]] = None 
    contact_details: Dict[str, str]  

def updated_patient_data(patient: Patient):
    print("Update Patient Data")
    print("Name:", patient.name)
    print("Email:", patient.email)
    print("LinkedIn:", patient.LinkedIn)
    print("Age:", patient.age)
    print("Weight:", patient.weight)
    print("Contact Details:", patient.contact_details)
    print("Updated")

patient_data = {
    "name": "Prajwal",
    "email": "pmg@gmail.com",
    "LinkedIn": "https://www.linkedin.com/prajwal5675",  
    "age": 24,
    "weight": 59.9,
    "contact_details": {"phone": "2984789207"}
}

patient1 = Patient(**patient_data)
updated_patient_data(patient1)
