from fastapi import FastAPI, HTTPException, Query, Depends
from sqlalchemy.orm import Session
from datetime import datetime
from models import Student
from schemas import StudentCreate, StudentUpdate
from database import get_session, init_db
from sqlalchemy import text

# Initialize FastAPI app
app = FastAPI()

# Initialize the database
init_db()

# Endpoint to create a new student
@app.post("/students")
async def create_student(student: StudentCreate, db: Session = Depends(get_session)):
    try:
        dob = student.dob
        query = text("""
        INSERT INTO student (name, age, department, phonenumber, emailId, dob)
        VALUES (:name, :age, :department, :phonenumber, :emailId, :dob);
        """)
        db.execute(query, {
            'name': student.name,
            'age': student.age,
            'department': student.department,
            'phonenumber': student.phonenumber,
            'emailId': student.emailId,
            'dob': dob
        })
        db.commit()
        return {"message": "Student added successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint to get all students
@app.get("/students")
async def get_all_students(db: Session = Depends(get_session)):
    try:
        students = db.query(Student).all()
        return students
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint to get a student by ID
@app.get("/students/{student_id}")
async def get_student_by_id(student_id: int, db: Session = Depends(get_session)):
    try:
        student = db.query(Student).filter(Student.id == student_id).first()
        if not student:
            raise HTTPException(status_code=404, detail="Student not found")
        return student
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint to update student details
@app.put("/students/{student_id}")
async def update_student(student_id: int, student: StudentUpdate, db: Session = Depends(get_session)):
    try:
        student_obj = db.query(Student).filter(Student.id == student_id).first()
        if not student_obj:
            raise HTTPException(status_code=404, detail="Student not found")
        student_obj.phonenumber = student.phonenumber
        student_obj.emailId = student.emailId
        db.commit()
        return {"message": "Student updated successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint to delete a student by ID
@app.delete("/students/{student_id}")
async def delete_student(student_id: int, db: Session = Depends(get_session)):
    try:
        student = db.query(Student).filter(Student.id == student_id).first()
        if not student:
            raise HTTPException(status_code=404, detail="Student not found")
        db.delete(student)
        db.commit()
        return {"message": "Student deleted successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint to get students by department
@app.get("/students/department/{department}")
async def get_students_by_department(department: str, db: Session = Depends(get_session)):
    try:
        students = db.query(Student).filter(Student.department == department).all()
        return students
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint to get students by DOB
@app.get("/students/dob/{dob}")
async def get_students_by_dob(dob: str, db: Session = Depends(get_session)):

    try:
        dob_date = datetime.strptime(dob, "%Y-%m-%d").date()
        students = db.query(Student).filter(Student.dob == dob_date).all()
        return students
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format. Use YYYY-MM-DD.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
