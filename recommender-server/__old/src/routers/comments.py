from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from database import config
from typing import Annotated

from models.course import Comment, CommentBase

router = APIRouter(
    prefix='/comments',
    tags=['comments'],
    responses={404: {'description' : 'not found'}},
)

@router.get('/{id}', response_model=Comment)
async def read_course(id: int, session: Annotated[Session, Depends(config.get_db_session)]):
    course = session.get(Comment, id)
    return course

@router.get('/', response_model=list[Comment])
async def read_courses(session: Annotated[Session, Depends(config.get_db_session)]):
    courses = session.exec(select(Comment)).all()
    return courses

@router.post('/', response_model=Comment)
async def create_course(requestCourse: CommentBase, session: Annotated[Session, Depends(config.get_db_session)]):
    db_course = Comment.model_validate(requestCourse)
    session.add(db_course)
    session.commit()
    session.refresh(db_course)

    return db_course