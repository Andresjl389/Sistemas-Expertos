from fastapi import APIRouter, Depends, HTTPException
from schemas.user_schema import Token, UserCreate, UserLogin
from core.db import get_db
from sqlalchemy.orm import Session
from services.user_service import create_user, login_user


user_router = APIRouter()


@user_router.post("/users", response_model=UserCreate, status_code=201, tags=['Auth'])
async def register_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        return await create_user(db, user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@user_router.post('/login', response_model=Token, tags=['Auth'])
def login(user: UserLogin, db: Session = Depends(get_db)):
    return login_user(db, user)