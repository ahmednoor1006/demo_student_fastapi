from typing import Optional

from pydantic import BaseModel


class StudentBase(BaseModel):
    name: str
    marks: int


class StudentCreate(StudentBase):
    teacher_id: int


class Student(BaseModel):
    id: int
    name: str
    marks: int
    teacher_id: int
    teacher: Optional["TeacherBase"] = None

    class Config:
        from_attributes = True


class StudentMini(BaseModel):
    id: int
    name: str
    marks: int

    class Config:
        from_attributes = True


