import uuid
from sqlalchemy import Column, Integer, String, Uuid
from sqlalchemy.orm import relationship
from core.db import Base


from models.consulta import Consulta
from models.enfermedad import Enfermedad
from models.resultados_consulta import Resultado
from models.sintoma_enfermedad import SintomaEnfermedad
from models.sintomas import Sintoma
from models.sintomas_consulta import SintomasConsulta 

class Usuario(Base):
    __tablename__ = "usuario"

    id = Column(Uuid, primary_key=True, index=True, nullable=False, default=uuid.uuid4)
    nombre = Column(String, index=True, nullable=False)
    correo = Column(String, unique=True, index=True, nullable=False)
    contraseña = Column(String, nullable=False)

    consulta = relationship('Consulta', back_populates='usuario')