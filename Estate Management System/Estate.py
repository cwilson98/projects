from typing import List

class Estate:

    def __init__(self, name:str, location:str) -> None:
        self.name = name
        self.location = location

    def __repr__(self):
        return f'Estate={self.name}, Country={self.location}'

    def __str__(self):
        return f'{self.name} is located in {self.location}'

    def __create_estate(self) -> Estate:
        for name in names:
            estate = Estate(name)
            self.name.append(estate)

    def remove_estate(self) -> bool:
        if estate in self.name:
            self.name.remove(estate)
            return True
        else:
            print("Estate does not exist")
            return False