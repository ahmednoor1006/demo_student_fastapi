from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .... import crud, database
from .... import schemas
from ....auth_utils import get_current_user

router = APIRouter()

@router.post("/", response_model=schemas.Student)
def create_student(student: schemas.StudentCreate, db: Session = Depends(database.get_db),
                   current_user: schemas.User = Depends(get_current_user)):
    return crud.create_student(db=db, student=student)


@router.get("/", response_model=list[schemas.Student])
def read_students(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db),
                  current_user: schemas.User = Depends(get_current_user)):
    return crud.get_students(db, skip=skip, limit=limit)


@router.delete("/{student_id}", response_model=schemas.Student)
def delete_student(student_id: int, db: Session = Depends(database.get_db),
                   current_user: schemas.User = Depends(get_current_user)):
    student = crud.delete_student(db=db, student_id=student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student


