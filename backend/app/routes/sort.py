from fastapi import APIRouter, Query, HTTPException
from app.utils.data import load_data

router = APIRouter(
    prefix='/sort',
    tags=['Patients']
)


@router.get('/')
def sort_patients(
    sort_by: str = Query(...,
                         description='Sort on the basis of height, weight or bmi',
                         example='height'),
    order: str = Query('asc', description='ort in asc or desc order')
):
    valid_fields = ['height', 'weight', 'bmi']

    if sort_by not in valid_fields:
        HTTPException(status_code=401,
                      detail=f'Invalid field. Select from {valid_fields}')
    if order not in ['asc', 'desc']:
        HTTPException(status_code=401,
                      detail=f'Invalid field. Select between asc and desc')

    data = load_data()

    sort_order = True if order == 'desc' else False

    sorted_data = sorted(data.values(), key=lambda x: x.get(
        sort_by, 0), reverse=sort_order)
    return sorted_data
