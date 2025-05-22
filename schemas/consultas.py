from pydantic import BaseModel, EmailStr

class ConsultaGet(BaseModel):
    id: str
    fecha: str
    usuario_id: str

class ConsultasPost(BaseModel):
    razon: str
    
    
class Token(BaseModel):
    access_token: str
    token_type: str

    class Config:
        from_attributes = True