from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Optional


class Patient(BaseModel):

    id: Annotated[str,
                  Field(..., description='Patient id', examples=['P001'])]
    name: Annotated[str, Field(..., description='Name of the patient')]
    city: Annotated[str,
                    Field(..., description='City where the patient is living')]
    age: Annotated[int, Field(..., ge=0, lt=120,
                              description='Age of the patient')]
    gender: Annotated[Literal['male', 'female', 'do not say'],
                      Field(..., description='Gender of the patient')]
    height: Annotated[float,
                      Field(..., gt=0, description='Height of the patient in mtrs')]
    weight: Annotated[float,
                      Field(..., gt=0, description='Weight of the patient in kgs')]

    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight / (self.height**2))


class PatientUpdate(BaseModel):
    name: Annotated[Optional[str], Field(
        default=None, description='Name of the patient')]
    city: Annotated[Optional[str],
                    Field(default=None, description='City where the patient is living')]
    age: Annotated[Optional[int], Field(default=None, ge=0, lt=120,
                                        description='Age of the patient')]
    gender: Annotated[Optional[Literal['male', 'female', 'do not say']],
                      Field(default=None, description='Gender of the patient')]
    height: Annotated[Optional[float],
                      Field(default=None, gt=0, description='Height of the patient in mtrs')]
    weight: Annotated[Optional[float],
                      Field(default=None, gt=0, description='Weight of the patient in kgs')]
