import unittest
from estate_system import EstateSystem
from thoroughfare import Thoroughfare

class TestProperty(unittest.TestCase):
    def test_create_thoroughfare(self):
        estate_system = EstateSystem()
        thoroughfare = Thoroughfare(estate_system, "Cool")
        self.assertEqual(thoroughfare.name, "Cool", "Thoroughfare should have name Name")

    def test_add_property(self):
        estate_system = EstateSystem()
        thoroughfare = Thoroughfare(estate_system, "Cool")
        self.assertEqual(thoroughfare.add_property(), 1, "One Property should be added")

    def test_remove_property(self):
        estate_system = EstateSystem()
        thoroughfare = Thoroughfare(estate_system, "Cool")
        self.assertEqual(thoroughfare.add_property(), 1, "One Property should be added")
        self.assertEqual(thoroughfare.remove_property(), 0, "There should be no properties")

    def test_change_name(self):
        estate_system = EstateSystem()
        thoroughfare = Thoroughfare(estate_system, "Cool")
        self.assertEqual(thoroughfare.change_name("Beep"), "Beep", "New name should be Beep")

if __name__ == '__main__':
    unittest.main()
