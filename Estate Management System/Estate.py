class Estate:

    def __init__(self, name:str, location:str) -> None:
        self.name = name
        self.location = location
        self.thoroughfare = []
        self.properties = []

    def __repr__(self):
        return f'Estate(name={self.name} County(location={self.location}'

    def __str__(self):
        return f'Estate(name={self.name} has {len(self.thoroughfare)} thoroughfares ' \
               f'and {len(self.properties)} properties.' \
               f'The current estate manager is {self.manager}.'

    def location(self):
        return self.location