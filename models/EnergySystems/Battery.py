from LoggerManager.Logger import log
from enums.Enums import CoolingType
from models.Bus import Bus


class Battery:
    def __init__(self, uid, temperature, capacity, nb_cell, consumption, cooling_type: CoolingType):
        super().__init__()
        self.uid = uid
        self.temperature = temperature
        self.capacity = capacity
        self.nb_cell = nb_cell
        self.consumption = consumption
        self.cooling_type = cooling_type

    def get_cooling_type(self):

        chosen_cooling_type = CoolingType.AIR
        return chosen_cooling_type

    def get_consumption(self):
        consumption = 1  # GW.h
        return consumption


