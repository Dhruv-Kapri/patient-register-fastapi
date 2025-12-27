from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from app.schemas.patient_schema import Patient
from app.utils.data import load_data, save_data

router = APIRouter(
    prefix='/create',
    tags=['Patients']
)


@router.post('/')
def create_patient(patient: Patient):

    data = load_data()

    if patient.id in data:
        raise HTTPException(status_code=400, detail='Patient already exists')

    data[patient.id] = patient.model_dump(exclude='id')
    save_data(data)

    return JSONResponse(status_code=200, content={'message': 'Patient Created'})


# {"id": "P010", "name": "Ananya Verma", "city": "Guwahati", "age": 28, "gender": "female", "height": 1.65, "weight": 90.0}
