from LivingThing import LivingThing

class Planet:

    def __init__(self, name: str = '') -> None:
        self.__name = name
        self.__livingthings = []

    def add(self, livingthing: LivingThing) -> bool:
        self.__livingthings.append(livingthing)
        return (livingthing in self.__livingthings)

    def remove(self, livingthing: LivingThing) -> bool:
        self.__livingthings.remove(livingthing)
        return (livingthing not in self.__livingthings)

    def has(self, livingthing: LivingThing) -> bool:
        return (livingthing in self.__livingthings)

    def __repr__(self):
        return f'Planet(name={self.__name}, human={self.__livingthings})'

    def __str__(self):
        return f'The Planet {self.__name} has {len(self.__livingthings)} living things'

    def population(self) -> int:
        return len(self.__livingthings)