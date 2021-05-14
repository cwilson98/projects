import unittest
from estate_system import EstateSystem
from estate import Estate
from manager import Manager

class TestEstate(unittest.TestCase):
    def test_create_estate(self):
        estate_system = EstateSystem()
        estate = Estate(estate_system, "Me")
        self.assertEqual(estate.name, "Me", "Name Should be Me")

    def test_add_thoroughfare(self):
        estate_system = EstateSystem()
        estate = Estate(estate_system, "Python")
        self.assertEqual(estate.add_thoroughfare(), 1, "There should be one thoroughfare")

    def test_add_property(self):
        estate_system = EstateSystem()
        estate = Estate(estate_system, "Python")
        self.assertEqual(estate.add_property(), 1, "There should be one property")

    def test_remove_thoroughfare(self):
        estate_system = EstateSystem()
        estate = Estate(estate_system, "Python")
        self.assertEqual(estate.add_thoroughfare(), 1, "There should be one thoroughfare")
        self.assertEqual(estate.remove_thoroughfare(), 1, "There should be no thoroughfares")

    def test_remove_property(self):
        estate_system = EstateSystem()
        estate = Estate(estate_system, "Python")
        self.assertEqual(estate.add_property(), 1, "There should be one property")
        self.assertEqual(estate.remove_property(), 1, "There should be no properties")

    def test_update_estate(self):
        estate_system = EstateSystem()
        estate = Estate(estate_system, "Python")
        self.assertEqual(estate.update_estate("Charm"), "Charm", "Name should be changed to Charm")

    def test_change_manager(self):
        estate_system = EstateSystem()
        estate = Estate(estate_system, "Python")
        manager = Manager(estate_system, "Luis")
        estate.estate_manager = manager
        self.assertEqual(estate.change_manager("Chris"), "Chris", "The new manager should be Chris")






if __name__ == '__main__':
    unittest.main()
