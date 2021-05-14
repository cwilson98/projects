import unittest
from estate_system import EstateSystem
from property import Property

class TestProperty(unittest.TestCase):
    def test_create_property(self):
        estate_system = EstateSystem()
        property = Property(estate_system, "Name")
        self.assertEqual(property.name, "Name", "Property should have name Name")

    def test_add_household(self):
        estate_system = EstateSystem()
        property = Property(estate_system, "Name")
        self.assertEqual(property.add_household(), 1, "One household should be added")

    def test_remove_household(self):
        estate_system = EstateSystem()
        property = Property(estate_system, "Name")
        self.assertEqual(property.add_household(), 1, "One household should be added")
        self.assertEqual(property.remove_household(), 0, "There should be no households")

    def test_change_name(self):
        estate_system = EstateSystem()
        property = Property(estate_system, "Name")
        self.assertEqual(property.change_name("Blarg"), "Blarg", "Name should be Blarg")

    def test_change_owner(self):
        estate_system = EstateSystem()
        property = Property(estate_system, "Name")
        self.assertEqual(property.change_owner("Kait"), "Kait", "Owner should be Kait")



if __name__ == '__main__':
    unittest.main()
