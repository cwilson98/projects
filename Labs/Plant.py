from LivingThing import LivingThing
from InvisibilitySuperPower import InvisibilitySuperPower

class Plant(LivingThing, InvisibilitySuperPower):

    def __init__(self, name: str, energy: int=LivingThing.MAX_ENERGY) -> None:
        self.__name = name
        self.__energy = energy
    def __repr__(self) -> str:
        return f'Plant(name={self.__name})'

    def __str__(self) -> str:
        return f'{self.__name} has {self.__energy} energy'

    def absorb(self, amount:int) -> int:
        new_energy = self.__energy + amount
        if new_energy > LivingThing.MAX_ENERGY:
            self.energy = LivingThing.MAX_ENERGY
            return new_energy - LivingThing.MAX_ENERGY
        else:
            self.energy = new_energy
            return self.energy - LivingThing.MAX_ENERGY





