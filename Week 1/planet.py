from Human import Human

class Planet:

    def __init__(self, name: str = '') -> None:
        self.__name = name
        self.__human = []

    def add(self, human: Human) -> bool:
        self.__human.append(human)
        return (human in self.__human)

    def remove(self, human: Human) -> bool:
        self.__human.remove(human)
        return (human in self.__human)

    def has(self, human: Human) -> bool:
        return (human in self.__human)

    def __repr__(self):
        return f'Planet(name={self.__name}, human={self.__human})'

    def __str__(self):
        return f'The Planet {self.__name} has {len(self.__human)} humans'

    def population(self) -> int:
        return len(self.__human)