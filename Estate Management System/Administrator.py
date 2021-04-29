from Manager import Manager
from Estate import Estate

class Administrator(Manager):

    def __init__(self, name: str):
        super(Manager, self).__init__(name)
        self.name = name
        self.estate = []

    def __repr__(self):
        return f'Administrator={self.name}'

    def create_estate(self) -> Estate:
        Estate.id += 1
        estate = Estate(f"Estate {Estate.id}")
        self.estate.append(estate)
        print(self.estate)
        return Estate

    def remove_estate(self, estate:Estate) -> bool:
        if estate in self.estate:
            self.estate.remove(estate)
            return True
        else:
            return False

    def display_estate(self) -> None:
        for estate in self.estate:
            print(estate)




