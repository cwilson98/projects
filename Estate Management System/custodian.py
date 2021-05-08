class Custodian:

    id = 0
    MONEY = 100,000

    def __init__(self, name: str, bank_account:int = 100000):
        self.name = name
        self.bank_account = bank_account

    def __str__(self):
        return f'The current custodian is {self.name}'

    def clean(self):
        self.bank_account += 100

    def cook(self):
        self.bank_account += 200
