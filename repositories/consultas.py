from sqlalchemy.orm import Session
from models.consulta import Consulta
from models.user import Usuario
from schemas.user_schema import UserCreate
from core.security import get_password_hash


def insert_one(db: Session, consulta: Consulta):
    db.add(consulta)
    db.commit()
    db.refresh(consulta)
    return consulta