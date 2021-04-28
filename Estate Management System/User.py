from Thoroughfare import Thoroughfare
from Property import Property
from Household import Household
import random

class User:

    id = 0

    def __init__(self, name: str):
        self.name = name
        self.thoroughfare = []
        self.property = []
        self.household = []

    def __repr__(self) -> str:
        return f"User={self.name}"

    def __str__(self):
        return f"Hello {self.name}"

    def create_thoroughfare(self) -> Thoroughfare:
        thoroughfare = Thoroughfare(f"Thoroughfare{random.choice(Thoroughfare.PATHWAY)}")
        self.thoroughfare.append(thoroughfare)
        return Thoroughfare

    def create_property(self) -> Property:
        Property.id += 1
        property = Property(f"Property {Property.id}")
        self.property.append(property)
        print((self.property))
        return Property

    def create_household(self) -> Household:
        Household.id += 1
        household = Household(f"Household {Household.id}")
        self.household.append(household)
        return Household

    def display_property(self) -> None:
        for property in self.property:
            print(property)







