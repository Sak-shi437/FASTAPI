from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Optional
import json


app = FastAPI()

class Patient(BaseModel):

    id: Annotated[str, Field(..., description='ID of the patient', examples=['P001'])]
    name: Annotated[str, Field(..., description='Name of the patient')]
    city: Annotated[str, Field(..., description='City where the patient is living')]
    age: Annotated[int, Field(..., gt=0, lt=120, description='Age of the patient')]
    gender: Annotated[Literal['male', 'female', 'others'], Field(..., description='Gender of the patient')]
    height: Annotated[float, Field(..., gt=0, description='Height of the patient in mtrs')]
    weight: Annotated[float, Field(..., gt=0, description='Weight of the patient in kgs')]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi

    @computed_field
    @property
    def verdict(self) -> str:

        if self.bmi < 18.5:
            return 'Underweight'
        elif self.bmi < 25:
            return 'Normal'
        elif self.bmi < 30:
            return 'Normal'
        else:
            return 'obese'

        class PatientUpdate(BaseModel):
            name: Annotated[optional[str], Field(default=None)]
            city: Annotated[optional[str], Field(default=None)]
            age: Annotated[optional[int], Field(default=None, gt=0)]
            gender: Annotated[optional[Literal['male','female']],Field(default=None)]
            height: Annotated[optional[float], Field(default=None, gt=0)]
            weight: Annotated[optional[float], Field(default=None, gt=0)]


        def load_data():
            with open('patient.json','r') as f:
                data = json.load(f)

            return data

        @app.get("/")

        def hello():
            return {'message':'Patient Management System API'}

        @app.get('/about')
        def about():
            return {'messgae': 'Afully functional API to manage your patient record'}

        @app.get('/view')
        def view():
            data = load_data()

            if patient_id in data:
                return data[patient_id]
            raise HTTPexception(status_code=404, detail='Patient not found')

        
        
        
        
        
        
        