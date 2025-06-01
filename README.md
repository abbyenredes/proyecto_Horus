# Proyecto HORUS

HORUS es una solución basada en la API de Telefónica Device Location para el análisis geoespacial de la densidad poblacional. El objetivo es permitir la trazabilidad anónima de dispositivos móviles para generar información valiosa para estrategias de marketing físico y análisis urbano.

## 🚀 Demo
Explora nuestra demo presentada en el Summer Hackaton 42Madrid:  
[Acceder a la demo](https://drive.google.com/drive/folders/1h0FwokB2KU1KGUXam1i67ffrET06QJg3?usp=sharing)

---

## 🧠 Idea Principal

HORUS permite analizar mapas urbanos para identificar zonas de alta concentración de usuarios, utilizando información anónima proveniente de dispositivos móviles. El sistema ofrece:

- Análisis demográfico (edad, sexo, hora del día).
- Visualización en mapas de calor.
- Herramienta de filtrado temporal y espacial.

## 🔧 Tecnologías Usadas

- **Telefónica Device Location API**: Para obtención de coordenadas geográficas anónimas.
- **MongoDB**: Base de datos NoSQL para almacenar la información de ubicación.
- **PyMongo**: Interfaz entre Python y MongoDB.
- **FastAPI**: Backend para gestionar peticiones HTTP y lógica de negocio.
- **Folium + HeatMap Plugin**: Visualización interactiva en mapas de calor.

---

## 🏗️ Arquitectura del Sistema

```
Nivel 1: Fuente de Datos
└── Telefónica Device Location API

Nivel 2: Almacenamiento de Datos
└── MongoDB + PyMongo

Nivel 3: Backend / Procesamiento
└── FastAPI + NumPy

Nivel 4: Visualización
└── Folium + HeatMap
```

## ⚙️ Funcionamiento

1. Se recogen datos de ubicación de dispositivos móviles (previo consentimiento del usuario).
2. La información es almacenada en MongoDB.
3. FastAPI procesa y filtra los datos según parámetros definidos.
4. La información procesada se visualiza mediante mapas de calor.

---

## 🌍 Aplicaciones

- Análisis de flujos de personas en zonas urbanas.
- Estrategias de marketing geolocalizado.
- Optimización de publicidad física (carteles, tiendas, eventos).

## 📌 Equipo

**Número de equipo**: 19  
**Nombre del proyecto**: HORUS

---

## 📄 Licencia

Este proyecto se presenta como parte de una iniciativa académica. Para usos comerciales, por favor contacta al equipo desarrollador.
