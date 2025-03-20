from pydantic import BaseModel

# Définition du modèle des données envoyées par le frontend
class SimulationRequest(BaseModel):
    # environnement: Environnement
    temperature: float
    humidity: float
    passengers: int
    # distance_trajet: float
    # nb_arrets: int
    # vitesse_moyenne_bus: float
    # nb_passagers: int
    # profil_d_optimisation: ProfilOptimisation