from pydantic import BaseModel


# Définition du modèle des données envoyées par le frontend
class SimulationRequest(BaseModel):
    busType: str
    routeName: str
    temperature: float
    humidity: float
    coolingType: str
    optimization: str
