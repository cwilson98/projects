from Thoroughfare import Thoroughfare
from Property import Property
from Household import Household
from Custodian import Custodian
import random
from typing import List

class User:
    def __init__(self, name: str):
        self.name = name
        self.thoroughfare = []
        self.property = []
        self.household = []
        self.custodian = []

    def __str__(self):
        return f'Hello {self.name}'

    def add_thoroughfare(self, names: List[str]) -> None:
        for name in names:
            thoroughfare = Thoroughfare(
                f"{name} {random.choice(['Street', 'Close', 'Avenue', 'Crescent', 'Lane', 'Court', 'Road'])}")
            self.thoroughfare.append(thoroughfare)

    def display_thoroughfare(self) -> None:
        for thorough in self.thoroughfare:
            print(thorough)

    def update_thoroughfare(self) -> bool:
        for path in self.thoroughfare:
            print(path)
        replace = input("Which name do you want to change: ")
        if replace in self.thoroughfare:
            self.thoroughfare.remove(replace)
            addition = input("What other street do you want: ")
            self.thoroughfare.append(addition)
            return True
        else:
            print("Pathway does not exit.")
            return False

    def add_property(self) -> Property:
        Property.id += 1
        property = Property(f"Property {Property.id}")
        self.property.append(property)
        return property

    def display_properties(self) -> None:
        for prop in self.property:
            print(prop)

    def add_household(self) -> Household:
        Household.id += 1
        household = Household(f"Household {Household.id}")
        self.household.append(household)
        return household

    def display_households(self) -> None:
        for house in self.household:
            print(house)

    def add_custodian(self) -> Custodian:
        Custodian.id += 1
        custodian = Custodian(f"Butler {Custodian.id}")
        self.custodian.append(custodian)
        return custodian

    def display_custodians(self) -> None:
        for emp in self.custodian:
            print(emp)




