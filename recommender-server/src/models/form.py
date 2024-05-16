from sqlmodel import SQLModel


class FormResponse(SQLModel):
    response: list


class FormRequest(SQLModel):
    Evaluation : int
    University : int
    CourseType : int
    Track : int
    Lectures : float
    SubjectType : float
    Interactions: float
    Blackboard : float
    Recordings : float
    TeacherAccessibilty : float
