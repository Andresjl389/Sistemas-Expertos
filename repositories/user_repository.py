from sqlalchemy.orm import Session
from models.user import Usuario
from schemas.user_schema import UserCreate
from core.security import get_password_hash


async def insert_user(db: Session, user: UserCreate):
    hashed_password = get_password_hash(user.contraseña)
    db_user = Usuario(
        nombre=user.nombre, 
        correo=user.correo,
        contraseña=hashed_password
        )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_email(db: Session, email: str):
    return db.query(Usuario).filter(Usuario.correo == email).first()