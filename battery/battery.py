from abc import ABC, abstractmethod

from datetime import datetime

from car import Car


class Battery(Car, ABC):
    @abstractmethod
    def needs_service(self):
        pass

class SpindlerBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date
    
    def needs_service(self):
        threshold = self.last_service_date.replace(year=self.last_service_date.year + 3)
        return threshold < self.current_date

class NubbinBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        threshold = self.last_service_date.replace(year=self.last_service_date.year + 4)
        return threshold < self.current_date
