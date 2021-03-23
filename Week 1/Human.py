from Animal import Animal
from Clothing import Clothing


class Human(Animal):

    def __init__(self, name: str, age: int = 0, energy: int = Animal.MAX_ENERGY) -> None:
        super(Human, self).__init__(name, age, energy)
        self.clothing = []


    def dress(self, clothing: Clothing) -> None:
        self.clothing.add(clothing)

    def undress(self, clothing: Clothing) -> None:
        self.clothing.remove(clothing)

