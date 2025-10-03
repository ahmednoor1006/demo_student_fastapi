from sqlalchemy.orm import Session

from .. import models, schemas


def get_teachers(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Teacher).offset(skip).limit(limit).all()


def get_teacher(db: Session, teacher_id: int):
    return db.query(models.Teacher).filter(models.Teacher.id == teacher_id).first()


def create_teacher(db: Session, teacher: schemas.TeacherCreate):
    db_teacher = models.Teacher(name=teacher.name, subject=teacher.subject)
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return db_teacher


def delete_teacher(db: Session, teacher_id: int):
    db_teacher = db.query(models.Teacher).filter(models.Teacher.id == teacher_id).first()
    if db_teacher:
        db.delete(db_teacher)
        db.commit()
        return db_teacher
    return None


