import uuid
from sqlalchemy import Column, Date, String, Uuid, ForeignKey
from sqlalchemy.orm import relationship
from core.db import Base
import datetime

class Enfermedad(Base):
    __tablename__ = "enfermedad"

    id = Column(Uuid, primary_key=True, index=True, nullable=False, default=uuid.uuid4)
    nombre = Column(String, index=True, nullable=False)
    descripcion = Column(String, index=True, nullable=False)


    sintomas_enfermedad = relationship('SintomaEnfermedad', back_populates='enfermedad')
