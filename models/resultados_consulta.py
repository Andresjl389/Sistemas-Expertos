import uuid
from sqlalchemy import Column, Date, String, Uuid, ForeignKey
from sqlalchemy.orm import relationship
from core.db import Base
import datetime


class Resultado(Base):
    __tablename__ = "resultado"

    id = Column(Uuid, primary_key=True, index=True, nullable=False, default=uuid.uuid4)
    diagnostico_final = Column(String, index=True, nullable=False)

    consulta_id = Column(Uuid, ForeignKey("consulta.id"))

    consulta = relationship('Consulta', back_populates='resultado')
    sintomas_consulta = relationship('SintomasConsulta', back_populates='resultado')
