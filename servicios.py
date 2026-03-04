from typing import List
from modelos import Paciente, Cita

# Base de datos en memoria
pacientes = []
citas = []

# Funciones de servicio

def crear_paciente(paciente: Paciente):
    nuevo = {
        "id": len(pacientes) + 1,
        "nombre": paciente.nombre,
        "documento": paciente.documento
    }
    pacientes.append(nuevo)
    return nuevo


def crear_cita(cita: Cita):
    # Verificar que el paciente exista
    paciente = next((p for p in pacientes if p["id"] == cita.paciente_id), None)
    if paciente is None:
        return None

    nueva = {
        "id": len(citas) + 1,
        "paciente_id": cita.paciente_id,
        "fecha": cita.fecha,
        "motivo": cita.motivo
    }
    citas.append(nueva)
    return nueva


def get_cita_by_id(cita_id: int):
    return next((c for c in citas if c["id"] == cita_id), None)