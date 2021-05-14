import unittest
from estate_system import EstateSystem
from manager import Manager

class TestManager(unittest.TestCase):
    def test_create_manager(self):
        estate_system = EstateSystem()
        manager = Manager(estate_system, "Chris")
        self.assertEqual(manager.username("Chris"), "Chris", "The manager should be made Chris")

    def test_create_thoroughfare(self):
        estate_system = EstateSystem()
        manager = Manager(estate_system, "Chris")
        self.assertEqual(manager.create_thoroughfare("Bill"), "Bill", "Thoroughfare should be created")

    def test_view_thoroughfare(self):
        estate_system = EstateSystem()
        manager = Manager(estate_system, "Chris")
        self.assertEqual(manager.create_thoroughfare("Greg"), "Greg", "Thoroughfare named Greg should be made")
        self.assertEqual(manager.create_thoroughfare("Ford"), "Ford", "Thoroughfare named Ford should be made")
        self.assertEqual(manager.create_thoroughfare("Blank"), "Blank", "Thoroughfare named Blank should be made")
        self.assertEqual(manager.view_thoroughfare(), None, "Display all Thoroughfares")

    def test_remove_thoroughfare(self):
        estate_system = EstateSystem()
        manager = Manager(estate_system, "Chris")
        self.assertEqual(manager.create_thoroughfare("Greg"), "Greg", "Thoroughfare named Greg should be made")
        self.assertEqual(manager.remove_thoroughfare("Greg"), "Greg", "Thoroughfare named Greg should be deleted")

    def test_update_thoroughfare(self):
        estate_system = EstateSystem()
        manager = Manager(estate_system, "Chris")
        self.assertEqual(manager.create_thoroughfare("Greg"), "Greg", "Thoroughfare named Greg should be made")
        self.assertEqual(manager.update_thoroughfare("Greg"), "Greg", "Should bring user to the thoroughfare menu")

    def test_create_property(self):
        estate_system = EstateSystem()
        manager = Manager(estate_system, "Chris")
        self.assertEqual(manager.create_property("Bill"), "Bill", "Property should be created")

    def test_view_property(self):
        estate_system = EstateSystem()
        manager = Manager(estate_system, "Chris")
        self.assertEqual(manager.create_property("Greg"), "Greg", "Property named Greg should be made")
        self.assertEqual(manager.create_property("Ford"), "Ford", "Property named Ford should be made")
        self.assertEqual(manager.create_property("Blank"), "Blank", "Property named Blank should be made")
        self.assertEqual(manager.view_property(), None, "Display all Properties")

    def test_remove_property(self):
        estate_system = EstateSystem()
        manager = Manager(estate_system, "Chris")
        self.assertEqual(manager.create_property("Greg"), "Greg", "Property named Greg should be made")
        self.assertEqual(manager.remove_property("Greg"), "Greg", "Property named Greg should be deleted")

    def test_update_property(self):
        estate_system = EstateSystem()
        manager = Manager(estate_system, "Chris")
        self.assertEqual(manager.create_property("Greg"), "Greg", "Property named Greg should be made")
        self.assertEqual(manager.update_property("Greg"), "Greg", "Should bring user to the property menu")

    def test_create_household(self):
        estate_system = EstateSystem()
        manager = Manager(estate_system, "Chris")
        self.assertEqual(manager.create_household("Bill"), "Bill", "Household should be created")

    def test_view_household(self):
        estate_system = EstateSystem()
        manager = Manager(estate_system, "Chris")
        self.assertEqual(manager.create_household("Greg"), "Greg", "Household named Greg should be made")
        self.assertEqual(manager.create_household("Ford"), "Ford", "Household named Ford should be made")
        self.assertEqual(manager.create_household("Blank"), "Blank", "Household named Blank should be made")
        self.assertEqual(manager.view_household(), None, "Display all Households")

    def test_remove_household(self):
        estate_system = EstateSystem()
        manager = Manager(estate_system, "Chris")
        self.assertEqual(manager.create_household("Greg"), "Greg", "Household named Greg should be made")
        self.assertEqual(manager.remove_household("Greg"), "Greg", "Household named Greg should be deleted")

    def test_update_household(self):
        estate_system = EstateSystem()
        manager = Manager(estate_system, "Chris")
        self.assertEqual(manager.create_household("Greg"), "Greg", "Household named Greg should be made")
        self.assertEqual(manager.update_household("Greg"), "Greg", "Should bring user to the household menu")

    def test_create_user(self):
        estate_system = EstateSystem()
        manager = Manager(estate_system, "Chris")
        self.assertEqual(manager.create_user("Bill"), "Bill", "User should be created")

    def test_view_user(self):
        estate_system = EstateSystem()
        manager = Manager(estate_system, "Chris")
        self.assertEqual(manager.create_user("Greg"), "Greg", "User named Greg should be made")
        self.assertEqual(manager.create_user("Ford"), "Ford", "User named Ford should be made")
        self.assertEqual(manager.create_user("Blank"), "Blank", "User named Blank should be made")
        self.assertEqual(manager.view_users(), None, "Display all Users")

    def test_remove_user(self):
        estate_system = EstateSystem()
        manager = Manager(estate_system, "Chris")
        self.assertEqual(manager.create_user("Greg"), "Greg", "User named Greg should be made")
        self.assertEqual(manager.remove_user("Greg"), "Greg", "User named Greg should be deleted")


if __name__ == '__main__':
    unittest.main()
