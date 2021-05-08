import unittest
from user import User
from property import Property

class MyTestCase(unittest.TestCase):
    def test_update_property(self):
        TheUser = User("Chris")
        self.assertEqual(TheUser.create_property(), Property, "One property should be created.")

        property = Property
        self.assertEqual(property.update_property(Property), True, "Name should change to whatever")

if __name__ == '__main__':
    unittest.main()
