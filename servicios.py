from typing import List, Optional
from modelos import PacienteCreate, Paciente, CitaCreate, Cita

# Bases de datos en memoria
pacientes_db: List[Paciente] = []
citas_db: List[Cita] = []
contador_pacientes = 1
contador_citas = 1

def crear_paciente(paciente_data: PacienteCreate) -> Paciente:
    """Crea un nuevo paciente y lo almacena."""
    global contador_pacientes
    nuevo_paciente = Paciente(
        id=contador_pacientes,
        nombre=paciente_data.nombre,
        documento=paciente_data.documento
    )
    pacientes_db.append(nuevo_paciente)
    contador_pacientes += 1
    return nuevo_paciente

def crear_cita(cita_data: CitaCreate) -> Optional[Cita]:
    """Crea una nueva cita si el paciente existe."""
    global contador_citas
    
    # Verificar que el paciente exista
    paciente_existe = any(p.id == cita_data.paciente_id for p in pacientes_db)
    if not paciente_existe:
        return None
    
    nueva_cita = Cita(
        id=contador_citas,
        paciente_id=cita_data.paciente_id,
        fecha=cita_data.fecha,
        motivo=cita_data.motivo
    )
    citas_db.append(nueva_cita)
    contador_citas += 1
    return nueva_cita

def obtener_cita_por_id(cita_id: int) -> Optional[Cita]:
    """Busca una cita por su ID."""
    for cita in citas_db:
        if cita.id == cita_id:
            return cita
    return None

# Funciones adicionales
def listar_pacientes() -> List[Paciente]:
    """Retorna todos los pacientes."""
    return pacientes_db

def listar_citas() -> List[Cita]:
    """Retorna todas las citas."""
    return citas_db

def obtener_paciente_por_id(paciente_id: int) -> Optional[Paciente]:
    """Busca un paciente por su ID."""
    for paciente in pacientes_db:
        if paciente.id == paciente_id:
            return paciente
    return None