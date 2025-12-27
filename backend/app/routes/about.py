from fastapi import APIRouter

router = APIRouter(
    prefix='/about',
    tags=['General']
)


@router.get('/')
def about():
    return {'message': 'A fully functional API to manage your patient records'}
