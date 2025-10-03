import os
from fastapi import FastAPI, Depends, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from starlette.middleware.sessions import SessionMiddleware
import crud, models, schemas, database, auth
from auth_utils import get_current_user

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Student Teacher Management System")

# Add session middleware for OAuth
app.add_middleware(SessionMiddleware, secret_key=os.getenv("SECRET_KEY", "your-secret-key"))

# Mount static files
static_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "static")
app.mount("/static", StaticFiles(directory=static_dir), name="static")

# Include auth router
app.include_router(auth.router)

# Serve frontend
@app.get("/")
async def read_index():
    return FileResponse(os.path.join(static_dir, 'index.html'))

@app.get("/dashboard")
async def read_dashboard():
    return FileResponse(os.path.join(static_dir, 'dashboard.html'))

@app.get("/student")
async def read_student():
    return FileResponse(os.path.join(static_dir, 'student.html'))

@app.get("/teacher")
async def read_teacher():
    return FileResponse(os.path.join(static_dir, 'teacher.html'))

# ---------------- Teacher Routes ----------------
@app.post("/teachers/", response_model=schemas.Teacher)
def create_teacher(teacher: schemas.TeacherCreate, db: Session = Depends(database.get_db), 
                   current_user: schemas.User = Depends(get_current_user)):
    return crud.create_teacher(db=db, teacher=teacher)

@app.get("/teachers/", response_model=list[schemas.Teacher])
def read_teachers(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db), 
                  current_user: schemas.User = Depends(get_current_user)):
    return crud.get_teachers(db, skip=skip, limit=limit)

@app.delete("/teachers/{teacher_id}", response_model=schemas.Teacher)
def delete_teacher(teacher_id: int, db: Session = Depends(database.get_db), 
                   current_user: schemas.User = Depends(get_current_user)):
    teacher = crud.delete_teacher(db=db, teacher_id=teacher_id)
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return teacher

# ---------------- Student Routes ----------------
@app.post("/students/", response_model=schemas.Student)
def create_student(student: schemas.StudentCreate, db: Session = Depends(database.get_db),
                   current_user: schemas.User = Depends(get_current_user)):
    return crud.create_student(db=db, student=student)

@app.get("/students/", response_model=list[schemas.Student])
def read_students(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db),
                  current_user: schemas.User = Depends(get_current_user)):
    return crud.get_students(db, skip=skip, limit=limit)

@app.delete("/students/{student_id}", response_model=schemas.Student)
def delete_student(student_id: int, db: Session = Depends(database.get_db),
                   current_user: schemas.User = Depends(get_current_user)):
    student = crud.delete_student(db=db, student_id=student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student
