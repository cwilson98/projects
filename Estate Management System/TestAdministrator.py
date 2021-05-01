import unittest
from Administrator import Administrator
from Estate import Estate
from Property import Property

class TestAdministrator(unittest.TestCase):
    def testcreate_estate(self):
        admin = Administrator("Chris")
        self.assertEqual(admin.create_estate(), Estate, "One estate should be made")

        self.assertEqual(admin.create_property(), Property, "Property")



if __name__ == '__main__':
    unittest.main()