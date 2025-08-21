# Using_Field_Function_Attach_Meta_Data using Annotated 
from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: Annotated[str,Field(max_length=50,title='Name of the Patient',description="Full legal name of the patient as recorded in official medical records (max 50 characters).",examples=["Prajwal Ghotkar", "Aarav Sharma", "Emily Johnson"])] 
    email: EmailStr  # Email validation
    LinkedIn: AnyUrl # LinkedIn URL validation
    age: int = Field(gt=0,lt=90)  
    weight: Annotated[float, Field(gt=0,strict=True)] # strict=True = No automatic type conversion.
    # It enforces that the value provided is exactly a float, not "75", not 75 (int), only 75.0.
    married: Annotated[bool,Field(default=None,description="Indicates if the patient is married or not.")]   
    allergies: Annotated[Optional[List[str]], Field(default=None,max_length=5)]  
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
