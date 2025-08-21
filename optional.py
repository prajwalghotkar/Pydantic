from pydantic import BaseModel
from typing import List
from typing import Dict
from typing import Optional

class Patient(BaseModel):
    name: str 
    age: int  
    weight: float
    married: Optional[bool] = None # Optional field
    allergies: List[str] = None # Optional field --> jb aap kisi cheez ko optional bana dete ho to usko default value deni hoti hain aur o hain None. 
    contact_details: Dict[str,str]  


def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.married)
    print(patient.allergies)   
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

patient_data = {"name": "Prajwal","age": 24 ,"weight":59.9,"contact_details":{'email':'pmg@gmail.com','phone':'2984789207'}} 
patient1 = Patient(**patient_data)

# insert_patient_data(patient1)
updated_patient_data(patient1)

'''
Optional fields
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