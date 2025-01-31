# **Student Management System using SQLAlchemy and FastAPI**

This project is a **Student Management System API** built using **FastAPI** and **SQLAlchemy**. It provides a set of endpoints to perform CRUD (Create, Read, Update, Delete) operations on student data and supports advanced filtering based on attributes like department and date of birth (DOB). 

---

### **Key Features**
- **Add a New Student**: Create new student records with fields like name, age, department, phone number, email, and DOB.
- **Retrieve All Students**: Fetch a list of all students stored in the database.
- **Search by ID**: Get details of a student by their unique ID.
- **Filter by Department**: Retrieve all students enrolled in a specific department.
- **Filter by DOB**: Find students born on a specific date.
- **Update Student Details**: Update phone numbers or email addresses for existing students.
- **Delete Student Records**: Remove a student record from the database.

---

### **Tech Stack**
- **Backend Framework**: FastAPI (for building the RESTful APIs)
- **Database**: MySQL (with SQLAlchemy as the ORM)
- **Dependencies Management**: Python's `pip`
- **Pydantic**: For data validation
- **Docker (Optional)**: To containerize the application

---

### **Setup and Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure the database:
   - Update `DATABASE_URL` in the `database.py` file to your MySQL credentials.
4. Run the application:
   ```bash
   uvicorn main:app --reload
   ```
5. Access the API:
   - Open your browser or use a tool like Postman to access the docs at:
     ```
     http://127.0.0.1:8000/docs
     ```

---

### **API Endpoints**
| Method | Endpoint                        | Description                              |
|--------|---------------------------------|------------------------------------------|
| POST   | `/students`                     | Create a new student                     |
| GET    | `/students`                     | Retrieve all students                    |
| GET    | `/students/{student_id}`        | Retrieve a student by ID                 |
| GET    | `/students/department/{department}` | Get students by department              |
| GET    | `/students/dob/{dob}`           | Get students by date of birth            |
| PUT    | `/students/{student_id}`        | Update student details by ID             |
| DELETE | `/students/{student_id}`        | Delete a student by ID                   |

---

### **Contributions**
Contributions, issues, and feature requests are welcome! Feel free to fork the repository and submit a pull request.
