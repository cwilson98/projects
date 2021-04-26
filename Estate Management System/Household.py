from random import randint

class Household:

    id = 0

    def __init__(self, name: str):
        self.name = name
        self.custodian = []

    def __repr__(self):
        return f'(name={self.name}, occupants={randint(0, 11)})'

    def __str__(self):
        return f'{self.name} currently has {randint(0, 11)} people residing there.'


    def population(self) -> int:
        return len(self.occupants)