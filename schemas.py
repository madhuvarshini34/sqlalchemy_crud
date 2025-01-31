# schemas.py
from pydantic import BaseModel
from datetime import date

class StudentCreate(BaseModel):
    name: str
    age: int
    department: str
    phonenumber: int
    emailId: str
    dob: date  # YYYY-MM-DD format

class StudentUpdate(BaseModel):
    phonenumber: int
    emailId: str
