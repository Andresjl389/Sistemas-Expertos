from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    nombre: str
    correo: EmailStr
    contraseña: str

class UserLogin(BaseModel):
    correo: EmailStr
    contraseña: str
    
class Token(BaseModel):
    access_token: str
    token_type: str

    class Config:
        from_attributes = True