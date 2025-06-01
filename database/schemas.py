# esquemas de datos para la base de datos

def get_district_center(Areas_collection):
    return {
        "id": 1,
        "name": "Distrito Centro",
        "city": "Madrid",
        "neighborhood": "Centro",
        "latitude": 40.4168,
        "longitude": -3.7038,
        "radius_meters": 1000,
        "status": "activo"
    }   
    
def get_district_subareas(Subarea_collection):
    return [
        {
            "id": 1,
            "area_id": "1",
            "layer": 1,
            "latitud": 40.4168,
            "name": "Subarea Centro",
            "latitude": 40.4168,
            "longitude": -3.7038,
            "radio_meters": 500
        },
        {
            "id": 2,
            "area_id": "1",
            "layer": 2,
            "latitud": 40.4170,
            "name": "Subarea Malasaña",
            "latitude": 40.4170,
            "longitude": -3.7040,
            "radio_meters": 300
        }
    ]

def get_user_area_visits(user_area_visits_collection):
    return [
        {
            "id": "1",
            "user_id": "user123",
            "time_location": 1700000000,
            "neighborhood": "Centro",
            "was_present": True
        },
        {
            "id": "2",
            "user_id": "user456",
            "time_location": 1700000100,
            "neighborhood": "Malasaña",
            "was_present": False
        }
    ]
    
def all_user_area_visits(user_area_visits_collection):
    return [get_user_area_visits(user_area_visits_collection) for user_area_visits_collection in user_area_visits_collection]