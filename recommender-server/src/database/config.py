from sqlmodel import create_engine, SQLModel, Session

from models.user import User

from dotenv import load_dotenv
from os import getenv

load_dotenv()

db_url = getenv('DB_URL')

engine = create_engine(db_url, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

async def get_db_session():
    with Session(engine) as session:
        yield session
