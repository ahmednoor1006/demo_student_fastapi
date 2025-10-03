from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .... import crud, database
from .... import schemas
from ....auth_utils import get_current_user

router = APIRouter()

@router.post("/", response_model=schemas.Teacher)
def create_teacher(teacher: schemas.TeacherCreate, db: Session = Depends(database.get_db),
                   current_user: schemas.User = Depends(get_current_user)):
    return crud.create_teacher(db=db, teacher=teacher)


@router.get("/", response_model=list[schemas.Teacher])
def read_teachers(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db),
                  current_user: schemas.User = Depends(get_current_user)):
    return crud.get_teachers(db, skip=skip, limit=limit)


@router.delete("/{teacher_id}", response_model=schemas.Teacher)
def delete_teacher(teacher_id: int, db: Session = Depends(database.get_db),
                   current_user: schemas.User = Depends(get_current_user)):
    teacher = crud.delete_teacher(db=db, teacher_id=teacher_id)
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return teacher


