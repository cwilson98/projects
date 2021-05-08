from estate import Estate
from manager import Manager
from estate_gui import EstateGui

class Admin(Manager):

    def __init__(self, estate_system, username):
        super().__init__(estate_system, username)

    def create_estate(self, name):
        estate = Estate(self.estate_system, name)
        self.estate_system.estates.append(estate)

    def view_estate(self):
        for name in self.estate_system.estates:
            print(name)

    def update_estate(self, name):
        for estate in self.estate_system.estates:
            if estate.name == name:
                estategui = EstateGui(self.estate_system, estate)
                estategui.mainloop()
                break

    def remove_estate(self, name):
        for Estate in self.estate_system.estates:
            if Estate.name == name:
                self.estate_system.estates.remove(Estate)

    def create_manager(self, name):
        manager = Manager(self.estate_system, name)
        self.estate_system.users.append(manager)

    def remove_manager(self, name):
        for Manager in self.estate_system.users:
            if Manager.username == name:
                self.estate_system.users.remove(Manager)

    def view_managers(self):
        for user in self.estate_system.users:
            if isinstance(user, Manager):
                print(user)