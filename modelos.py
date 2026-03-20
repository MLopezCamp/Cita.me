from pydantic import BaseModel

# Modelos para entrada de datos (sin ID)
class PacienteCreate(BaseModel):
    nombre: str
    documento: str

class CitaCreate(BaseModel):
    paciente_id: int
    fecha: str
    motivo: str

# Modelos para respuesta (con ID)
class Paciente(PacienteCreate):
    id: int

class Cita(CitaCreate):
    id: int