import uuid
from sqlalchemy import Column, Date, String, Uuid, ForeignKey
from sqlalchemy.orm import relationship
from core.db import Base
import datetime


class SintomasConsulta(Base):
    __tablename__ = "sintomas_consulta"

    id = Column(Uuid, primary_key=True, index=True, nullable=False, default=uuid.uuid4)
    resultado_id = Column(Uuid, ForeignKey("resultado.id"))
    sintoma_id = Column(Uuid, ForeignKey("sintoma.id"))


    sintoma = relationship('Sintoma', back_populates='sintomas_consulta')
    resultado = relationship('Resultado', back_populates='sintomas_consulta')
