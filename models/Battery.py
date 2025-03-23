from LoggerManager.Logger import log
from enums.Enums import CoolingType


class Battery:
    def __init__(self, uid, temperature, capacity, nb_cell, consumption, cooling_type: CoolingType):
        self.uid = uid
        self.temperature = temperature
        self.capacity = capacity
        self.nb_cell = nb_cell
        self.consumption = consumption
        self.cooling_type = cooling_type

    def get_cooling_type(self):

        log.d("Cooling type is")
