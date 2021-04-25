from Thoroughfare import Thoroughfare
from Property import Property
from Household import Household

class Basic_System_User:
    def __init__(self, name: str):
        self.name = name
        self.thoroughfare = []
        self.property = []
        self.household = []

    def create_thoroughfare(self, thoroughfare: Thoroughfare) -> bool:
        if thoroughfare not in self.thoroughfare:
            self.thoroughfare.append(Thoroughfare)
            return True
        else:
            print("Thoroughfare already exists.")
            return False

    def view_thoroughfare(self):
        return self.thoroughfare

    def update:

    def create_property(self, property: Property) -> bool:
        if property not in self.property:
            self.property.append(Property)
            return True
        else:
            print("Property already exists.")
            return False

    def create_household(self, household: Household) -> bool:
        if household not in self.household:
            self.household.append(household)
            return True
        else:
            print("Household already exists.")
            return False



    def generate_invoice(self, household):
        household = input("Which household would you like to choose: ")
        print(household)

