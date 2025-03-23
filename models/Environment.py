class Battery:
    def __init__(self, initial_in_temperature: float, out_temperature:float, humidity:float):

        self.initial_in_temperature = initial_in_temperature
        self.out_temperature = out_temperature
        self.humidity = humidity

        self.conditions = dict()
        self.conditions["Indoor temperature"] = self.initial_in_temperature
        self.conditions["Outdoor temperature"] = self.out_temperature
        self.conditions["Humidity"] = self.humidity

    def get_conditions(self):

        return self.conditions
