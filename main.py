from fastapi import FastAPI, HTTPException
from modelos import Paciente, Cita
import servicios

app = FastAPI()

@app.get("/")
def home():
    return {"mensaje": "Reservas de Citas Médicas API funcionando"}

@app.post("/pacientes")
def api_crear_paciente(paciente: Paciente):
    return servicios.crear_paciente(paciente)

@app.post("/citas")
def api_crear_cita(cita: Cita):

    creada = servicios.crear_cita(cita)
    if creada is None:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")

    return creada

@app.get("/citas/{cita_id}")
def api_get_cita(cita_id: int):
    cita = servicios.get_cita_by_id(cita_id)
    if cita is None:
        raise HTTPException(status_code=404, detail="Cita no encontrada")
    return cita