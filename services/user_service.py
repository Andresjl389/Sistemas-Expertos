from datetime import timedelta
from fastapi import HTTPException
from sqlalchemy.orm import Session
from core.security import check_password_hash, create_access_token
from repositories.user_repository import insert_user, get_user_by_email
from schemas.user_schema import UserCreate, UserLogin

def create_user(db: Session, user: UserCreate):
    existing_user = get_user_by_email(db, user.correo)
    if existing_user:
        raise ValueError("El usuario ya existe")
    return insert_user(db, user)


def login_user(db: Session, user_login: UserLogin):
    user = get_user_by_email(db, user_login.correo)
    if not user or not check_password_hash(user_login.contraseña, user.contraseña):
        raise HTTPException(status_code=401, detail='Correo o contraseña incorrectos')
    
    token = create_access_token(data={'sub':user.correo}, expires_delta=timedelta(minutes=30))
    return {'access_token':token, 'token_type':'bearer'}