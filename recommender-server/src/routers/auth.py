from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session

from database import config

from datetime import timedelta
from typing import Annotated

from auth.utils import authenticate_user, create_access_token
from auth.models import Token
from auth.config import ACCESS_TOKEN_EXPIRE_MINUTES

router = APIRouter(
    prefix='',
    tags=['auth'],
    responses={404: {'description': 'not found'}},
)


@router.post("/token")
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], session: Annotated[Session, Depends(config.get_db_session)]) -> Token:
    user = await authenticate_user(form_data.username, form_data.password, session)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")