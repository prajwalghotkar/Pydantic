from pydantic import BaseModel
from typing import List
from typing import Dict

class Patient(BaseModel):
    name: str # required
    age: int # required 
    weight: float
    married: bool 
    allergies: List[str]
    contact_details: Dict[str,str]  # required field


def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.contact_details)   
    print("inserted")
    print()

def updated_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)   
    print("updated")

patient_data = {"name": "Prajwal", "weight":59.9,"married":True,"allergies":['pollen','dust'],"contact_details":{'email':'pmg@gmail.com','phone':'2984789207'}} # age is missing pydantic will raise an error becouse mere liye age ye required hain okye prajwal
patient1 = Patient(**patient_data)

insert_patient_data(patient1)
updated_patient_data(patient1)


'''
In Pydantic, when you define a model, each field can be required or optional

Required --> must be provided, otherwise Pydantic raises an error.

Optional --> not mandatory, can be missing or set to None.


1. Required fields
Any field without a default value is required.

from pydantic import BaseModel
class Patient(BaseModel):
    name: str     # required
    age: int      # required

If you try:    
    
Patient(name="Prajwal") then it will raise an error becouse age is required.

# Error: age is missing.

'''

'''
2. Optional fields
There are two ways to make a field optional.

(a) Using Optional[...]

from typing import Optional
class Patient(BaseModel):
    name: str
    age: Optional[int]  # can be int OR None

Patient(name="Prajwal")  then it will not raise an error code will work fine becouse age is optional.


(b) Giving a default value
class Patient(BaseModel):
    name: str
    married: bool = False   # default value

Patient(name="Prajwal")  married will be False automatically  this will also work fine.  
'''