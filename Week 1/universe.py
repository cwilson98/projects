from typing import List
from planet import Planet

class Universe:

    def __init__(self) -> None:
        self.__planets = []

    def generate(self, names: List[str]) -> None:
        new_planets = []
        for name in names:
            planet = Planet(name)
            new_planets.append(planet)
            self.__planets.append(planet)

    def display(self) -> None:
        for planet in self.__planets:
            print(f"Planet:{planet.__name}, Population:{planet.population()}")