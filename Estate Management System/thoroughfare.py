import random

class Thoroughfare:

    id = 0
    PATHWAY = ['Street', 'Close', 'Avenue', 'Crescent', 'Lane', 'Court', 'Road']

    def __init__(self, estate_system, name:str) -> None:
        self.estate_system = estate_system
        self.name = name
        self.property = []

    def __repr__(self):
        return f'Name = {self.name}, Properties = {len(self.property)} '

    def __str__(self):
        return f'{self.name} has {len(self.property)} properties.'

    def change_name(self, name) -> None:
        self.name = (F"{name} {random.choice(Thoroughfare.PATHWAY)}")

    def add_property(self):
        for Property in self.estate_system.property:
            self.property.append(Property)

    def remove_property(self):
        for Property in self.property:
            self.property.remove(Property)






