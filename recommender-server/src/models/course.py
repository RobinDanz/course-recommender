from sqlmodel import Field, SQLModel
from datetime import time

class Course(SQLModel, table=True):
    """
    Representation of a course in the database
    """
    id: int | None = Field(default=None, primary_key=True)
    title: str = Field()
    day: int = Field()
    type: int = Field()
    site: int = Field()
    code: str = Field()
    start: time = Field()
    end: time = Field()
    track: int = Field()
    semester: int = Field()
    description: str = Field()
    url: str = Field()


class CourseCreate(SQLModel):
    title: str
    day: int
    type: int
    site: int
    code: str
    start: time = Field()
    end: time = Field()
    track: int
    semester: int
    description: str
    url: str


class CourseRead(SQLModel):
    id: int
    title: str
    day: int
    type: int
    site: int
    code: str
    start: time
    end: time
    track: int
    semester: int
    description: str
    url: str