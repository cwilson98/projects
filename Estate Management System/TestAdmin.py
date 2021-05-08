import unittest
from admin import Admin
from estate import Estate
from property import Property

class TestAdmin(unittest.TestCase):
    def testcreate_estate(self):
        admin = Admin(self, "Chris")
        self.assertEqual(admin.create_estate("Shapiro"), Estate, "One estate should be made")



if __name__ == '__main__':
    unittest.main()
