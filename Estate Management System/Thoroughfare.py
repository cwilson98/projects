from Property import Property
import random

class Thoroughfare:

    id = 0
    PATHWAY = ['Street', 'Close', 'Avenue', 'Crescent', 'Lane', 'Court', 'Road']

    def __init__(self, name:str) -> None:
        self.name = name
        self.property = []

    def __repr__(self):
        return f'Name = {self.name}, Properties = {len(self.property)} '

    def __str__(self):
        return f'{self.name} has {len(self.property)} properties'

    def update_thoroughfare(self) -> None:
        rename = input("What is the new name of the thoroughfare: ")
        self.name = (F"{rename} {random.choice(Thoroughfare.PATHWAY)}")

    def add_property(self, property:Property) -> bool:
        for property in self.property:
            self.property.append(property)
            return True
        else:
            return False






