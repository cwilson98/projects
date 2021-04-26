from typing import List
import random

class Thoroughfare:

    id = 0

    def __init__(self, name: str) -> None:
        self.__name = name
        self.__thoroughfares = []

    def __repr__(self):
        return f'Thoroughfare={len(self.__thoroughfares)}'

    def __str__(self):
        return f'The current thoroughfare is {self.__name}'

    def add_thoroughfare(self, names:List[str]) -> None:
        for name in names:
            thoroughfare = Thoroughfare(f"{name} {random.choice(['Street', 'Close', 'Avenue', 'Crescent', 'Lane', 'Court', 'Road'])}")
            self.__thoroughfares.append(thoroughfare)

    def display_thoroughfare(self) -> None:
        for path in self.__thoroughfares:
            print(path)

    def update_thoroughfare(self) -> bool:
        for path in self.__thoroughfares:
            print(path)
        replace = input("Which name do you want to change: ")
        if replace in self.__thoroughfares:
            self.__thoroughfares.remove(replace)
            addition = input("What other street do you want: ")
            self.__thoroughfares.append(addition)
            return True
        else:
            print("Pathway does not exit.")
            return False



