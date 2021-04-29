from tkinter import *
from User import User

class User_Gui(Tk, User):
    def __init__(self):
        super(User_Gui, self).__init__()

        self.thoroughfare_label = Label()
        self.property_label = Label()
        self.household_label = Label()

        self.thoroughfare_list = Listbox()
        self.property_list = Listbox()
        self.household_list = Listbox()

        self.add_t_button = Button()

        self.add_p_button = Button()

        self.add_h_button = Button()

        self.add_u_button = Button()

        self.add_thoroughfare_label()
        self.add_thoroughfare_list()
        self.add_thoroughfare_button()
        self.add_property_label()
        self.add_property_list()
        self.add_property_button()
        self.add_household_label()
        self.add_household_list()
        self.add_household_button()

    def add_thoroughfare_label(self):
        # add
        self.thoroughfare_label.grid(row=0, column=0, columnspan=2)
        # style
        self.thoroughfare_label.configure(text="Thoroughfares")

    def add_thoroughfare_list(self):
        self.thoroughfare_list.grid(row=1, column=0, columnspan=2)

    def add_thoroughfare_button(self):
        self.add_t_button.grid(row=2, column=0, columnspan=2)
        self.add_t_button.configure(text="Add Thoroughfare")

    def add_property_label(self):
        # add
        self.property_label.grid(row=0, column=2, columnspan=2)
        # style
        self.property_label.configure(text="Properties")

    def add_property_list(self):
        self.property_list.grid(row=1, column=2, columnspan=2)

    def add_property_button(self):
        self.add_p_button.grid(row=2, column=2, columnspan=2)
        self.add_p_button.configure(text="Add Property")

    def add_household_label(self):
        # add
        self.household_label.grid(row=0, column=4, columnspan=2)
        # style
        self.household_label.configure(text="Households")

    def add_household_list(self):
        self.household_list.grid(row=1, column=4, columnspan=2)

    def add_household_button(self):
        self.add_h_button.grid(row=2, column=4, columnspan=2)
        self.add_h_button.configure(text="Add Household")


if __name__ == '__main__':
    gui = User_Gui()
    gui.mainloop()












