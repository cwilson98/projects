import unittest
from User import User

class TestManager(unittest.TestCase):
    def testcreate_thoroughfare(self):
        create = User("Chris")
        self.assertEqual(create.create_thoroughfare(["Funny Lane"]), None, "One thoroughfare should be created")



if __name__ == '__main__':
    unittest.main()
