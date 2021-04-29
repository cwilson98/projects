from tkinter import *
from Estate import Estate
from User_Gui import User_Gui

class Manager_Gui(User_Gui, Tk):

    def __init__(self):
        super().__init__()
        self.manager = Estate.estate_manager

        #list of components
        self.user_label = Label()


        self.user_list = Listbox()

        self.remove_t_button = Button()
        self.remove_p_button = Button()
        self.remove_h_button = Button()
        self.remove_u_button = Button()

        #set window attributes
        self.title("Estate Management System")

        #add components
        self.remove_thoroughfare_button()

        self.remove_property_button()

        self.remove_household_button()
        self.add_user_label()
        self.add_user_list()
        self.add_user_button()
        self.remove_user_button()

    def remove_thoroughfare_button(self):
        self.remove_t_button.grid(row=2, column=1)
        self.remove_t_button.configure(text="Remove Thoroughfare")

    def remove_property_button(self):
        self.remove_p_button.grid(row=2, column=3)
        self.remove_p_button.configure(text="Remove Property")

    def remove_household_button(self):
        self.remove_h_button.grid(row=2, column=5)
        self.remove_h_button.configure(text="Remove Household")

    def add_user_label(self):
        # add
        self.user_label.grid(row=0, column=6, columnspan=2)
        # style
        self.user_label.configure(text="Users")

    def add_user_list(self):
        self.user_list.grid(row=1, column=6, columnspan=2)

    def add_user_button(self):
        self.add_u_button.grid(row=2, column=6)
        self.add_u_button.configure(text="Add User")

    def remove_user_button(self):
        self.remove_u_button.grid(row=2, column=7)
        self.remove_u_button.configure(text="Remove User")


if __name__ == '__main__':
    gui = Manager_Gui()
    gui.mainloop()
