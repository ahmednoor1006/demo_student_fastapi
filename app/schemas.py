from pydantic import BaseModel
from typing import List, Optional

# ---------------- Student Schemas ----------------
class StudentBase(BaseModel):
    name: str
    marks: int

class StudentCreate(StudentBase):
    teacher_id: int

class Student(StudentBase):  # <-- main Student schema
    id: int
    teacher_id: int
    # show teacher info in response
    teacher: Optional["TeacherBase"] = None

    class Config:
        from_attributes = True


# ---------------- Teacher Schemas ----------------
class TeacherBase(BaseModel):
    name: str
    subject: str

class TeacherCreate(TeacherBase):
    pass

class Teacher(TeacherBase):   # <-- main Teacher schema
    id: int
    students: List["StudentMini"] = []

    class Config:
        from_attributes = True

class StudentMini(BaseModel):   # student info inside teacher
    id: int
    name: str
    marks: int

    class Config:
        from_attributes = True


# ---------------- User Schemas ----------------
class UserBase(BaseModel):
    email: str
    name: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config:
        from_attributes = True


# Solve forward references
Student.model_rebuild()
Teacher.model_rebuild()
