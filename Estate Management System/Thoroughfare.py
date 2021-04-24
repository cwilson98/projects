class Thoroughfare:

    def __init__(self, name: str) -> None:
        self.name = name
        self.properties = []

    def __repr__(self):
        return f'Thoroughfare(name={self.name}'

    def __str__(self):
        return f'Thoroughfare(name={self.name} has {len(self.properties)} properties.' \
               f'It is located in the {self.estate} Estate'

