from datetime import date

class Household:

    id = 0
    CUSTODIAN = 'Custodian'
    MSC = 1250
    MONEY = 100,000
    date = date.today()

    def __init__(self, estate_system, name:str, custodian:str = CUSTODIAN, date:str = date, money:int = MONEY, occupants:int = 1):
        self.estate_system = estate_system
        self.name = name
        self.household = []
        self.custodian = custodian
        self.occupants = occupants
        self.date = date
        self.money = money

    def __repr__(self):
        return f'Name = {self.name}, Occupants = {self.occupants}'

    def __str__(self):
        return f'{self.name} has {self.occupants} occupants.'

    def add_occupant(self) -> None:
        self.occupants += 1

    def remove_occupant(self):
        self.occupants -= 1

    def change_name(self, name):
        self.name = name

    def make_payment(self, payment):
            if payment >= Household.MSC:
                self.money = payment - Household.MSC
            elif payment < Household.MSC:
                self.money = 0





