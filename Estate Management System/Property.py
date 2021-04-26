from Thoroughfare import Thoroughfare
from datetime import date

class Property(Thoroughfare):

    type = 'detached house'
    id = 0
    date = date.today()
    location = Thoroughfare

    def __init__(self, name:str):
        self.name = name
        self.type = type
        self.address = []
        self.date = date
        self.location = location

    def __repr__(self):
        return f'Property (name={self.name}, (type={self.type}, (location={self.location}, (owner={self.owner}, date={self.date})'

    def __str__(self):
        return f'{self.name} is a {self.type} located on .'

    def ownership(self):
        return f'The property is owned by {self.owner}'

    def completion_date(self):
        return f'The property was completed on {self.date}'