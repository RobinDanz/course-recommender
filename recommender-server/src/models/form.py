from sqlmodel import SQLModel


class FormResponse(SQLModel):
    response: str


class FormRequest(SQLModel):
    a: int
    b: str

