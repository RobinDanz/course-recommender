import json
from sqlmodel import create_engine, SQLModel, Session, select, exists
from datetime import time
from models.course import CourseCreate, Course

from dotenv import load_dotenv
from os import getenv

load_dotenv()

db_url = getenv('DB_URL')

engine = create_engine(db_url, echo=False)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

async def get_db_session():
    with Session(engine) as session:
        yield session


async def fill_db():
    courses_model = []
    with open('scripts/out/data.json') as f:
        courses = json.load(f)
        for course in courses:
            sem = course['semester'][0]
            c = CourseCreate(
                title=course['name'],
                day=0 if not course['day'] else course['day'],
                type=0 if course['type'] == 'Course' else 1,
                site=course['site'],
                code=course['codes'][0],
                start=str_to_time(course['start']),
                end=str_to_time(course['end']),
                track=int(course['tracks'][0].replace('T', '')),
                semester=0 if sem == 'S' else 1
            )

            db_course = Course.model_validate(c)
            courses_model.append(db_course)

            with Session(engine) as session:
                if len(session.exec(select(Course).where(Course.code == c.code)).all()) < 1:
                    session.add(db_course)
                    session.commit()


    


def str_to_time(time_str: str):
    t = time(0,0,0)
    if time_str:
        split = time_str.split(':')
        t = time(int(split[0]), int(split[1]))
    return t
        