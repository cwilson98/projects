import unittest
from estate import Estate
from thoroughfare import Thoroughfare
from property import Property

class TestEstate(unittest.TestCase):
    def test_add_thoroughfare(self):
        estate = Estate("Python")
        self.assertEqual(estate.thoroughfares(), 0, "There should be no Thoroughfares.")

        thoroughfare = Thoroughfare("Gallop")
        estate.add_thoroughfare(thoroughfare)
        self.assertEqual(estate.thoroughfares(), 1, "There should be one Thoroughfare")

    def test_remove_thoroughfare(self):
        estate = Estate("Sonic")
        thorougfare = Thoroughfare("Porn")
        estate.add_thoroughfare(thorougfare)
        self.assertEqual(estate.thoroughfares(), 1, "There should be one Thoroughfare")
        estate.remove_thoroughfare(thorougfare)
        self.assertEqual(estate.thoroughfares(), 0, "There should be no Thoroughfares")


    def test_add_property(self):
        estate = Estate("Kennedie")
        self.assertEqual(estate.properties(), 0, "There should be no properties.")

        property = Property("Mom")
        estate.add_property(property)
        self.assertEqual(estate.properties(), 1, "There should be one Property.")

if __name__ == '__main__':
    unittest.main()
