from pydantic import BaseModel
from typing import List
from typing import Dict

class Patient(BaseModel):
    name: str
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str,str]  # key--> string and values--> string


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

patient_data = {"name": "Prajwal", "age": '24', "weight":59.9,"married":True,"allergies":['pollen','dust'],"contact_details":{'email':'pmg@gmail.com','phone':'2984789207'}} # age is string but pydantic will convert it to int pydantic is smart enough 

patient1 = Patient(**patient_data)

insert_patient_data(patient1)
updated_patient_data(patient1)


'''
Why List[str] instead of just List?

List[str] means: This list must contain only strings.
Example: ["pollen", "dust"] 
Example: [1, 2, 3]  (Pydantic will raise a validation error)
If you just write List:
like that---> allergies: List
then Python (and Pydantic) doesn’t know what the list should contain. It could be a list of numbers, dicts, strings, etc. No validation on list items. so List[str] gives stronger validation.similerly in case of dictonary 

Why Dict[str, str] instead of just Dict?

Dict[str, str] means: This dictionary must have keys of type str and values of type str.
Example: {"email": "pmg@gmail.com", "phone": "1234567890"} 
Example: {1: "pmg@gmail.com", "phone": 123} 
If you just write Dict----> contact_details: Dict. then it allows any type for keys and values. No strong validation.
Dict[str, str] enforces both keys and values to be strings.
'''