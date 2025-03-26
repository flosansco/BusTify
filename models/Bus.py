from models.EnergySystems.Battery import Battery
from models.EnergySystems.Propulsion import Propulsion
from models.EnergySystems.HVAC import HVAC
from models.Route.Traject import Traject
from LoggerManager.Logger import log
import json


class Bus:
    uid: int
    traject: Traject
    battery: Battery
    propulsion: Propulsion
    hvac: HVAC
    nb_passenger: int
    confort_thermique: int  # à définir

    def __init__(self):
        log.i("Creating bus")

    def get_bus_characteristics(self, json_inputs_file="../ressources/inputs.json"):
        with open(json_inputs_file, 'r') as json_file:
            j = json.load(json_file)  # type: dict
            log.d(j.keys())


    def get_bus_estimated_weight(self):
        estimated_empty_bus_weight = 3000  # kg
        estimated_average_passenger_weight = 75  # kg
        estimated_weight = estimated_average_passenger_weight * self.nb_passenger
        return estimated_weight

    def calculate_total_bus_consumption(self):
        return self.battery.get_consumption() + self.propulsion.get_consumption() + self.hvac.get_consumption()

if __name__ == '__main__':
    Bus().get_bus_characteristics()