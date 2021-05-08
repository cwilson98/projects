from thoroughfare import Thoroughfare
from property import Property
from household import Household
from thoroughfaregui import ThoroughfareGui
from propertygui import PropertyGui
from householdgui import HouseholdGui
import random

class User:

    id = 0

    def __init__(self, estate_system, username):
        self.username = username
        self.estate_system = estate_system

    def __str__(self):
        return f"{self.username}"

    def create_thoroughfare(self, name):
        thoroughfare = Thoroughfare(self.estate_system, f'{name} {random.choice(Thoroughfare.PATHWAY)}')
        self.estate_system.thoroughfare.append(thoroughfare)

    def view_thoroughfare(self):
        for name in self.estate_system.thoroughfare:
            print(name)

    def update_thoroughfare(self, name):
        for thoroughfare in self.estate_system.thoroughfare:
            if thoroughfare.name == name:
                thoroughfaregui = ThoroughfareGui(self.estate_system, thoroughfare)
                thoroughfaregui.mainloop()
                break

    def create_property(self, name):
        property = Property(self.estate_system, name)
        self.estate_system.property.append(property)

    def view_property(self):
        for name in self.estate_system.property:
            print(name)

    def update_property(self, name):
        for property in self.estate_system.property:
            if property.name == name:
                propertygui = PropertyGui(self.estate_system, property)
                propertygui.mainloop()
                break

    def create_household(self, name):
        household = Household(self.estate_system, name)
        self.estate_system.household.append(household)

    def view_household(self) -> None:
        for name in self.estate_system.household:
            print(name)

    def update_household(self, name):
        for household in self.estate_system.household:
            if household.name == name:
                householdgui = HouseholdGui(self.estate_system, household)
                householdgui.mainloop()
                break








