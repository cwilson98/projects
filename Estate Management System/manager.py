from user import User

class Manager(User):

    def __init__(self, estate_system, username) -> None:
        super().__init__(estate_system, username)

    def remove_thoroughfare(self, name):
        for Thoroughfare in self.estate_system.thoroughfare:
            if Thoroughfare.name == name:
                self.estate_system.thoroughfare.remove(Thoroughfare)

    def remove_property(self, name):
        for Property in self.estate_system.property:
            if Property.name == name:
                self.estate_system.property.remove(Property)

    def remove_household(self, name):
        for Household in self.estate_system.household:
            if Household.name == name:
                self.estate_system.household.remove(Household)

    def create_user(self, name):
        user = User(self.estate_system, name)
        self.estate_system.users.append(user)

    def view_users(self):
        for user in self.estate_system.users:
            if isinstance(user, User):
                print(user)

    def remove_user(self, name):
        for User in self.estate_system.users:
            if User.username == name:
                self.estate_system.users.remove(User)
