from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# --- Configuración de CORS (Cross-Origin Resource Sharing) ---
origins = [
    "http://localhost:64223",
    "http://localhost:3000",
    "http://localhost:8080",
    "http://127.0.0.1:61641",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:8080",
    "http://localhost:5000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,          # Permite las solicitudes de estos orígenes específicos
    allow_credentials=True,         # Permite credenciales (cookies, encabezados de autorización)
    allow_methods=["*"],            # Permite todos los métodos HTTP (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],            # Permite todos los encabezados en la solicitud
)

# --- Definición de Modelos de Datos ---
class MessageResponse(BaseModel):
    message: str

class NameRequest(BaseModel):
    name: str

# --- Endpoints ---
@app.get("/hello", response_model=MessageResponse)
async def read_hello():
    """
    Este endpoint devuelve un mensaje simple.
    """
    return {"message": "FUNCIONA"}

@app.post("/greet", response_model=MessageResponse)
async def greet_user(request_data: NameRequest):
    """
    Este endpoint recibe un nombre en el cuerpo de la solicitud JSON y devuelve un saludo personalizado.
    FastAPI valida automáticamente el 'request_data' usando el modelo 'NameRequest'.
    """
    name = request_data.name
    if not name:
        raise HTTPException(status_code=400, detail="El nombre es requerido.")
    return {"message": f"FUNCIONA, {name}! FUNCIONA JAJA."}

# --- Ejecución del Servidor FastAPI ---
if __name__ == "__main__":
    import uvicorn
    # uvicorn.run(): Inicia el servidor ASGI.
    # "main:app": Le dice a uvicorn que busque la instancia 'app' en el archivo 'main.py'.
    # --host 0.0.0.0: Permite que el servidor sea accesible desde cualquier dirección IP
    # --port 5000: Define el puerto en el que escuchará el servidor.
    # --reload: Recarga el servidor automáticamente cuando detecta cambios en el código.
    uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True)