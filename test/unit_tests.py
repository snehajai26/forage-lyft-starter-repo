import sys
sys.path.append(".")
import unittest
from datetime import datetime
from battery.battery import SpindlerBattery, NubbinBattery
from engine.engine import CapuletEngine, WilloughbyEngine, SternmanEngine

class TestSpindler(unittest.TestCase):
    def test_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2, day=today.day -1)
        batt = SpindlerBattery(today, last_service_date)
        self.assertTrue(batt.needs_service())

    def test_no_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        batt = SpindlerBattery(today, last_service_date)
        self.assertFalse(batt.needs_service())

class TestNubbin(unittest.TestCase):
    def test_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4, day = today.day - 1)
        batt = NubbinBattery(today, last_service_date)
        self.assertTrue(batt.needs_service())
    def test_no_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        batt = NubbinBattery(today, last_service_date)
        self.assertFalse(batt.needs_service())

class TestCapulet(unittest.TestCase):
    def test_service(self):
        current_mileage = 30001
        last_service_mileage = 0
        eng = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(eng.needs_service())
    def test_service(self):
        current_mileage = 30000
        last_service_mileage = 0
        eng = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(eng.needs_service())

class TestWilloughby(unittest.TestCase):
    def test_service(self):
        current_mileage = 60001
        last_service_mileage = 0
        eng = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(eng.needs_service())
    def test_service(self):
        current_mileage = 0000
        last_service_mileage = 0
        eng = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(eng.needs_service())

class TestSternman(unittest.TestCase):
    def test_service(self):
        warning_light = True
        eng = SternmanEngine(warning_light)
        self.assertTrue(eng.needs_service())
    def test_service(self):
        eng = SternmanEngine(False)
        self.assertFalse(eng.needs_service())

if __name__ == '__main__':
    unittest.main()