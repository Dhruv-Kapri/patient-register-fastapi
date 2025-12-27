from fastapi import APIRouter, Path, HTTPException
from app.utils.data import load_data

router = APIRouter(
    prefix='/patient',
    tags=['Patients']
)


@router.get('/')
def patient_home():
    return {'message': 'Type patient_id along with the url to view patient information'}


@router.get('/{patient_id}')
def view_patient(patient_id: str = Path(..., description='ID of the patient in the DB', example='P001')):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    else:
        raise HTTPException(status_code=404, detail='Patient not found')
