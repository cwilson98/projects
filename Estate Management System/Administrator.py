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
        estate = Estate(f"Estate {Estate.id}")
        self.__estates.append(estate)
        return estate

    def __remove_estate(self) -> bool:
        name = input("What estate do you want to remove: ")
        if name in self.__estates:
            self.__estates.remove(name)
            return True
        else:
            print("Estate does not exist")
            return False

