class Human:

    MAX_ENERGY = 100
    MOVE_ENERGY = 10
    REPRODUCE_ENERGY = 20

    def __init__(self, name:str, age:int=0, energy:int=100) -> None:
        self.name = name
        self.age = age
        self.energy = energy

    def __repr__(self) -> str:
        return f'human(name={self.name}, age={self.age}, energy={self.energy})'

    def __str__(self) -> str:
        return f'{self.name} is {self.age} years old and has {self.energy} energy'

    def grow(self) -> None:
        self.age = self.age + 1

    def eat(self, amount: int) -> int:
        new_energy = self.energy + amount
        if new_energy > Human.MAX_ENERGY:
            self.energy = Human.MAX_ENERGY
            return new_energy - Human.MAX_ENERGY
        else:
            self.energy = new_energy
            return self.energy - Human.MAX_ENERGY

    def reproduce(self) -> bool:
        new_energy = self.energy - Human.REPRODUCE_ENERGY
        if new_energy >= Human.REPRODUCE_ENERGY:
            self.energy = new_energy - Human.REPRODUCE_ENERGY
            return True
        else:
            return False

    def move(self, distance: int) -> bool:
        new_energy = self.energy - distance
        if new_energy >= Human.MOVE_ENERGY:
            self.energy = new_energy
            return True
        else:
            return False

