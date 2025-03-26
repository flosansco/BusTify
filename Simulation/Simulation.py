from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from Simulation.SimulationRequest import SimulationRequest
from models.EnergySystems.HVAC import HVAC
from LoggerManager.Logger import log


class Simulation:
    """

    """
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
        Fonction qui sera exécutée via l'appel javascript en cliquant sur le bouton "Lancer la simulation"



        :param SimulationRequest request: l'ensemble des données utilisées par le backend qui seront
                envoyées au frontend. Doit absolument correspondre aux données déclarées dans le .js
        """
        try:
            log.d(f"Données reçues : {request.model_dump()}")
            log.i("Calcul des consommations HVAC uniquement")

            # Simuler la consommation (remplacer par une vraie logique plus tard)
            hvac = HVAC()
            total_hvac_consumption = hvac.get_pac_consumption() + hvac.get_acs_consumption() + hvac.get_btms_consumption()

            # Réponse renvoyée au frontend (js)
            return {
                "pacConsumption": hvac.get_pac_consumption(),
                "acsConsumption": hvac.get_acs_consumption(),
                "btmsConsumption": hvac.get_btms_consumption(),
                "totalConsumption": total_hvac_consumption
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

    def display_graph(self):
        log.i("Affichage de graph avec plt")


    @staticmethod
    def more_functions_here():
        log.d("You can add more functions to this class")

if __name__ == '__main__':
    # Tests
    Simulation().load_scenario(scenario='my saved scenario')
    Simulation().load_scenario()
