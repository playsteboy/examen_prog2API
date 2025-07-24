import json
from typing import List
from urllib import request

from fastapi import FastAPI , Request
from pydantic import BaseModel
from starlette.responses import Response
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/hello")
def hello():
    return Response(content="Hello world",status_code=200)

@app.get("/welcome")
def welcome(name : str):
    return JSONResponse(content="Welcome "+name , status_code=200)
@app.post("/student")

class StudentModel(BaseModel):
    reference: str
    firstname: str
    lastname: str
    age: int
    pass

student_store: List[StudentModel] = []
def serialized_stored_student():
    student_converted = []
    for student in student_store:
        student_converted.append(student.model_dump())
    return student_converted

@app.post("/students")
def create_student(student_list: List[StudentModel]):
    student_store.extend(student_list)
    return {"student": serialized_stored_student()}

@app.get("/students")
def list_students():
    return {"students": serialized_stored_student()}

@app.put("/students")
def update_students(student_list: List[StudentModel]):
    global student_store
    for new_student in student_list:
        found = False
        for i, existing_student in enumerate(student_store):
            if new_student.reference == existing_student.reference:
                student_store[i] = new_student
                found = True
                break
        if not found:
            student_store.append(new_student)
    return {"events": serialized_stored_student()}

@app.get("/students-authorized")
def students_authorized(request: Request):
    authorization = request.headers.get("Authorization")
    if authorization:
        if authorization == "Bon courage":
            return Response(content="Bon courage", status_code=200)
        return Response(content="Vous n'avez pas la permission necessaire", status_code=400)
    return Response(content="Vous n'etes pas autorise", status_code=401)
