from abc import ABC, abstractmethod

from car import Car

class Tires(Car, ABC):
    @abstractmethod
    def needs_service(self):
        pass

class CarriganTires(Tires):
    def __init__(self, tires_array):
        self.tires_array = tires_array
    
    def needs_service(self):
        return self.tires_array[0] >= 0.9 or self.tires_array[1] >=0.9 or self.tires_array[2] >=0.9 or self.tires_array[3] >=0.9

class OctoprimeTires(Tires):
    def __init__(self, tires_array):
        self.tires_array = tires_array
    
    def needs_service(self):
        return self.tires_array[0] + self.tires_array[1] + self.tires_array[2] + self.tires_array[3] >= 3