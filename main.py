from fastapi import FastAPI, HTTPException
from typing import List
from modelos import PacienteCreate, CitaCreate, Paciente, Cita
import servicios

app = FastAPI(
    title="Sistema de Reservas de Citas Médicas",
    description="API para gestión de pacientes y citas médicas - Proyecto SSDD/PD",
    version="1.0.0"
)

# --- Endpoints públicos ---
@app.get("/")
def home():
    return {
        "mensaje": "API de Reservas de Citas Médicas para aplicacion Cita.me",
        "documentacion": "/docs",
        "estado": "funcionando"
    }

# --- Endpoints de Pacientes ---
@app.post("/pacientes", 
          response_model=Paciente, 
          status_code=201,
          summary="Crear un nuevo paciente")
def crear_paciente(paciente: PacienteCreate):
    """
    Registra un nuevo paciente en el sistema.
    
    - **nombre**: Nombre completo del paciente
    - **documento**: Número de identificación
    """
    return servicios.crear_paciente(paciente)

@app.get("/pacientes", 
         response_model=List[Paciente],
         summary="Listar todos los pacientes")
def listar_pacientes():
    """Obtiene la lista completa de pacientes registrados."""
    return servicios.listar_pacientes()

@app.get("/pacientes/{paciente_id}", 
         response_model=Paciente,
         summary="Obtener paciente por ID")
def obtener_paciente(paciente_id: int):
    """
    Busca un paciente específico por su ID.
    """
    paciente = servicios.obtener_paciente_por_id(paciente_id)
    if not paciente:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    return paciente

# --- Endpoints de Citas ---
@app.post("/citas", 
          response_model=Cita, 
          status_code=201,
          summary="Crear una nueva cita")
def crear_cita(cita: CitaCreate):
    """
    Crea una nueva cita médica.
    
    - **paciente_id**: ID del paciente existente
    - **fecha**: Fecha y hora de la cita (formato: YYYY-MM-DD HH:MM)
    - **motivo**: Razón de la consulta
    """
    nueva_cita = servicios.crear_cita(cita)
    if not nueva_cita:
        raise HTTPException(
            status_code=400, 
            detail="No se puede crear la cita: el paciente no existe"
        )
    return nueva_cita

@app.get("/citas", 
         response_model=List[Cita],
         summary="Listar todas las citas")
def listar_citas():
    """Obtiene la lista completa de citas agendadas."""
    return servicios.listar_citas()

@app.get("/citas/{cita_id}", 
         response_model=Cita,
         summary="Obtener cita por ID")
def obtener_cita(cita_id: int):
    """
    Busca una cita específica por su ID.
    """
    cita = servicios.obtener_cita_por_id(cita_id)
    if not cita:
        raise HTTPException(status_code=404, detail="Cita no encontrada")
    return cita