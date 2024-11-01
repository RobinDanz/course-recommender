from sqlmodel import Field, SQLModel, Relationship
from datetime import time
from sqlalchemy import Column, TEXT

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
    description: str = Field(sa_column=Column(TEXT))
    url: str = Field()
    comments: list["Comment"] = Relationship(back_populates='course')


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
    comments: list["CommentBase"]

from sqlmodel import Field, SQLModel, Relationship
from datetime import time

class CommentBase(SQLModel):
    """
    Representation of a comment in the database
    """
    username: str | None = Field()
    content: str = Field()

    course_id: int | None = Field(default=None, foreign_key='course.id')


class Comment(CommentBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

    course: Course | None = Relationship(back_populates='comments')