from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.db import get_db
from models.sintomas import Sintoma
from models.sintoma_enfermedad import SintomaEnfermedad
from models.enfermedad import Enfermedad
from utils.sesion import get_sesion, reset_sesion
from pydantic import BaseModel
from typing import Optional
import uuid

diagnostico_router = APIRouter(tags=['Diagnostico'])

class Respuesta(BaseModel):
    usuario_id: str
    sintoma_id: str
    respuesta: bool

@diagnostico_router.get("/diagnostico/pregunta_siguiente")
def pregunta_siguiente(usuario_id: str, db: Session = Depends(get_db)):
    sesion = get_sesion(usuario_id)
    sintomas = db.query(Sintoma).all()
    for sintoma in sintomas:
        if str(sintoma.id) not in sesion["preguntados"]:
            return {"sintoma_id": str(sintoma.id), "pregunta": f"¿Presentas {sintoma.nombre}?"}
    return {"mensaje": "Todas las preguntas respondidas. Usa /diagnostico/resultado para ver el resultado."}

@diagnostico_router.post("/diagnostico/responder")
def responder(respuesta: Respuesta, db: Session = Depends(get_db)):
    sesion = get_sesion(respuesta.usuario_id)
    sesion["preguntados"].add(respuesta.sintoma_id)
    if respuesta.respuesta:
        asociaciones = db.query(SintomaEnfermedad).filter_by(sintoma_id=respuesta.sintoma_id).all()
        for a in asociaciones:
            sesion["puntuacion"][str(a.enfermedad_id)] += 1
    return {"mensaje": "Respuesta guardada. Usa /diagnostico/pregunta_siguiente para continuar."}

@diagnostico_router.get("/diagnostico/resultado")
def resultado(usuario_id: str, db: Session = Depends(get_db)):
    sesion = get_sesion(usuario_id)
    puntuacion = sesion["puntuacion"]
    if not puntuacion:
        return {"mensaje": "No se han registrado respuestas."}
    enfermedades = db.query(Enfermedad).filter(Enfermedad.id.in_(puntuacion.keys())).all()
    resultados = []
    for e in enfermedades:
        resultados.append({
            "enfermedad": e.nombre,
            "descripcion": e.descripcion,
            "puntos": puntuacion[str(e.id)]
        })
    top = sorted(resultados, key=lambda x: x['puntos'], reverse=True)[:5]
    return {"diagnostico_top5": top}

@diagnostico_router.post("/diagnostico/reiniciar")
def reiniciar(usuario_id: str):
    reset_sesion(usuario_id)
    return {"mensaje": "Sesión reiniciada."}
