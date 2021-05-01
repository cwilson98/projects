from admin import admin
from System_Gui import System_Gui


class Estate_System():

    def __init__(self):
        self.estates = []
        self.users = []
        self.users.append(admin(self,"Chris"))
        self.current_user = None

if __name__ == '__main__':
    system = Estate_System()
    gui = System_Gui(system)
    gui.mainloop()