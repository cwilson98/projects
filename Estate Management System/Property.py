class Property:

    def __init__(self, name:str, type:str, location:str, owner:str, date:str):
        self.name = name
        self.location = location
        self.type = type
        self.owner = owner
        self.date = date

    def __repr__(self):
        return f'Property (name={self.name}, (type={self.type}, (location={self.location}, (owner={self.owner}, date={self.date})'

    def __str__(self):
        return f'{self.name} is a {self.type} located on {self.location}.'

    def ownership(self):
        return f'The property is owned by {self.owner}'

    def completion_date(self):
        return f'The property was completed on {self.date}'