from abc import ABC
from homework_02 import exceptions


class Vehicle(ABC):
    weight = int
    fuel = int
    fuel_consumption = int
    started = bool

    def __init__(self, weight, fuel, fuel_consumption, started = False):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = started

    def start(self):
        if self.fuel > 0:
            self.started = True
        else:
            raise exceptions.LowFuelError

    def move(self, distance):
        if self.fuel < self.fuel_consumption * distance:
            raise exceptions.NotEnoughFuel
        else:
            self.fuel -= self.fuel_consumption * distance
