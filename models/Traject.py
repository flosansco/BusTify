from models.Segment import Segment


class Traject:
    def __init__(self, uid, segment_list: list[Segment], length: float):
        self.uid = uid
        self.segment_list = segment_list
        self.nb_stops = len(self.segment_list)
        self.length = length  # km




