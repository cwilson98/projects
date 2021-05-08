import unittest
from thoroughfare import Thoroughfare

class TestThoroughfare(unittest.TestCase):
    def testcreate_thoroughfare(self):
        street = Thoroughfare("Cool")
        self.assertEqual(street.create_thoroughfare(["Cool"]), None, "One street should be created")

    def teststr_thoroughfare(self):
        print(str())

if __name__ == '__main__':
    unittest.main()
