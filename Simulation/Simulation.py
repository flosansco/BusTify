from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from Simulation.SimulationRequest import SimulationRequest
from LoggerManager.Logger import log


class Simulation:
    def __init__(self):
        self.app = FastAPI()
        self.app.post("/simulate")(self.simulate)

        self.app.add_middleware(
            CORSMiddleware,  # ignore warning
            allow_origins=["*"],  # Permet à tous les domaines d'accéder à l'API (à restreindre en prod)
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],)

    @staticmethod
    async def simulate(request: SimulationRequest):
        """
        Fonction qui sera exécutée via l'appel javascript en cliquant sur un bouton

        :param SimulationRequest request: l'ensemble des données utilisées par le backend qui seront envoyées au frontend
        """
        try:
            log.d("Calcul des consommations")
            # Simuler la consommation (remplacer par une vraie logique plus tard)
            pac_consumption = 20 + request.temperature / 5
            acs_consumption = 15 + request.humidity / 10
            btms_consumption = 10 if request.coolingType == "air" else 5

            total_consumption = pac_consumption + acs_consumption + btms_consumption

            return {
                "pacConsumption": pac_consumption,
                "acsConsumption": acs_consumption,
                "btmsConsumption": btms_consumption,
                "totalConsumption": total_consumption
            }
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))


    @staticmethod
    def load_scenario(*args, **kwargs):
        if args or kwargs:
            log.i(f"Loading saved scenario")
            for kwarg in kwargs:
                 log.i(f"First saved scenario: {kwarg}")
        else:
            log.i("Creating new scenario")

    @staticmethod
    def save_scenario(scenario):
        log.i("Saving scenario <id> with params <params>")


    @staticmethod
    def more_functions_here():
        log.d("You can add more functions to this class")

if __name__ == '__main__':
    # Tests
    Simulation().load_scenario(scenario='my saved scenario')
    Simulation().load_scenario()
