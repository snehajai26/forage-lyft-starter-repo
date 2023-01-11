from abc import ABC, abstractmethod


class Serviceable(ABC):
    @abstractmethod
    def needs_service(self):
        pass

class Car(Serviceable):

    def __init__(self, engine, battery, tires_array):
        self.engine = engine
        self.battery = battery
        self.tires = tires_array

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service() or self.tires.needs_service()
