from datetime import date
from Household import Household
import random

class Property:

    TYPE = ['detached house', 'semi-detached house', 'terrace house', 'a block of flats']
    id = 0
    DATE = date.today()
    OWNER = 'DaBaby'
    ADDRESS = ['Ares 1', 'Ares 2', 'Ares 3', 'Ares 4', 'Ares 5']

    def __init__(self, name:str, address:str = ADDRESS, type:str = TYPE, date:str = DATE, owner:str = OWNER):
        self.name = name
        self.type = random.choice(type)
        self.address = random.choice(address)
        self.date = date
        self.owner = owner
        self.household = []

    def __repr__(self):
        return f'Name = {self.name}, Type = {self.type}, Owner = {self.owner}, Completion Date = {self.date}'

    def __str__(self):
        return f'{self.name} is a {self.type} with {len(self.household)} households.'

    def completion_date(self):
        return f'The property was completed on {self.date}'

    def add_household(self, household:Household) -> bool:
        if household:
            self.household.append(household)
            return True
        else:
            return False

    def update_property(self) -> True:

            print("What option would you like to choose: ")
            options_menu = """Choose one of the options listed below:


                             [1] Change the owner of the property
                             [2] Change the name of the property



                             """
            print(options_menu)
            ans = input("What will it be: ")
            if ans == '1':
                new_owner = input("Enter a new owner for the property: ")
                self.owner = new_owner
                print(self.owner)
                return True
            elif ans == '2':
                new_name = input("Enter a new name for the property: ")
                self.name = new_name
                return True
            else:
                print("That's not an option.")
                return False

    def remove_household(self, household:Household) -> bool:
        if household in self.household:
            self.household.remove(household)
            return True
        else:
            return False

    def display_households(self) -> None:
        for house in self.household:
            print(house)
