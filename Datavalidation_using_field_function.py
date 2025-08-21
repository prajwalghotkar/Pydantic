from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional

class Patient(BaseModel):
    name: str = Field(max_length=50) # Name ki length 50 charecters se zhyada nahi honi chahiye nahi to pyadantic error dega
    email: EmailStr  # Email validation
    LinkedIn: AnyUrl # LinkedIn URL validation
    age: int = Field(gt=0,lt=90)  # Koi bhi age ki value 0 se zyada aur 90 se km set nahi kr sakta,maen age should in btweeen 0 and 90.
    weight: float = Field(gt=0) # Koi bhi weight ki value 0 se km set nahi kr sakta, mean weight should be greater than 0.
    married: Optional[bool] = None  
    allergies: Optional[List[str]] = Field(max_length=5) # means koi bhi list main 5 se zhyada allergies add nahi kr sakta. 
    contact_details: Dict[str, str]  

def updated_patient_data(patient: Patient):
    print("Update Patient Data")
    print("Name:", patient.name)
    print("Email:", patient.email)
    print("LinkedIn:", patient.LinkedIn)
    print("Age:", patient.age)
    print("Weight:", patient.weight)
    print("Contact Details:", patient.contact_details)
    print("Allergies:",patient.allergies)
    print("Updated")

patient_data = {
    "name": "Prajwal",
    "email": "pmg@gmail.com",
    "LinkedIn": "https://www.linkedin.com/prajwal5675",  
    "age": 24,
    "weight": 59.9,
    "allergies":['pollen','dust'],
    "contact_details": {"phone": "2984789207"}
}

patient1 = Patient(**patient_data)
updated_patient_data(patient1)
