from models.Points import Point
from LoggerManager.Logger import log


class Segment:
    def __init__(self, uid, start_point: Point, end_point: Point):
        self.uid = uid
        self.start_point = start_point
        self.end_point = end_point

    def create_segment(self):
        log.i("Creating segment")
