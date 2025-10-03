from .student import (
    get_students,
    get_student,
    create_student,
    delete_student,
)
from .teacher import (
    get_teachers,
    get_teacher,
    create_teacher,
    delete_teacher,
)
from .user import (
    get_user_by_email,
    create_user,
)

__all__ = [
    # student
    "get_students",
    "get_student",
    "create_student",
    "delete_student",
    # teacher
    "get_teachers",
    "get_teacher",
    "create_teacher",
    "delete_teacher",
    # user
    "get_user_by_email",
    "create_user",
]


