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


@consulta_router.post("/diagnostico/{ruta}")
def evaluar_sintomas(ruta: str, sintomas: SintomasInput):
    # Aquí puedes hacer lógica con ruta_dificultad_respirar(datos), etc.
    respuestas = sintomas.model_dump(exclude_none=True)
    resultado = evaluar_ruta(ruta, respuestas)
    return {"respuesta":resultado}


@consulta_router.get("/pregunta_siguiente")
def obtener_pregunta(db: Session = Depends(get_db)):
    # Obtener síntomas aún no preguntados
    sintomas = db.query(Sintoma).all()
    ya_preguntados = user_session.get("preguntados", set())
    for sintoma in sintomas:
        if str(sintoma.id) not in ya_preguntados:
            return {"sintoma_id": str(sintoma.id), "pregunta": f"¿Presentas {sintoma.nombre}?"}
    return {"mensaje": "Has respondido todas las preguntas. Usa /resultado para ver el diagnóstico."}

@consulta_router.post("/responder")
def registrar_respuesta(respuesta: Respuesta, db: Session = Depends(get_db)):
    # Inicializar estructuras de sesión
    if "puntuacion" not in user_session:
        user_session["puntuacion"] = defaultdict(int)
        user_session["preguntados"] = set()

    user_session["preguntados"].add(respuesta.sintoma_id)

    if respuesta.respuesta:
        # Obtener enfermedades asociadas a este síntoma
        asociaciones = db.query(SintomaEnfermedad).filter_by(sintoma_id=respuesta.sintoma_id).all()
        for asociacion in asociaciones:
            user_session["puntuacion"][str(asociacion.enfermedad_id)] += 1

    return {"mensaje": "Respuesta registrada. Usa /pregunta_siguiente para continuar."}

@consulta_router.get("/resultado")
def obtener_resultado(db: Session = Depends(get_db)):
    puntuacion = user_session.get("puntuacion", {})
    if not puntuacion:
        return {"mensaje": "No hay respuestas registradas."}

    # Obtener nombres de enfermedades
    enfermedades = db.query(Enfermedad).filter(Enfermedad.id.in_(puntuacion.keys())).all()
    resultados = []
    for enfermedad in enfermedades:
        resultados.append({
            "enfermedad": enfermedad.nombre,
            "descripcion": enfermedad.descripcion,
            "puntos": puntuacion[str(enfermedad.id)]
        })

    # Ordenar por puntos y devolver top 5
    resultados = sorted(resultados, key=lambda x: x['puntos'], reverse=True)[:5]
    return {"diagnosticos_probables": resultados}