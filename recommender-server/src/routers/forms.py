from typing import Annotated
from fastapi import APIRouter, Depends

from models.form import *
from controllers.form_controller import fuzzy_set_variables, create_fuzzy
from sqlmodel import Session, select
from database import config
from models.course import Course

router = APIRouter(
    prefix='/forms',
    tags=['forms'],
    responses={404: {'description' : 'not found'}},
)

@router.post('/', response_model=FormResponse)
async def handle_form(form: FormRequest, session: Annotated[Session, Depends(config.get_db_session)]):
    FS = create_fuzzy()
    result = fuzzy_set_variables(form, FS)
    response_dict = {}
    for course in result.keys():
        c = session.exec(select(Course).where(Course.title == course)).all()[0]
        response_dict[c.id] = result[course]
    print(response_dict)
    response = FormResponse(result=response_dict)
    return response