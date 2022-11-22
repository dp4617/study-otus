"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02 import exceptions
from homework_02.base import Vehicle


class Plane(Vehicle):
    cargo = None
    max_cargo = None

    def __init__(self, weight, fuel, fuel_consumption, max_cargo, cargo=0):
        Vehicle.__init__(self, weight=weight, fuel=fuel, fuel_consumption=fuel_consumption)
        self.cargo = cargo
        self.max_cargo = max_cargo

    def load_cargo(self, to_load):
        if (self.cargo + to_load) > self.max_cargo:
            raise exceptions.CargoOverload
        else:
            self.cargo = self.cargo + to_load

    def remove_all_cargo(self):
        result = self.cargo
        self.cargo = 0
        return result
