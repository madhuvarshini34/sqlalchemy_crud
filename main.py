from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from models import Student  # Make sure this is your Student model
from database import Base, Session

# Establishing database connection
DATABASE_URL = "mysql+mysqlconnector://root:root@localhost/tution"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Ensure the tables are created if they don't exist
Base.metadata.create_all(engine)

# Function to create a new student using raw SQL queries
def create_student():
    try:
        # Get input from the user
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        department = input("Enter department: ")
        phonenumber = input("Enter phone number: ")
        emailId = input("Enter email ID: ")
        dob_input = input("Enter date of birth (YYYY-MM-DD): ")

        # Validate date format
        try:
            dob = datetime.strptime(dob_input, "%Y-%m-%d").date()  # Convert to proper date object
        except ValueError:
            print("Invalid date format. Please enter date in YYYY-MM-DD format.")
            return  # Exit the function if the date is invalid

        # Define raw SQL query using `text()`
        query = text("""
        INSERT INTO student (name, age, department, phonenumber, emailId, dob)
        VALUES (:name, :age, :department, :phonenumber, :emailId, :dob);
        """)

        # Execute the query with the provided data
        session.execute(query, {'name': name, 'age': age, 'department': department, 
                                'phonenumber': phonenumber, 'emailId': emailId, 'dob': dob})

        # Commit the changes to the database
        session.commit()

        print("Student added successfully!")
    except Exception as e:
        session.rollback()  # Rollback the transaction in case of error
        print(f"Error: {e}")

# Function to get all students
def get_all_students():
    try:
        students = session.query(Student).all()
        for student in students:
            print(f"ID: {student.id}, Name: {student.name}, Age: {student.age}, Department: {student.department}, Phone: {student.phonenumber}, Email ID: {student.emailId}, DOB: {student.dob}")
    except Exception as e:
        print(f"Error: {e}")

# Function to get a student by ID
def get_student_by_id(student_id):
    try:
        student = session.query(Student).filter(Student.id == student_id).first()
        if student:
            print(f"ID: {student.id}, Name: {student.name}, Age: {student.age}, Department: {student.department}, Phone: {student.phonenumber}, Email ID: {student.emailId}, DOB: {student.dob}")
        else:
            print("Student not found.")
    except Exception as e:
        print(f"Error: {e}")

# Function to get a student by name
def get_student_by_name(student_name):
    try:
        student = session.query(Student).filter(Student.name == student_name).first()
        if student:
            print(f"ID: {student.id}, Name: {student.name}, Age: {student.age}, Department: {student.department}, Phone: {student.phonenumber}, Email ID: {student.emailId}, DOB: {student.dob}")
        else:
            print("Student not found.")
    except Exception as e:
        print(f"Error: {e}")

# Function to update student details
def update_student(student_id):
    try:
        student = session.query(Student).filter(Student.id == student_id).first()
        if student:
            # Get new phone and email ID to update
            new_phonenumber = input("Enter new phone number: ")
            new_emailId = input("Enter new email ID: ")  # Changed to emailId

            student.phonenumber = new_phonenumber
            student.emailId = new_emailId

            # Commit the changes
            session.commit()

            print("Student updated successfully!")
        else:
            print("Student not found.")
    except Exception as e:
        session.rollback()  # Rollback the transaction in case of error
        print(f"Error: {e}")

# Function to delete student by ID
def delete_student(student_id):
    try:
        student = session.query(Student).filter(Student.id == student_id).first()
        if student:
            session.delete(student)
            session.commit()
            print("Student deleted successfully!")
        else:
            print("Student not found.")
    except Exception as e:
        session.rollback()  # Rollback the transaction in case of error
        print(f"Error: {e}")

# Function to get a student by DOB
def get_student_by_dob(dob_input):
    try:
        dob = datetime.strptime(dob_input, "%Y-%m-%d").date()  # Convert to proper date object
        student = session.query(Student).filter(Student.dob == dob).all()
        if student:
            for s in student:
                print(f"ID: {s.id}, Name: {s.name}, Age: {s.age}, Department: {s.department}, Phone: {s.phonenumber}, Email ID: {s.emailId}, DOB: {s.dob}")
        else:
            print("No student found with this date of birth.")
    except ValueError:
        print("Invalid date format. Please enter date in YYYY-MM-DD format.")

# Function to get a student by department
def get_student_by_department(department_name):
    try:
        students = session.query(Student).filter(Student.department == department_name).all()
        if students:
            for student in students:
                print(f"ID: {student.id}, Name: {student.name}, Age: {student.age}, Department: {student.department}, Phone: {student.phonenumber}, Email ID: {student.emailId}, DOB: {student.dob}")
        else:
            print("No student found in this department.")
    except Exception as e:
        print(f"Error: {e}")

# Main menu function
def main_menu():
    while True:
        print("\nSelect an option:")
        print("1. Create Student")
        print("2. Get All Students")
        print("3. Get Student by ID")
        print("4. Get Student by Name")
        print("5. Get Student by DOB")
        print("6. Get Student by Department")
        print("7. Update Student")
        print("8. Delete Student")
        print("9. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            create_student()
        elif choice == '2':
            get_all_students()
        elif choice == '3':
            student_id = int(input("Enter student ID: "))
            get_student_by_id(student_id)
        elif choice == '4':
            student_name = input("Enter student name: ")
            get_student_by_name(student_name)
        elif choice == '5':
            dob_input = input("Enter student DOB (YYYY-MM-DD): ")
            get_student_by_dob(dob_input)
        elif choice == '6':
            department_name = input("Enter department name: ")
            get_student_by_department(department_name)
        elif choice == '7':
            student_id = int(input("Enter student ID to update: "))
            update_student(student_id)
        elif choice == '8':
            student_id = int(input("Enter student ID to delete: "))
            delete_student(student_id)
        elif choice == '9':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

# Run the main menu
if __name__ == "__main__":
    main_menu()
    

