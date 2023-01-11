from car import Car
from engine.eng import CapuletEngine, WilloughbyEngine, SternmanEngine
from engine.battery import SpindlerBattery, NubbinBattery

class CarFactory:
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        calliope = Car(current_date, last_service_date, current_mileage, last_service_mileage)
        calliope.engine = CapuletEngine()
        calliope.battery = SpindlerBattery()
        return calliope
    
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        glissade = Car(current_date, last_service_date, current_mileage, last_service_mileage)
        glissade.engine = WilloughbyEngine()
        glissade.battery = SpindlerBattery()
        return glissade

    def create_palindrome(current_date, last_service_date, current_mileage, last_service_mileage):
        palindrome = Car(current_date, last_service_date, current_mileage, last_service_mileage)
        palindrome.engine = SternmanEngine()
        palindrome.battery = SpindlerBattery()
        return palindrome

    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        rorschach = Car(current_date, last_service_date, current_mileage, last_service_mileage)
        rorschach.engine = WilloughbyEngine()
        rorschach.battery = NubbinBattery()
        return rorschach

    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        thovex = Car(current_date, last_service_date, current_mileage, last_service_mileage)
        thovex.engine = CapuletEngine()
        thovex.battery = NubbinBattery()
        return thovex