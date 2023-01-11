from abc import ABC, abstractmethod

from datetime import datetime

from car import Car


class Battery(Car, ABC):
    @abstractmethod
    def needs_service(self):
        pass

class SpindlerBattery(Battery):
    def needs_service(self):
        threshold = service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        return threshold < datetime.today().date()

class NubbinBattery(Battery):
    def needs_service(self):
        threshold = service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        return threshold < datetime.today().date()
