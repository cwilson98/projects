from Manager import Manager
from Estate import Estate
from typing import List

class Admin(Manager):

    def __init__(self, name: str):
        self.__name = name
        self.__estates = []

    def __repr__(self):
        return f'Administrator={self.__name}'

    def __create_estate(self) -> Estate:
        estate = Estate("Random")
        self.__estates.append(estate)
        return estate

    def add_manager(self, manager: Manager) -> bool:
        if manager:
            self.__manager.append(manager)
            return True
        else:
            return False

