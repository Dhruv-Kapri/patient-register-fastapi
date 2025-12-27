from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from app.utils.data import load_data, save_data

router = APIRouter(
    prefix='/delete',
    tags=['Patients']
)


@router.delete('/{patient_id}')
def delete_patient(patient_id: str):
    data = load_data()
    if patient_id not in data:
        raise HTTPException(status_code=404, detail='Patient not found')

    del data[patient_id]
    save_data(data)

    return JSONResponse(status_code=200, content={'message': 'patient deleted'})
