from datetime import datetime, timedelta, timezone
from typing import Annotated

from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt
from sqlmodel import Session, select

from auth.config import ALGORITHM, SECRET_KEY, oauth2_scheme, password_context
from auth.models import TokenData
from database import config
from models.user import User


def verify_password(plain_password: str, hashed_password: str):
    """
    Check plaintext against hash
    """
    return password_context.verify(plain_password, hashed_password)

def get_password_hash(password: str):
    """
    Return hash of the password
    """
    return password_context.hash(password)

async def get_user(username: str, session: Session):
    """
    Returns a user from the database
    """
    query = select(User).where(User.username == username)
    user = session.exec(query).first()
    return user

async def authenticate_user(username: str, password: str, session: Session):
    """
    Verify if a user exists and if the given password matches
    """
    user = await get_user(username, session)

    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.noew(timezone.utc) + timedelta(minutes=15)
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(session: Annotated[Session, Depends(config.get_db_session)], token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Could not validate credentials',
        headers={'WWW-Authenticate': 'Bearer'},
    )

    try: 
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')

        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    
    user = await get_user(token_data.username, session)

    if user is None: 
        raise credentials_exception
    return user