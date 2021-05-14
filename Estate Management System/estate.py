from manager import Manager
from property import Property

class Estate:
    
    LOCATION = 'Southampton'
    id = 0
    MSC = 1250
    PRICE = 1000000

    def __init__(self, estate_system, name: str, manager: Manager = None, location: str = LOCATION) -> None:
        self.estate_system = estate_system
        self.name = name
        self.thoroughfare = []
        self.property = []
        self.location = location
        if manager is None:
            self.estate_manager = self.estate_system.current_user
        else:
            self.estate_manager = manager

    def __repr__(self) -> str:
        return f'Estate={self.name}, Country={self.location}, Manager={self.estate_manager}, \
                Thoroughfares={len(self.thoroughfare)}, Properties={len(self.property)}'

    def __str__(self):
        return f'{self.name} is located in {self.location}. The current manager is {self.estate_manager}. \
        It contains {len(self.thoroughfare)} thoroughfares and {len(self.property)} properties'

    def update_estate(self, name):
        self.name = name

    def change_manager(self, manager):
        self.estate_manager = manager

    def add_thoroughfare(self):
        for thoroughfare in self.estate_system.thoroughfare:
            self.thoroughfare.append(thoroughfare)

    def remove_thoroughfare(self):
        for thoroughfare in self.thoroughfare:
            self.thoroughfare.remove(thoroughfare)

    def add_property(self):
        for property in self.estate_system.property:
            self.property.append(property)

    def remove_property(self):
        for property in self.property:
            self.property.remove(property)

    def print_invoice(self):
        print(f"The price for {self.name} is {Estate.PRICE}")

