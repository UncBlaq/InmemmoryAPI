#Importing neccessary modules
from fastapi import FastAPI
from uuid import UUID

#Creating an app variable
app = FastAPI()

#Empty student dictionary
students = {}

#demo student
student = {
    "id" : 1,
    "Name" : " ",
"Age" : 20,
"Sex" : " ",
"Height ": 2.2
}

#post operation
@app.post("/students")
def create_student( 
                  name : str,
                    age : int,
                    sex : str,
                    height : float
                    ):

    new_student = student.copy()
    new_student["id"] = str(UUID(int = len(students) + 1))

    new_student["Name"] = name
    new_student["Age"] = age
    new_student["Sex"] = sex
    new_student["Height "] = height

    students[new_student["id"]] = new_student
   
    return new_student

#Read operation
@app.get('/students/')
def get_students():
    return students

@app.get('/students/{id}/')
def get_student_by_id(id : UUID):
    student = students.get(str(id))
    if not student:
        return f"Student with id: {id} not found"
    return student

@app.put("/student/update")
def update_student(id : str, Name : str, Age : int, Sex : str, Height: float):
    student = students.get(str(id))
    if not student:
        return f"Student with id: {id} not found"
    student["Name"] = Name
    student["Age"] = Age
    student["Sex"] = Sex
    student["Height "] = Height
    return student


@app.delete("/student/delete")
def delete_student(id : str):
    student = students.get(str(id))
    if not student:
        return f"Student with id: {id} not found"
    del students[str(id)]
    return f"Student with id: {id} deleted"
 
  


                
    
   