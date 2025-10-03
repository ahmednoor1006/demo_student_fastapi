from typing import List

from pydantic import BaseModel

from .student import StudentMini


class TeacherBase(BaseModel):
    name: str
    subject: str


class TeacherCreate(TeacherBase):
    pass


class Teacher(TeacherBase):
    id: int
    students: List[StudentMini] = []

    class Config:
        from_attributes = True


