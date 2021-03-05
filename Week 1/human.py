class Human:

    MAX_ENERGY = 100
    MOVE_ENERGY = 10
    REPRODUCE_ENERGY = 20

    def __init__(self, name:str, age:int=0, energy:int=MAX_ENERGY):
        self.__name = name
        self.__age = age
        self.__energy = energy

    def __repr__(self) -> str:
        return f'human(name={self.__name}, age={self.__age}, energy={self.__energy})'

    def __str__(self) -> str:
        return f'{self.__name} is {self.__age} years old and has {self.__energy} energy'

    def grow(self) -> int:
        return self.__age + 1

    def eat(self, amount: int) -> int:
        new_energy = self.__energy + amount
        if new_energy >= Human.MAX_ENERGY:
            leftovers = new_energy - Human.MAX_ENERGY
            self.__energy = Human.MAX_ENERGY
            return leftovers
        else:
            self.__energy = new_energy



    def reproduce(self) -> bool:
        if self.__energy >= Human.REPRODUCE_ENERGY:
            self.__energy = self.__energy - Human.REPRODUCE_ENERGY
            return True
        else:
            return False

    def move(self, distance: int) -> bool:
        required_energy = Human.MOVE_ENERGY + distance
        if self.__energy >= required_energy:
            self.__energy = self.__energy - required_energy
            return True
        else:
            return False

    def dress(self, clothing: Clothing) -> None:
        self.clothing.add(clothing)

    def undress(self, clothing: Clothing) -> None:
        self.clothing.remove(clothing)