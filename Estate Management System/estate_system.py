from admin import Admin
from manager import Manager
from user import User
from systemgui import System_Gui

class EstateSystem:

    def __init__(self):
        self.estates = []
        self.thoroughfare = []
        self.property = []
        self.household = []
        self.users = []
        self.users.append(Admin(self, "Chris"))
        self.users.append(Manager(self, "Luis"))
        self.users.append(User(self, "Jordan"))
        self.current_user = None
        self.current_estate = None
        self.current_thoroughfare = None
        self.current_property = None
        self.current_household = None

if __name__ == '__main__':
    system = EstateSystem()
    gui = System_Gui(system)
    gui.mainloop()