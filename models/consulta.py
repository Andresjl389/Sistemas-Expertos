from typing import TYPE_CHECKING
import uuid
from sqlalchemy import Column, Date, String, Uuid, ForeignKey
from sqlalchemy.orm import relationship
from core.db import Base
import datetime
    

class Consulta(Base):
    __tablename__ = "consulta"

    id = Column(Uuid, primary_key=True, index=True, nullable=False, default=uuid.uuid4)
    fecha = Column(Date, nullable=False, default=datetime.date.today())
    razon = Column(String, index=True, nullable=False)

    usuario_id = Column(Uuid, ForeignKey("usuario.id"))

    usuario = relationship("Usuario", back_populates="consulta")
    resultado = relationship('Resultado', back_populates='consulta')

