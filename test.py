import folium
from folium.plugins import HeatMap
import numpy as np

# Coordenadas centrales de Madrid
madrid_coords = [40.4068, -3.7038]

# Número de puntos por mapa
num_points = 300

# Cantidad de mapas a generar
total_maps = 5

for i in range(1, total_maps + 1):
    # Fijar una semilla diferente para cada mapa
    np.random.seed(i * 42)

    # Generar coordenadas alrededor de Madrid
    lats = np.random.normal(madrid_coords[0], 0.05, num_points)
    lons = np.random.normal(madrid_coords[1], 0.05, num_points)
    weights = np.random.randint(1, 10, num_points)  # Peso opcional

    # Combinar los datos en formato [[lat, lon, peso]]
    data = [[float(lat), float(lon), int(weight)] for lat, lon, weight in zip(lats, lons, weights)]

    # Crear mapa base
    m = folium.Map(location=madrid_coords, zoom_start=12)

    # Añadir mapa de calor
    HeatMap(data).add_to(m)

    # Guardar mapa con nombre único
    filename = f"mapa_calor_{i}.html"
    m.save(filename)
    print(f"✅ Mapa {i} guardado como '{filename}'")