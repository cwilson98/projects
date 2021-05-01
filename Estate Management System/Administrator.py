from Manager import Manager
from Estate import Estate


class Administrator(Manager):

    def __init__(self, estate_system, name: str):
        super().__init__(name)
        self.estate_system = estate_system
        self.name = name

    def __repr__(self):
        return f'Administrator={self.name}'

    def create_estate(self, name):
        estate = Estate(name)
        self.estate_system.append(estate)

    def remove_estate(self, name) -> bool:
        estate = Estate(name)
        self.estate_system.remove(estate)

    def display_estate(self) -> None:
        for estate in self.estate:
            print(estate)





