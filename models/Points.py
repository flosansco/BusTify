class Point:
    def __init__(self, uid, type_id, position):
        self.uid = uid
        self.type_id = uid  # defines if it's a : stop, major or minor intersection, pedestrian crossing or red light
        self.position = position

    @staticmethod
    def _get_position(lat, long, elevation):
        print("OneStreetMap will do it I guess ?")
