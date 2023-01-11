from abc import ABC, abstractmethod

from car import Car


class Engine(Car, ABC):
    @abstractmethod
    def needs_service(self):
        pass

class CapuletEngine(Engine):
    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > 30000

class SternmanEngine(Engine):
    def needs_service(self):
        return self.warning_light_is_on

class WilloughbyEngine(Engine):
    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > 60000