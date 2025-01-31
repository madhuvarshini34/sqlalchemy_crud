# models.py
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    department = Column(String)
    phonenumber = Column(Integer)
    emailId = Column(String)
    dob = Column(Date)

    def __repr__(self):
        return f"<Student(name={self.name}, department={self.department})>"
