class LivingThing:

    MAX_ENERGY = 100
    MOVE_ENERGY = 10
    REPRODUCE_ENERGY = 20

    def __init__(self, name: str) -> None:
        self._name = name

    def grow(self) -> None:
        self.age = self.age + 1

    def reproduce(self) -> bool:
        new_energy = self.energy - LivingThing.REPRODUCE_ENERGY
        if new_energy >= LivingThing.REPRODUCE_ENERGY:
            self.energy = new_energy - LivingThing.REPRODUCE_ENERGY
            return True
        else:
            return False
