import unittest

from Human import Human
from planet import Planet

class TestPlanet(unittest.TestCase):

    def test_add_human(self):

        # check: 0 population
        earth = Planet("Earth")
        self.assertEqual(earth.population(), 0, "Population should be 0.")

        # check: single human
        prins = Human("Prins")
        earth.add(prins)
        self.assertEqual(earth.population(), 1, "Population should be 1.")

    def test_has(self):

        # check: does not have specified human
        earth = Planet("Earth")
        prins = Human("Prins")
        self.assertFalse(earth.has(prins), "Should be false.")

        # check: has specified human
        earth.add(prins)
        self.assertTrue(earth.has(prins), "Should be true.")

    def test_population(self):

        # check: no population
        earth = Planet("Earth")
        self.assertEqual(earth.population(), 0, "Population should be 0.")

        # check: no population of one
        prins = Human("Prins")
        earth.add(prins)
        self.assertEqual(earth.population(), 1, "Population should be 1")


if __name__ == '__main__':
    unittest.main()