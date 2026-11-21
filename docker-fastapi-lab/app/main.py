from fastapi import FastAPI

import mysql.connector

app = FastAPI()

def get_db():
    return mysql.connector.connect(
        host="mysql-db",
        user="root",
        password="root123",
        database="studentdb"
    )

@app.get("/")

def home():
    return {"message" : "FastAPI Docker Lab"}

@app.post("/students")
def add_student(name: str, course: str):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO students (name, course) VALUES (%s, %s)",
        (name, course)
    )

    db.commit()
    cursor.close()
    db.close()
    return {"message" : "Student added successfully"}

@app.get("/students")
def get_students():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    cursor.close()
    db.close()
    return students


