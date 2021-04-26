import unittest
from Estate import Estate

class TestEstate(unittest.TestCase):
    def test_repr(self):
        estate = Estate('Blarg', 'Southampton')
        print(repr(estate))


if __name__ == '__main__':
    unittest.main()
