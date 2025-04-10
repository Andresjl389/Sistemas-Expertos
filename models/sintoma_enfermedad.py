import uuid
from sqlalchemy import Column, Date, String, Uuid, ForeignKey
from sqlalchemy.orm import relationship
from core.db import Base
import datetime


class SintomaEnfermedad(Base):
    __tablename__ = "sintomas_enfermedad"

    id = Column(Uuid, primary_key=True, index=True, nullable=False, default=uuid.uuid4)
    sintoma_id = Column(Uuid, ForeignKey("sintoma.id"))
    enfermedad_id = Column(Uuid, ForeignKey("enfermedad.id"))


    enfermedad = relationship('Enfermedad', back_populates='sintomas_enfermedad')
    sintoma = relationship('Sintoma', back_populates='sintomas_enfermedad')
