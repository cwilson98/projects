import unittest
from estate_system import EstateSystem
from admin import Admin

class TestAdmin(unittest.TestCase):
    def test_create_admin(self):
        estate_system = EstateSystem()
        admin = Admin(estate_system, "Chris")
        self.assertEqual(admin.username("Chris"), "Chris", "The admin should be made Chris")

    def test_create_estate(self):
        estate_system = EstateSystem()
        admin = Admin(estate_system, "Chris")
        self.assertEqual(admin.create_estate("Greg"), "Greg", "Estate named Greg should be made")

    def test_view_estate(self):
        estate_system = EstateSystem()
        admin = Admin(estate_system, "Chris")
        self.assertEqual(admin.create_estate("Greg"), "Greg", "Estate named Greg should be made")
        self.assertEqual(admin.create_estate("Ford"), "Ford", "Estate named Ford should be made")
        self.assertEqual(admin.create_estate("Blank"), "Blank", "Estate named Blank should be made")
        self.assertEqual(admin.view_estate(), None, "Display all Estates")

    def test_remove_estate(self):
        estate_system = EstateSystem()
        admin = Admin(estate_system, "Chris")
        self.assertEqual(admin.create_estate("Greg"), "Greg", "Estate named Greg should be made")
        self.assertEqual(admin.remove_estate("Greg"), "Greg", "Estate named Greg should be deleted")

    def test_update_estate(self):
        estate_system = EstateSystem()
        admin = Admin(estate_system, "Chris")
        self.assertEqual(admin.create_estate("Greg"), "Greg", "Estate named Greg should be made")
        self.assertEqual(admin.update_estate("Greg"), "Greg", "Should bring to the menu for the Estate")

    def test_create_thoroughfare(self):
        estate_system = EstateSystem()
        admin = Admin(estate_system, "Chris")
        self.assertEqual(admin.create_thoroughfare("Bill"), "Bill", "Thoroughfare should be created")

    def test_view_thoroughfare(self):
        estate_system = EstateSystem()
        admin = Admin(estate_system, "Chris")
        self.assertEqual(admin.create_thoroughfare("Greg"), "Greg", "Thoroughfare named Greg should be made")
        self.assertEqual(admin.create_thoroughfare("Ford"), "Ford", "Thoroughfare named Ford should be made")
        self.assertEqual(admin.create_thoroughfare("Blank"), "Blank", "Thoroughfare named Blank should be made")
        self.assertEqual(admin.view_thoroughfare(), None, "Display all Thoroughfares")

    def test_remove_thoroughfare(self):
        estate_system = EstateSystem()
        admin = Admin(estate_system, "Chris")
        self.assertEqual(admin.create_thoroughfare("Greg"), "Greg", "Thoroughfare named Greg should be made")
        self.assertEqual(admin.remove_thoroughfare("Greg"), "Greg", "Thoroughfare named Greg should be deleted")

    def test_update_thoroughfare(self):
        estate_system = EstateSystem()
        admin = Admin(estate_system, "Chris")
        self.assertEqual(admin.create_thoroughfare("Greg"), "Greg", "Thoroughfare named Greg should be made")
        self.assertEqual(admin.update_thoroughfare("Greg"), "Greg", "Should bring user to the thoroughfare menu")

    def test_create_property(self):
        estate_system = EstateSystem()
        admin = Admin(estate_system, "Chris")
        self.assertEqual(admin.create_property("Bill"), "Bill", "Property should be created")

    def test_view_property(self):
        estate_system = EstateSystem()
        admin = Admin(estate_system, "Chris")
        self.assertEqual(admin.create_property("Greg"), "Greg", "Property named Greg should be made")
        self.assertEqual(admin.create_property("Ford"), "Ford", "Property named Ford should be made")
        self.assertEqual(admin.create_property("Blank"), "Blank", "Property named Blank should be made")
        self.assertEqual(admin.view_property(), None, "Display all Properties")

    def test_remove_property(self):
        estate_system = EstateSystem()
        admin = Admin(estate_system, "Chris")
        self.assertEqual(admin.create_property("Greg"), "Greg", "Property named Greg should be made")
        self.assertEqual(admin.remove_property("Greg"), "Greg", "Property named Greg should be deleted")

    def test_update_property(self):
        estate_system = EstateSystem()
        admin = Admin(estate_system, "Chris")
        self.assertEqual(admin.create_property("Greg"), "Greg", "Property named Greg should be made")
        self.assertEqual(admin.update_property("Greg"), "Greg", "Should bring user to the property menu")

    def test_create_household(self):
        estate_system = EstateSystem()
        admin = Admin(estate_system, "Chris")
        self.assertEqual(admin.create_household("Bill"), "Bill", "Household should be created")

    def test_view_household(self):
        estate_system = EstateSystem()
        admin = Admin(estate_system, "Chris")
        self.assertEqual(admin.create_household("Greg"), "Greg", "Household named Greg should be made")
        self.assertEqual(admin.create_household("Ford"), "Ford", "Household named Ford should be made")
        self.assertEqual(admin.create_household("Blank"), "Blank", "Household named Blank should be made")
        self.assertEqual(admin.view_household(), None, "Display all Households")

    def test_remove_household(self):
        estate_system = EstateSystem()
        admin = Admin(estate_system, "Chris")
        self.assertEqual(admin.create_household("Greg"), "Greg", "Household named Greg should be made")
        self.assertEqual(admin.remove_household("Greg"), "Greg", "Household named Greg should be deleted")

    def test_update_household(self):
        estate_system = EstateSystem()
        admin = Admin(estate_system, "Chris")
        self.assertEqual(admin.create_household("Greg"), "Greg", "Household named Greg should be made")
        self.assertEqual(admin.update_household("Greg"), "Greg", "Should bring user to the household menu")

    def test_create_manager(self):
        estate_system = EstateSystem()
        admin = Admin(estate_system, "Chris")
        self.assertEqual(admin.create_manager("Bill"), "Bill", "Manager should be created")

    def test_view_manager(self):
        estate_system = EstateSystem()
        admin = Admin(estate_system, "Chris")
        self.assertEqual(admin.create_manager("Greg"), "Greg", "Manager named Greg should be made")
        self.assertEqual(admin.create_manager("Ford"), "Ford", "Manager named Ford should be made")
        self.assertEqual(admin.create_manager("Blank"), "Blank", "Manager named Blank should be made")
        self.assertEqual(admin.view_managers(), None, "Display all Managers")

    def test_remove_manager(self):
        estate_system = EstateSystem()
        admin = Admin(estate_system, "Chris")
        self.assertEqual(admin.create_manager("Greg"), "Greg", "Manager named Greg should be made")
        self.assertEqual(admin.remove_manager("Greg"), "Greg", "Manager named Greg should be deleted")

    def test_create_user(self):
        estate_system = EstateSystem()
        admin = Admin(estate_system, "Chris")
        self.assertEqual(admin.create_user("Bill"), "Bill", "User should be created")

    def test_view_user(self):
        estate_system = EstateSystem()
        admin = Admin(estate_system, "Chris")
        self.assertEqual(admin.create_user("Greg"), "Greg", "User named Greg should be made")
        self.assertEqual(admin.create_user("Ford"), "Ford", "User named Ford should be made")
        self.assertEqual(admin.create_user("Blank"), "Blank", "User named Blank should be made")
        self.assertEqual(admin.view_users(), None, "Display all Users")

    def test_remove_user(self):
        estate_system = EstateSystem()
        admin = Admin(estate_system, "Chris")
        self.assertEqual(admin.create_user("Greg"), "Greg", "User named Greg should be made")
        self.assertEqual(admin.remove_user("Greg"), "Greg", "User named Greg should be deleted")


if __name__ == '__main__':
    unittest.main()
