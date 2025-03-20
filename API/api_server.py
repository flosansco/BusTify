from fastapi import FastAPI
from Simulation.SimulationRequest import SimulationRequest
from fastapi.middleware.cors import CORSMiddleware


# Création de l'application FastAPI
app = FastAPI()

# Autoriser le frontend (CORS pour éviter les erreurs de connexion)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permet à tous les domaines d'accéder à l'API (à restreindre en prod)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Endpoint pour la simulation
@app.post("/simulate")
def simulate(data: SimulationRequest):

    # Ici remplacer par des fonctions à dfinir qui vont faire les calculs
    # Quelque chose comme :
        # calculs = Calculs(inputs)
        # calculs.process()

    # Simulation simple de température de batterie
    if data.type_refroidissement == "air":
        temperature_batterie = data.temperature_ext + 5
    elif data.type_refroidissement == "liquide":
        temperature_batterie = data.temperature_ext + 3
    else:
        temperature_batterie = data.temperature_ext + 1  # CPM plus efficace

    return {"temperature_batterie": temperature_batterie}

# Lancer le serveur avec : uvicorn api_server:app --reload
