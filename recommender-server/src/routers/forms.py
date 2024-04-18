from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from database import config
from typing import Annotated

from models.form import *
from controllers.form_controller import *

router = APIRouter(
    prefix='/forms',
    tags=['forms'],
    responses={404: {'description' : 'not found'}},
)

@router.post('/', response_model=FormResponse)
async def handle_form(form: FormRequest):
    data = form
    response = fuzzy(data)
    return response