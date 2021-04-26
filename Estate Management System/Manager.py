from User import User
from Thoroughfare import Thoroughfare
from Property import Property
from Household import Household
from User import User

class Manager(User):

    def __init__(self, name:str) -> None:
        self.name = name
        self.__user = []

    def remove_thoroughfare(self, thoroughfare:Thoroughfare) -> bool:
        if thoroughfare in self.thoroughfare:
            self.thoroughfare.remove(Thoroughfare)
            return True
        else:
            print("Thoroughfare does not exist")
            return False

    def remove_property(self, property:Property):
        if property in self.property:
            self.property.remove(property)
            return True
        else:
            print("Property does not exist")
            return False

    def remove_household(self, household:Household):
        if household in self.household:
            self.household.remove(Household)
            return True
        else:
            print("Household does not exist")
            return False

    def create_user(self, user:User) -> bool:
        self.__user.append(user)
        return (user in self.__user)

