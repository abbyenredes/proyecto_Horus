# validar datos y guardar en MongoDB
from pydantic import BaseModel
from datetime import datetime


# modelado de datos
class Areas_collection(BaseModel):
    id: str
    city: str
    neighborhood: str
    center: list[float]  # Tuple for latitude and longitude
    radius_meters: int 
    

class Subarea_collection(BaseModel):
    id: str
    area_id: str
    layer: int
    latitud: float
    name: str
    center: list[float]  # Tuple for latitude and longitude
    radio_meters: int 
  
class  user_area_visits_collection(BaseModel):
    id: str
    user_id: str
    time_lacation: int = int( datetime.timestamp(datetime.now()))
    city: str
    neighborhood: str
    was_present: bool
    age: int
    gender: bool
    # Optional fields, one for each layer/ por si son necesarios dejo en comentario
    # layer_1: str
    # layer_2: str
    