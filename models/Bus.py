from models.Battery import Battery
from models.Traject import Traject
from LoggerManager.Logger import log
import json


class Bus:
    uid: int
    traject: Traject
    battery: Battery
    nb_passenger: int

    def __init__(self):
        log.i("Creating bus")

    def get_bus_characteristics(self, json_inputs_file="../ressources/inputs.json"):
        with open(json_inputs_file, 'r') as json_file:
            j = json.load(json_file)  # type: dict
            log.d(j.keys())




    def get_bus_average_weight(self):
        estimate_average_passenger_weight = 75  # kg
        average_weight = estimate_average_passenger_weight / self.nb_passenger
        return average_weight


if __name__ == '__main__':
    Bus().get_bus_characteristics()