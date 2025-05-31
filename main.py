from fastapi import FastAPI, APIrouter
from fastapi.responses import HTMLResponse

app = FastAPI()
router = APIrouter()

# pagina de inicio
@app.get("/")
async def home():
    return {"message": "Bienvenido a la API de Orus"}
