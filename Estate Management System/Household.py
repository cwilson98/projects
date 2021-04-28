import random
from datetime import date
from Custodian import Custodian


class Household:

    id = 0
    CUSTODIAN = 'Janitor'
    PRICE = (100,000)
    REFNUM = random.randint(1, 9999999999999999999999999999999999999999999999999999999999999)
    date = date.today()

    def __init__(self, name:str, custodian:str = CUSTODIAN, date:str = date):
        self.name = name
        self.household = []
        self.custodian = custodian
        self.occupants = []
        self.date = date

    def __repr__(self):
        return f'(name={self.name}, occupants={len(self.occupants)})'

    def __str__(self):
        return f'{self.name} currently has {len(self.occupants)} people residing there.'

    def display_households(self) -> None:
        for house in self.household:
            print(house)

    def add_occupant(self) -> None:
        Household.id += 1
        self.occupants.append(f'Human {Household.id}')

    def population(self) -> int:
        return len(self.occupants)

    def generate_invoice(self) -> None:
        print(f'{self.household} is sold by Solent Council')
        print(Household.PRICE)
        print(Household.REFNUM)

    def receive_payment(self) -> bool:
        if Custodian.MONEY >= Household.PRICE:
            cheddar = Custodian.MONEY - Household.PRICE
            print("Remaining Balance is " + cheddar)
            return True
        else:
            print("Insufficient Funds")
            return False

    def print_receipt(self):
        return f'{self.household} had been purchased by {self.custodian} on {self.date}'


