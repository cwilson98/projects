from human import Human

class Planet:
    def __init__(self, name: str = ''):
        self.__name = name
        self.__humans = []

    def __repr__(self):
        return f'planet(name={self.__name}, humans ={self.__humans})'

    def __str__(self):
        return f'{self.__name} has {len(self.__humans)} humans.'

    def add(self, human: Human) -> bool:
        self.__humans.append(Human)
        return (human in self.__humans)

    def remove(self, human: Human) -> bool:
        self.__humans.remove(Human)
        return (human in self.__humans)

    def has(self, human: Human) -> bool:
        return (human in self.__humans)

    def population(self) -> int:
        return len(self.__humans)