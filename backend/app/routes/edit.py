from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from app.utils.data import load_data, save_data
from app.schemas.patient_schema import Patient, PatientUpdate

router = APIRouter(
    prefix='/edit',
    tags=['Patients']
)


@router.put('/{patient_id}')
def update_patient(patient_id: str, patient_update: PatientUpdate):

    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail='Patient id not found')

    existing_patient_info = data[patient_id]
    updated_patient_info = patient_update.model_dump(exclude_unset=True)

    for key, value in updated_patient_info.items():
        existing_patient_info[key] = value

    # existing_patient_info -> pydantic object -> updated bmi + verdict
    existing_patient_info['id'] = patient_id
    patient_pydantic_object = Patient(**existing_patient_info)

    # -> pydantic object -> dict
    existing_patient_info = patient_pydantic_object.model_dump(exclude='id')

    # add this dict to data
    data[patient_id] = existing_patient_info

    save_data(data)

    return JSONResponse(status_code=200, content={'message': 'Patient details changed'})
