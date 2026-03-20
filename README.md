#  Cita.me - Sistema de Agendamiento de Citas Médicas

Sistema distribuido para la gestión de reservas de citas médicas, desarrollado como proyecto académico para las asignaturas de **Sistemas Distribuidos (SSDD)** y **Programación Distribuida (PD)**. Implementa una API REST con Python y FastAPI, siguiendo una arquitectura cliente-servidor con servicios especializados.

##  Tabla de Contenidos
- [Características](#características)
- [Tecnologías Utilizadas](#tecnologías-utilizadas)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Requisitos Previos](#requisitos-previos)
- [Instalación y Ejecución](#instalación-y-ejecución)
- [Endpoints de la API](#endpoints-de-la-api)
- [Autores](#autores)
- [Licencia](#licencia)

---

## ✨ Características

- ✅ **Creación de pacientes** (`POST /pacientes`)
- ✅ **Agendamiento de citas** (`POST /citas`)
- ✅ **Consulta de citas por ID** (`GET /citas/{id}`)
- ✅ Validación de datos con **Pydantic**
- ✅ Documentación interactiva automática con **Swagger UI**
- ✅ Arquitectura modular (API, Servicios, Modelos)
- ✅ Persistencia en memoria (listas de Python)

##  Tecnologías Utilizadas

| Tecnología | Propósito |
|------------|-----------|
| **Python 3.10+** | Lenguaje de programación principal |
| **FastAPI** | Framework web para construir la API |
| **Pydantic** | Validación y serialización de datos |
| **Uvicorn** | Servidor ASGI para ejecutar FastAPI |
| **Git** | Control de versiones |

##  Estructura del Proyecto
Cita.me/
├── main.py # Endpoints de la API y configuración de FastAPI
├── modelos.py # Modelos de datos con Pydantic
├── servicios.py # Lógica de negocio y almacenamiento en memoria
├── requirements.txt # Dependencias del proyecto
├── .gitignore # Archivos ignorados por Git
└── README.md # Documentación del proyecto

##  Requisitos Previos

- Python 3.10 o superior instalado
- `pip` (gestor de paquetes de Python)
- (Opcional) `virtualenv` o `venv` para entorno virtual

##  Instalación y Ejecución

### 1. Clonar el repositorio
```bash
git clone https://github.com/MLopezCamp/Cita.me.git
cd Cita.me
2. Crear y activar entorno virtual
bash
# En Linux/Mac
python -m venv venv
source venv/bin/activate

# En Windows
python -m venv venv
venv\Scripts\activate
3. Instalar dependencias
bash
pip install -r requirements.txt
4. Ejecutar el servidor
bash
uvicorn main:app --reload
El servidor se iniciará en http://localhost:8000

 - Endpoints de la API
Método	Endpoint	Descripción	Cuerpo de Ejemplo
POST	/pacientes	Registra un nuevo paciente	{"nombre": "Juan Pérez", "documento": "12345678"}
POST	/citas	Agenda una nueva cita	{"paciente_id": 1, "fecha": "2025-04-15 10:30", "motivo": "Consulta general"}
GET	/citas/{id}	Obtiene los detalles de una cita específica	Parámetro en URL
GET	/pacientes	Lista todos los pacientes	-
GET	/pacientes/{id}	Obtiene un paciente por ID	-
GET	/citas	Lista todas las citas	-
GET	/	Mensaje de bienvenida	-
- Nota sobre validación
Al crear una cita, el sistema verifica que el paciente_id exista antes de agendar.

Si el paciente no existe, se retorna un error 400 (Bad Request).

Los datos se almacenan en memoria mientras el servidor está activo.

- Autores
- Mauriciol López - @MLopezCamp
- Rooger Andres Gomez - @Ragomez333


Proyecto desarrollado como parte del curso de Sistemas Distribuidos y Programación Distribuida.

- Licencia
Este proyecto está bajo la Licencia MIT - consulta el archivo LICENSE para más detalles.