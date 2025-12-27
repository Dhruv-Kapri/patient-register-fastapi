from fastapi import APIRouter

router = APIRouter(
    prefix='',
    tags=['General']
)


@router.get("/")
def hello():
    return {'message': 'Patient Management System API'}
