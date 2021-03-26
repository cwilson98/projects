from Human import Human
from FlyingSuperPower import FlyingSuperPower

class SuperHuman(Human, FlyingSuperPower):


    def __init__(self, name:str, age:int, energy:int) -> None:
        self.__name = name
        self.__age = age
        self.__energy = energy

    def fly(self, distance) -> None:
        print("Human is flying")

    def turnInvisible(self) -> None:
        print("Human is now invisible")

    def turnVisible(self) -> None:
        print("Human is now visible")
        