import unittest

from User import User
from Thoroughfare import Thoroughfare
from Property import Property
from Household import Household


class TestUser(unittest.TestCase):

    def testcreate_thoroughfare(self):
        user = User("Chris")
        self.assertEqual(user.create_thoroughfare(), Thoroughfare, "One thoroughfare should be created")

    def testcreate_household(self):
        user = User("Chris")
        self.assertEqual(user.create_household(), Household, "One household should be created")

    def testcreate_property(self):
        user = User("Chris")
        self.assertEqual(user.create_property(), Property, "One property should be created")

if __name__ == '__main__':
    unittest.main()
