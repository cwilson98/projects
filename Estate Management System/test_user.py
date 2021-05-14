import unittest
from estate_system import EstateSystem
from user import User

class TestUser(unittest.TestCase):
    def test_create_user(self):
        estate_system = EstateSystem()
        user = User(estate_system, "Chris")
        self.assertEqual(user.username("Chris"), "Chris", "The User should be made Chris")

    def test_create_thoroughfare(self):
        estate_system = EstateSystem()
        user = User(estate_system, "Chris")
        self.assertEqual(user.create_thoroughfare("Bill"), "Bill", "Thoroughfare should be created")

    def test_view_thoroughfare(self):
        estate_system = EstateSystem()
        user = User(estate_system, "Chris")
        self.assertEqual(user.create_thoroughfare("Greg"), "Greg", "Thoroughfare named Greg should be made")
        self.assertEqual(user.create_thoroughfare("Ford"), "Ford", "Thoroughfare named Ford should be made")
        self.assertEqual(user.create_thoroughfare("Blank"), "Blank", "Thoroughfare named Blank should be made")
        self.assertEqual(user.view_thoroughfare(), None, "Display all Thoroughfares")

    def test_update_thoroughfare(self):
        estate_system = EstateSystem()
        user = User(estate_system, "Chris")
        self.assertEqual(user.create_thoroughfare("Greg"), "Greg", "Thoroughfare named Greg should be made")
        self.assertEqual(user.update_thoroughfare("Greg"), "Greg", "Should bring user to the thoroughfare menu")

    def test_create_property(self):
        estate_system = EstateSystem()
        user = User(estate_system, "Chris")
        self.assertEqual(user.create_property("Bill"), "Bill", "Property should be created")

    def test_view_property(self):
        estate_system = EstateSystem()
        user = User(estate_system, "Chris")
        self.assertEqual(user.create_property("Greg"), "Greg", "Property named Greg should be made")
        self.assertEqual(user.create_property("Ford"), "Ford", "Property named Ford should be made")
        self.assertEqual(user.create_property("Blank"), "Blank", "Property named Blank should be made")
        self.assertEqual(user.view_property(), None, "Display all Properties")

    def test_update_property(self):
        estate_system = EstateSystem()
        user = User(estate_system, "Chris")
        self.assertEqual(user.create_property("Greg"), "Greg", "Property named Greg should be made")
        self.assertEqual(user.update_property("Greg"), "Greg", "Should bring user to the property menu")

    def test_create_household(self):
        estate_system = EstateSystem()
        user = User(estate_system, "Chris")
        self.assertEqual(user.create_household("Bill"), "Bill", "Household should be created")

    def test_view_household(self):
        estate_system = EstateSystem()
        user = User(estate_system, "Chris")
        self.assertEqual(user.create_household("Greg"), "Greg", "Household named Greg should be made")
        self.assertEqual(user.create_household("Ford"), "Ford", "Household named Ford should be made")
        self.assertEqual(user.create_household("Blank"), "Blank", "Household named Blank should be made")
        self.assertEqual(user.view_household(), None, "Display all Households")

    def test_update_household(self):
        estate_system = EstateSystem()
        user = User(estate_system, "Chris")
        self.assertEqual(user.create_household("Greg"), "Greg", "Household named Greg should be made")
        self.assertEqual(user.update_household("Greg"), "Greg", "Should bring user to the household menu")

if __name__ == '__main__':
    unittest.main()
