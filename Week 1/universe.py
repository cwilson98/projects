from planet import Planet
from typing import List

class Universe:

    def __init__(self):
        self.__planets = []

    def generate(self, planet_names:List[str]) -> None:
        generated_planets = []

        for planet_name in planet_names:
            planet = Planet(planet_name)
            self.__planets.append(planet)
            generated_planets.append(planet)

    def display(self) -> None:
        for planet in self.__planets:
            print(f"Planet: {planet.__name}, Population: {planet.population()}")