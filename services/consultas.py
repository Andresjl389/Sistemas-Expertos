from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.consulta import Consulta
from repositories.consultas import insert_one
from repositories.user_repository import get_user_by_email
from schemas.consultas import ConsultasPost


def create_consultation(db: Session, user: str, consulta: ConsultasPost):
    search_user = get_user_by_email(db, user)
    if not search_user:
        raise HTTPException(status_code=401, detail='Usuario invalido')
    
    new_consultation = Consulta(
        razon=consulta.razon,
        usuario_id=search_user.id
    )
    return insert_one(db, new_consultation)
