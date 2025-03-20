class Battery:
    def __init__(self, in_temperature:float=20.5, out_temperature:float=5.0, humidity:float=52.5):
        self.in_temperature = in_temperature
        self.out_temperature = out_temperature
        self.humidity = humidity

        self.conditions = dict()
        self.conditions["Indoor temperature"] = self.in_temperature
        self.conditions["Outdoor temperature"] = self.out_temperature
        self.conditions["Humidity"] = self.humidity

    def get_conditions(self):

        return self.conditions
