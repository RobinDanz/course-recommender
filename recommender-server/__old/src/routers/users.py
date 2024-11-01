from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from database import config
from auth.utils import get_current_user, password_context
from typing import Annotated

from models.user import User, UserCreate, UserRead

router = APIRouter(
    prefix='/users',
    tags=['users'],
    responses={404: {'description': 'not found'}},
)

@router.get('/{id}', response_model=UserRead)
async def read_user(id: int, session: Annotated[Session, Depends(config.get_db_session)], user: Annotated[User, Depends(get_current_user)]):
    user = session.get(User, id)
    return user

@router.get('/', response_model=list[UserRead])
async def read_users(session: Annotated[Session, Depends(config.get_db_session)], user: Annotated[User, Depends(get_current_user)]):
    users = session.exec(select(User)).all()

    return users

@router.post('/')
async def create_user(requestUser: UserCreate, session: Annotated[Session, Depends(config.get_db_session)], user: Annotated[User, Depends(get_current_user)]):
    requestUser.password = password_context.hash(requestUser.password)
    db_user = User.model_validate(requestUser)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return db_user




    
