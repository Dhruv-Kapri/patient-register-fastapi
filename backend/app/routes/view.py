from fastapi import APIRouter
from app.utils.data import load_data

router = APIRouter(
    prefix='/view',
    tags=['Patients']
)


@router.get('/')
def view():
    data = load_data()
    return data
