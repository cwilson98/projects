from Thoroughfare import Thoroughfare
from Property import Property

class Estate:
    
    LOCATION = 'Southampton'
    managers = ['Ryan', 'Cisco', 'Manuel']
    estate_manager = 'Frankie'
    id = 0
    MSC = 1250

    def __init__(self, name: str, manager:str = estate_manager, location: str = LOCATION) -> None:
        self.name = name
        self.thoroughfare = []
        self.property = []
        self.location = location
        self.manager = manager

    def __repr__(self) -> str:
        return f'Estate={self.name}, Country={self.location}, Manager={self.manager}, \
                Thoroughfares={len(self.thoroughfare)}, Properties={len(self.property)}'

    def __str__(self):
        return f'{self.name} is located in {self.location}. The current manager is {self.manager}. \
        It contains {len(self.thoroughfare)} thoroughfares and {len(self.property)} properties'



    def update_estate(self) -> bool:
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
            self.thoroughfare.append(thoroughfare)
            return True
        else:
            return False

    def remove_thoroughfare(self, thoroughfare:Thoroughfare) -> bool:
        if thoroughfare in self.thoroughfare:
            self.thoroughfare.remove(thoroughfare)
            return True
        else:
            return False

    def add_property(self, property:Property) -> bool:
        if property:
            self.property.append(property)
            return True
        else:
            return False

    def remove_property(self, property:Property) -> bool:
        if property in self.property:
            self.property.remove(property)
            return True
        else:
            return False

    def thoroughfares(self) -> int:
        return len(self.thoroughfare)

    def properties(self) -> int:
        return len(self.property)

    def invoice(self) -> str:
        return f"The monthly service charge is ${Estate.MSC}"
