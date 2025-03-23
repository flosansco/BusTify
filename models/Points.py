from enums.Enums import TypeId


class Point:
    def __init__(self, uid, position, type_id: TypeId = TypeId.STOP):
        self.uid = uid
        self.position = position
        self.type_id = type_id  # defines if it's a : stop, major or minor intersection, pedestrian crossing or red light

    @staticmethod
    def _get_position(lat, long, elevation):
        print("OneStreetMap will do it I guess ?")
