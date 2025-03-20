from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from Simulation.SimulationRequest import SimulationRequest
from LoggerManager.Logger import log


class Simulation:
    def __init__(self):
        self.app = FastAPI()
        self.setup_routes()

        self.app.add_middleware(
            CORSMiddleware,  # ignore warning
            allow_origins=["*"],  # Permet à tous les domaines d'accéder à l'API (à restreindre en prod)
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],)

    def setup_routes(self):
        self.app.post("/simulate")(self.simulate)

    @staticmethod
    async def simulate(data: SimulationRequest):
        try:
            result_message = f"Simulation réussie pour {data.passengers} passagers avec {data.temperature}°C et {data.humidity}% d'humidité."
            return {"message": result_message}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    async def save_scenario(scenario):
        log.i("Saving scenario <id> with params <params>")

    @staticmethod
    async def more_functions_here():
        log.d("You can add more functions here")


# Point d'entrée pour Uvicorn
# Lancer le serveur avec : uvicorn api_server:app --reload
log.i("Please launch simulation with `uvicorn api_server:app --reload`")
simulation = Simulation()
app = simulation.app
