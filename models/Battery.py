from LoggerManager.Logger import log

class Battery:
    def __init__(self, uid, temperature, capacity, nb_cell, consumption):
        self.uid = uid
        self.temperature = temperature
        self.capacity = capacity
        self.nb_cell = nb_cell
        self.consumption = consumption

    def get_cooling_type(self):

        log.d("Cooling type is")