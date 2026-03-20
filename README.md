# Cita.me - Sistema de Agendamiento de Citas Médicas

Sistema distribuido para la gestión de reservas de citas médicas, desarrollado como proyecto académico para las asignaturas de Sistemas Distribuidos (SSDD) y Programación Distribuida (PD).

Implementa una API REST con Python y FastAPI, siguiendo una arquitectura cliente-servidor con servicios especializados.

---

## Tabla de Contenidos

- Características
- Tecnologías Utilizadas
- Estructura del Proyecto
- Requisitos Previos
- Instalación y Ejecución
- Endpoints de la API
- Validación
- Autores
- Licencia

---

## Características

- Creación de pacientes (`POST /pacientes`)
- Agendamiento de citas (`POST /citas`)
- Consulta de citas por ID (`GET /citas/{id}`)
- Validación de datos con Pydantic
- Documentación interactiva automática con Swagger UI
- Arquitectura modular (API, servicios, modelos)
- Persistencia en memoria (listas de Python)

---

## Tecnologías Utilizadas

| Tecnología   | Propósito                                      |
|--------------|-----------------------------------------------|
| Python 3.10+ | Lenguaje de programación principal            |
| FastAPI      | Framework web para construir la API           |
| Pydantic     | Validación y serialización de datos           |
| Uvicorn      | Servidor ASGI para ejecutar FastAPI           |
| Git          | Control de versiones                         |

---

## Estructura del Proyecto

Cita.me/
├── main.py
├── modelos.py
├── servicios.py
├── requirements.txt
├── .gitignore
└── README.md

---

## Requisitos Previos

- Python 3.10 o superior
- pip
- (Opcional) virtualenv o venv

---

## Instalación y Ejecución

### 1. Clonar el repositorio

git clone https://github.com/MLopezCamp/Cita.me.git  
cd Cita.me  

### 2. Crear entorno virtual

python -m venv venv  

Linux/Mac:
source venv/bin/activate  

Windows:
venv\Scripts\activate  

### 3. Ejecutar servidor

uvicorn main:app --reload  

http://localhost:8000

---

## Endpoints

POST /pacientes  
POST /citas  
GET /citas/{id}  
GET /pacientes  
GET /pacientes/{id}  
GET /citas  
GET /

---

## Validación

- Se valida que el paciente exista
- Error 400 si no existe
- Datos en memoria

---

## Autores

- Mauriciol López - @MLopezCamp
- Rooger Andres Gomez - @Ragomez333

---

## Licencia

Licencia MIT