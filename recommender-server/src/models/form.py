from sqlmodel import SQLModel


class FormResponse(SQLModel):
    response: dict


class FormRequest(SQLModel):
    evaluation : list
    university : list
    courseType : list
    track : list
    lectures : list
    subjectType : int
    interactions: int
    blackboard : int
    recordings : int
    teacherAccessibilty : int
