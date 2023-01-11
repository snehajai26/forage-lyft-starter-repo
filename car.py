from abc import ABC, abstractmethod


class Serviceable(ABC):
    @abstractmethod
    def needs_service(self):
        pass

class Car(Serviceable):
    #def __init__(self, last_service_date):
    #    self.last_service_date = last_service_date

    def __init__(self, current_date, last_service_date, current_mileage, last_service_mileage):
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        self.engine = None
        self.battery = None


    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()
