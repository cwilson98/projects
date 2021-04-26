import unittest
from Homan import Human


class TestHuman(unittest.TestCase):

    def test_eat(self) -> None:
        # energy is full and try to eat
        human_prins = Human("Prins")
        self.assertEqual(human_prins.eat(20), 20, "Excess should be 20.")

        # energy is below 100 and eat more than required
        human_prins = Human("Prins", energy=90)
        self.assertEqual(human_prins.eat(20), 10, "Excess should 20.")

        # energy is below 100 and eat exactly what is required
        human_prins = Human("Prins", energy=80)
        self.assertEqual(human_prins.eat(20), 0, "Excess should be 0.")

        # energy is below 100 and eat less than required
        human_prins = Human("Prins", energy=70)
        self.assertEqual(human_prins.eat(20), -10, "Excess should be -10.")

    def test_grow(self) -> None:
        human_prins = Human("Prins")
        human_prins.grow()
        self.assertEqual(human_prins.age, 1, "Age should be 1")

    def test_reproduce(self):
        human_prins = Human("Prins")
        self.assertEqual(human_prins.reproduce(), True, "Energy should be at 80")

    def test_str(self):
        aHuman = Human('Adam')
        print(str(aHuman))
    # Add additional tests here.


if __name__ == '__main__':
    unittest.main()