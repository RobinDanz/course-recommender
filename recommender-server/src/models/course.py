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
    site: str = Field()
    code: str = Field()
    start: time = Field()
    end: time = Field()
    track: int = Field()
    semester: int = Field() # 0 = Spring, 1 = Autumn


class CourseCreate(SQLModel):
    title: str
    day: int
    type: int
    site: str
    code: str
    start: time = Field()
    end: time = Field()
    track: int
    semester: int


class CourseRead(SQLModel):
    id: int
    title: str
    day: int
    type: int
    site: str
    code: str
    start: time
    end: time
    track: int
    semester: int