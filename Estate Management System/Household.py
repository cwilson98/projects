class Household:

    def __init__(self, name: str):
        self.name = name
        self.occupants = []

    def __repr__(self):
        return f'(name={self.name}, occupants={len(self.occupants)})'

    def __str__(self):
        return f'{self.name} currently has {len(self.occupants)} people residing there '

    def display_custodian(self) -> str:
        return self.custodian

    def population(self) -> int:
        return len(self.occupants)