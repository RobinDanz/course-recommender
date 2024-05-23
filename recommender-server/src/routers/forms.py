from fastapi import APIRouter

from models.form import *
from controllers.form_controller import fuzzy_set_variables

router = APIRouter(
    prefix='/forms',
    tags=['forms'],
    responses={404: {'description' : 'not found'}},
)

@router.post('/', response_model=FormResponse)
async def handle_form(form: FormRequest):
    response = fuzzy_set_variables(form)
    print(response)
    response = FormResponse(response={'coucou': 123})
    return response