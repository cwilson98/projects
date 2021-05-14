import unittest
from estate_system import EstateSystem
from household import Household


class TestHousehold(unittest.TestCase):
    def test_create_household(self):
        estate_system = EstateSystem()
        household = Household(estate_system, "House")
        self.assertEqual(household.name, "House", "Household House should be created")

    def test_add_occupants(self):
        estate_system = EstateSystem()
        household = Household(estate_system, "House")
        self.assertEqual(household.add_occupant(), 2, "Two occupants should be added to household")

    def test_remove_occupants(self):
        estate_system = EstateSystem()
        household = Household(estate_system, "House")
        self.assertEqual(household.add_occupant(), 2, "Two occupants should be added to household")
        self.assertEqual(household.remove_occupant(), 2, "Two occupants should be removed from household")

    def test_change_name(self):
        estate_system = EstateSystem()
        household = Household(estate_system, "House")
        self.assertEqual(household.change_name("Peng"), "Peng", "Name should now be Peng")

    def test_make_payment(self):
        estate_system = EstateSystem()
        household = Household(estate_system, "House")
        self.assertEqual(household.make_payment(2000), None, "Household should now be paid for")

    def test_make_underpayment(self):
        estate_system = EstateSystem()
        household = Household(estate_system, "House")
        self.assertEqual(household.make_payment(500), None, "Household should now have $650 left")

if __name__ == '__main__':
    unittest.main()
