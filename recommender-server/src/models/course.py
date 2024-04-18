from sqlmodel import Field, SQLModel

class Course(SQLModel, table=True):
    """
    Representation of a course in the database
    """
    id: int | None = Field(default=None, primary_key=True)
    title: str = Field(unique=True)
