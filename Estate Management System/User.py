from Thoroughfare import Thoroughfare
from Property import Property
from Household import Household
import random

class User:

    id = 0

    def __init__(self, Estate_System, name: str):
        self.name = name
        self.estate_system = Estate_System
        self.thoroughfare = []
        self.property = []
        self.household = []

    def create_thoroughfare(self, name):
        thoroughfare = Thoroughfare(f"{name} {random.choice(Thoroughfare.PATHWAY)}")
        self.thoroughfare.append(thoroughfare)

    def view_thoroughfare(self):
        for name in self.thoroughfare:
            print(name)

    def create_property(self, name):
        property = Property(name)
        self.property.append(property)

    def view_property(self):
        for name in self.property:
            print(name)

    def create_household(self, name):
        household = Household(name)
        self.household.append(household)

    def view_household(self) -> None:
        for name in self.household:
            print(name)







