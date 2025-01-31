from sqlalchemy import Column, Integer, String, Date
from database import Base  # Assuming you have your Base in the database.py file

class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    department = Column(String, nullable=False)
    phonenumber = Column(String, nullable=False)  # Phonenumber is now a string
    emailId = Column(String, nullable=False)  # Changed to emailId
    dob = Column(Date, nullable=False)  # dob field to store the date of birth

    def __repr__(self):
        return f"<Student(name={self.name}, age={self.age}, department={self.department}, phonenumber={self.phonenumber}, emailId={self.emailId}, dob={self.dob})>"
