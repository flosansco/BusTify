import os

from models.Trajet import Traject
from models.Points import Point
from LoggerManager.Logger import log


class Routine:

    def __init__(self):
        log.i(f"Creating new instance of {self.__class__} ")

    @staticmethod
    def run_routine(routines):
        print(f"Running routine : {routines}")

    @staticmethod
    def create_traject():
        log.d("Hello")
        log.i("Hello")
        log.e("Hello")
        log.w("Hello")


if __name__ == '__main__':
    Routine()
