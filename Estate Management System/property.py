from datetime import date
import random

class Property:

    TYPE = ['detached house', 'semi-detached house', 'terrace house', 'a block of flats']
    id = 0
    DATE = date.today()
    OWNER = 'DaBaby'
    ADDRESS = ['Ares 1', 'Ares 2', 'Ares 3', 'Ares 4', 'Ares 5']

    def __init__(self, estate_system, name:str, address:str = ADDRESS, type:str = TYPE, date:str = DATE, owner:str = OWNER):
        self.estate_system = estate_system
        self.name = name
        self.type = random.choice(type)
        self.address = random.choice(address)
        self.date = date
        self.owner = owner
        self.household = []

    def __repr__(self):
        return f'Name = {self.name}, Type = {self.type}, Owner = {self.owner}, Completion Date = {self.date}'

    def __str__(self):
        return f'{self.name} is a {self.type} with {len(self.household)} households. The property was completed on {self.date}. The current owner is {self.owner} '

    def add_household(self):
        for household in self.estate_system.household:
            self.household.append(household)

    def change_name(self, name):
        self.name = name

    def change_owner(self, name):
        self.owner = name

    def remove_household(self):
        for Household in self.estate_system.household:
            self.household.remove(Household)

