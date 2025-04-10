import uuid
from sqlalchemy import Column, Date, String, Uuid, ForeignKey
from sqlalchemy.orm import relationship
from core.db import Base
import datetime



class Sintoma(Base):
    __tablename__ = "sintoma"

    id = Column(Uuid, primary_key=True, index=True, nullable=False, default=uuid.uuid4)
    nombre = Column(String, index=True, nullable=False)

    sintomas_consulta = relationship('SintomasConsulta', back_populates='sintoma')
    sintomas_enfermedad = relationship('SintomaEnfermedad', back_populates='sintoma')
