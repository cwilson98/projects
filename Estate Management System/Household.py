from datetime import date


class Household:

    id = 0
    CUSTODIAN = 'Janitor'
    MSC = 1250
    MONEY = 100,000
    date = date.today()

    def __init__(self, name:str, custodian:str = CUSTODIAN, date:str = date, money:int = MONEY):
        self.name = name
        self.household = []
        self.custodian = custodian
        self.occupants = []
        self.date = date
        self.money = money

    def __repr__(self):
        return f'Name = {self.name}, Occupants = {len(self.occupants)}'

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

    def make_payment(self) -> bool:
        afterpay = self.money - Household.MSC
        if self.money >= Household.MSC:
            self.money = afterpay
            print(f"The Custodian {self.custodian} has made a payment of {Household.MSC}. The remaining balance is {self.money}")
        else:
            print("Insufficient Funds")
            return False

    def print_receipt(self):
        return f'{self.household} has made a payment of {Household.MSC} on {self.date}'


