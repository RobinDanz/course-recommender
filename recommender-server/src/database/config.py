from sqlmodel import create_engine, SQLModel, Session

from models.user import User

db_url = 'mysql+pymysql://root:mariadb@db:3306/recommender'

engine = create_engine(db_url, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

async def get_db_session():
    with Session(engine) as session:
        yield session
