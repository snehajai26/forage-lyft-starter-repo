from car import Car
from engine.engine import CapuletEngine, WilloughbyEngine, SternmanEngine
from battery.battery import SpindlerBattery, NubbinBattery
from tires.tires import CarriganTires, OctoprimeTires

class CarFactory:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tires_array):
        engine = CapuletEngine(current_mileage, last_service_mileage)        
        battery = SpindlerBattery(current_date, last_service_date)
        tires = CarriganTires(tires_array)
        car = Car(engine, battery, tires)
        return car
    
    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tires_array):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)        
        battery = SpindlerBattery(current_date, last_service_date)
        tires = OctoprimeTires(tires_array)
        car = Car(engine, battery, tires)
        return car
    
    @staticmethod
    def create_palindrome(current_date, last_service_date, current_mileage, last_service_mileage, tires_array):
        engine = SternmanEngine(current_mileage, last_service_mileage)        
        battery = SpindlerBattery(current_date, last_service_date)
        tires = CarriganTires(tires_array)
        car = Car(engine, battery, tires)
        return car
    
    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tires_array):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)        
        battery = NubbinBattery(current_date, last_service_date)
        tires = OctoprimeTires(tires_array)
        car = Car(engine, battery, tires)
        return car
    
    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tires_array):
        engine = CapuletEngine(current_mileage, last_service_mileage)        
        battery = NubbinBattery(current_date, last_service_date)
        tires = CarriganTires(tires_array)
        car = Car(engine, battery, tires)
        return car