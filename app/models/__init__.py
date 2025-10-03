from ..database import Base

from .teacher import Teacher
from .student import Student
from .user import User

__all__ = [
    "Base",
    "Teacher",
    "Student",
    "User",
]


