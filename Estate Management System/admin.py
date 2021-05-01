from Estate import Estate
from Estate_Gui import Estate_Gui
from Manager import Manager

class admin(Manager):

    def __init__(self, username, Estate_System):
        super().__init__("Chris", Estate_System)
        self.username = username
        self.estate_system = Estate_System

    def create_estate(self, name):
        estate = Estate(name)
        self.estate_system.estates.append(estate)
        print(estate)

    def view_estate(self):
        for name in self.estate_system.estates:
            print(name)

    def update_estate(self, name):
        fd

    def remove_estate(self, name:Estate):
        if name in self.estate_system.estates:
            self.estate_system.estates.remove(name)
