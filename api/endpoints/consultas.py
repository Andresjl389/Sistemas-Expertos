from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from core.security import get_current_user
from expert_system.engine import evaluar_ruta
from schemas.consultas import ConsultasPost
from schemas.sintomas import SintomasInput
from schemas.user_schema import Token, UserCreate, UserLogin
from core.db import get_db
from sqlalchemy.orm import Session
from services.consultas import create_consultation
from services.user_service import create_user, login_user
from models.sintomas import Sintoma
from models.sintoma_enfermedad import SintomaEnfermedad
from models.enfermedad import Enfermedad
from collections import defaultdict


consulta_router = APIRouter(tags=['Consultas'])

class Respuesta(BaseModel):
    sintoma_id: str
    respuesta: bool

user_session = {}

@consulta_router.get('/consultas')
def get_consultas(current_user: str = Depends(get_current_user)):
    return {'message': current_user}


@consulta_router.post('/consultas')
def get_consultas(
    consulta: ConsultasPost,
    current_user: str = Depends(get_current_user), 
    db: Session = Depends(get_db)
    ):
    return JSONResponse(content=jsonable_encoder({'consulta':create_consultation(db, current_user, consulta)}))


# @consulta_router.post("/diagnostico/{ruta}")
# def evaluar_sintomas(ruta: str, sintomas: SintomasInput):
#     # Aquí puedes hacer lógica con ruta_dificultad_respirar(datos), etc.
#     respuestas = sintomas.model_dump(exclude_none=True)
#     resultado = evaluar_ruta(ruta, respuestas)
#     return {"respuesta":resultado}