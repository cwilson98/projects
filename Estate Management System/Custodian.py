from Household import Household

class Custodian:

    id = 0

    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f'The current custodian is {self.name}'

    def clean(self, Household):
        pass

    def cook(self, Household):
        pass