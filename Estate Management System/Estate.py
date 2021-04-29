from Thoroughfare import Thoroughfare
from Property import Property

class Estate:
    
    LOCATION = 'Southampton'
    managers = ['Ryan', 'Cisco', 'Manuel', 'Wilson']
    estate_manager = 'Wilson'
    id = 0

    def __init__(self, name: str, manager:str = estate_manager, location: str = LOCATION) -> None:
        self.__name = name
        self.__thoroughfare = []
        self.__property = []
        self.__location = location
        self.__manager = manager

    def __repr__(self) -> str:
        return f'Estate={self.__name}, Country={self.__location}, Manager={self.__manager}, Thoroughfares={len(self.__thoroughfare)}, Properties={len(self.__property)}'

    def __str__(self):
        return f'{self.__name} is located in {self.__location}. The current manager is {self.__manager}.' \
               f'It contains {len(self.__thoroughfare)} thoroughfares and {len(self.__property)} proerties'



    def __update_estate(self) -> bool:
        print("What option would you like to choose: ")
        options_menu = """Choose one of the options listed below:


                  [1] Change the Manager. 
                  [2] Change the name of the Estate



                  """
        print(options_menu)
        ans = input("What will it be: ")
        if ans == '1':
            print(f"The current manager is {self.__manager}")
            print("Here is a list of the managers.")
            print(Estate.managers)
            choice = input("Choose one: ")
            if choice in Estate.managers:
                self.__manager = choice
                return True
            else:
                print("Manager does not exist")
                return False
        elif ans == '2':
            print(f"The current name is {self.name}")
            new_name = input("Enter a new name: ")
            self.name = new_name
        else:
            print("That's not an option.")
            return False

    def add_thoroughfare(self, thoroughfare:Thoroughfare) -> bool:
        if thoroughfare:
            self.__thoroughfare.append(thoroughfare)
            return True
        else:
            return False

    def remove_thoroughfare(self, thoroughfare:Thoroughfare) -> bool:
        if thoroughfare in self.__thoroughfare:
            self.__thoroughfare.remove(thoroughfare)
            return True
        else:
            return False

    def add_property(self, property:Property) -> bool:
        if property:
            self.__property.append(property)
            return True
        else:
            return False

    def remove_property(self, property:Property) -> bool:
        if property in self.__property:
            self.__property.remove(property)
            return True
        else:
            return False

    def thoroughfares(self) -> int:
        return len(self.__thoroughfare)

    def properties(self) -> int:
        return len(self.__property)
