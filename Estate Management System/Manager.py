from Thoroughfare import Thoroughfare
from Property import Property
from Household import Household
from Estate import Estate
from User import User

class Manager(User):

    def __init__(self, username:str, Estate_System) -> None:
        super().__init__("Frankie", Estate_System)
        self.username = username
        self.user = []
        self.estate_system = Estate_System

    def remove_thoroughfare(self, thoroughfare:Thoroughfare) -> bool:
        if thoroughfare in self.thoroughfare:
            self.thoroughfare.remove(Thoroughfare)
            return True
        else:
            print("Thoroughfare does not exist")
            return False

    def remove_property(self, property:Property) -> bool:
        if property in self.property:
            self.property.remove(property)
            return True
        else:
            print("Property does not exist")
            return False

    def remove_household(self, household:Household) -> bool:
        if household in self.household:
            self.household.remove(Household)
            return True
        else:
            print("Household does not exist")
            return False

    def create_user(self, name):
        name = User(name)
        self.estate_system.users.append(name)

    def view_all_invoices(self):
        return f"The price for the entire estate is {len(self.household)} * {Estate.MSC}"
