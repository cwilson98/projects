from LivingThing import LivingThing

class Animal:

    MAX_ENERGY = 100

    def __init__(self, name:str, age:int=0, energy:int=LivingThing.MAX_ENERGY) -> None:
        self.name = name
        self.age = age
        self.energy = energy

    def eat(self, amount: int) -> int:
        new_energy = self.energy + amount
        if new_energy > Animal.MAX_ENERGY:
            self.energy = Animal.MAX_ENERGY
            return new_energy - Animal.MAX_ENERGY
        else:
            self.energy = new_energy
            return self.energy - Animal.MAX_ENERGY

    def move(self, distance: int) -> bool:
        new_energy = self.energy - distance
        if new_energy >= Animal.MOVE_ENERGY:
            self.energy = new_energy
            return True
        else:
            return False

