from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from database import config
from typing import Annotated

from models.course import Course, CourseRead, CourseCreate

router = APIRouter(
    prefix='/courses',
    tags=['courses'],
    responses={404: {'description' : 'not found'}},
)

@router.get('/{id}', response_model=CourseRead)
async def read_course(id: int, session: Annotated[Session, Depends(config.get_db_session)]):
    course = session.get(Course, id)
    return course

@router.get('/', response_model=list[CourseRead])
async def read_courses(session: Annotated[Session, Depends(config.get_db_session)]):
    courses = session.exec(select(Course)).all()
    return courses

@router.post('/', response_model=CourseRead)
async def create_course(requestCourse: CourseCreate, session: Annotated[Session, Depends(config.get_db_session)]):
    db_course = Course.model_validate(requestCourse)
    session.add(db_course)
    session.commit()
    session.refresh(db_course)

    return db_course