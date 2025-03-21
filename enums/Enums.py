from enum import Enum


class TypeId(Enum):
    STOP = "STOP"
    MAJOR_INTERSECTION = "MAJOR_INTERSECTION"
    MINOR_INTERSECTION = "MINOR_INTERSECTION"
    PEDESTRIAN_CROSSING = "PEDESTRIAN_CROSSING"
    RED_LIGHT = "RED_LIGHT"
