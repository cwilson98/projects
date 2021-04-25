class Estate:

    def __init__(self, name:str, location:str) -> None:
        self.name = name
        self.location = location

    def __repr__(self):
        return f'Estate(name={self.name} County(location={self.location}'

    def __str__(self):
        return f'Estate(name={self.name} is located in(location={self.location}'
