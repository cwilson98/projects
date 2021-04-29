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


    def add_occupant(self) -> None:
        Household.id += 1
        self.occupants.append(f'Human {Household.id}')

    def population(self) -> int:
        return len(self.occupants)

    def update_household(self) -> bool:
        options_menu = """Choose one of the options listed below:


                  [1] Change the name of the Custodian.
                  [2] Change the name of the Household.



                  """
        print(options_menu)
        ans = input("What will it be: ")
        if ans == '1':
            print(f"The current custodian is {self.custodian}")
            new_name = input("Enter the name of the new custodian: ")
            self.custodian = new_name
        elif ans == '2':
            print(f"The current name of the household is {self.name}")
            new_name = input("Enter a new name: ")
            self.name = new_name
        else:
            print("That's not an option.")
            return False


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


