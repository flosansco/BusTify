from models.Battery import Battery
from models.Trajet import Traject


class Bus:
    def __init__(self, uid, battery:Battery, traject:Traject, nb_passenger):
        self.uid = uid
        self.traject = traject
        self.battery = battery
        self.nb_passenger = nb_passenger


    def get_bus_average_weight(self):
        estimate_average_passenger_weight = 75  #kg
        average_weight = estimate_average_passenger_weight / self.nb_passenger
        return average_weight

