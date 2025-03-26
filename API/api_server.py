import sys
from Simulation.Simulation import Simulation
from LoggerManager.Logger import log


# Point d'entrée pour Uvicorn
# Lancer le serveur avec : uvicorn api_server:app --reload
log.i("Please launch simulation with `uvicorn API.api_server:app --reload`")
simulation = Simulation()
app = simulation.app
