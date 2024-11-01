from sqlmodel import Field, SQLModel

class User(SQLModel, table=True):
    """
    Representation of a user in the database
    """
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True)
    password: str = Field()
    type: int = Field()


class UserCreate(SQLModel):
    """
    User on creation
    """
    username: str
    password: str
    type: int

class UserRead(SQLModel):
    """
    User on read
    """
    id: int
    username: str
    type: int