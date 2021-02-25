class Human:

    MAX_ENERGY = 100
    MOVE_ENERGY = 10
    REPRODUCE_ENERGY = 20

    def __init__(self, name:str, age:int=0, energy:int=MAX_ENERGY) -> None:
        self.name = name
        self.age = age
        self.energy = energy

    def __repr__(self) -> str:
        return f'human(name={self.name}, age={self.age}, energy={self.energy})'

    def __str__(self) -> str:
        return f'{self.name} is {self.age} years old and has {self.energy} energy'

    def grow(self) -> int:
        return self.age + 1

    def eat(self, amount: int) -> int:
        new_energy = self.energy + amount
        if new_energy >= Human.MAX_ENERGY:
            leftovers = new_energy - Human.MAX_ENERGY
            self.energy = Human.MAX_ENERGY
            return leftovers
        else:
            self.energy = new_energy



    def reproduce(self) -> bool:
        if self.energy >= Human.REPRODUCE_ENERGY:
            self.energy = self.energy - Human.REPRODUCE_ENERGY
            return True
        else:
            return False

    def move(self, distance: int) -> bool:
        required_energy = Human.MOVE_ENERGY + distance
        if self.energy >= required_energy:
            self.energy = self.energy - required_energy
            return True
        else:
            return False


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

    # Add additional tests here.


if __name__ == '__main__':
    unittest.main()