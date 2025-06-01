from fastapi import FastAPI, APIRouter
from configuration import areas_collection
from database.schemas import get_district_center, get_district_subareas, get_user_area_visits, all_user_area_visits
from database.models import Areas_collection, Subarea_collection, user_area_visits_collection
# --- Imports ---
import configuration
import create_grid
import areas_to_db

app= FastAPI()
router = APIRouter()
@router.get("/")
async def get_all_user_area_visits():
    data = areas_collection.find( )
    return all_user_area_visits(data)

@router.post("/")
async def create_user_area_visit(user_visit: user_area_visits_collection):
    data = areas_collection.insert_one(user_visit.dict())
    return {"id": str(data.inserted_id), "message": "User area visit created successfully"}
