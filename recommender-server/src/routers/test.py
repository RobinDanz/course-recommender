from fastapi import APIRouter
from sqlmodel import SQLModel

class DataRequest(SQLModel):
    a: int
    b: str
    c: str

class DataResponse(SQLModel):
    test: int

router = APIRouter(
    prefix='/test',
    tags=['test'],
    responses={404: {'description': 'not found'}},
)

@router.post('/', response_model=DataResponse)
async def post_test(data: DataRequest):
    dataResponse = DataResponse(test=0)

    dataResponse.test = data.a * 1000

    return dataResponse