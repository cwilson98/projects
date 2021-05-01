from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from Estate import Estate
from Manager import Manager
from User_Gui import User_Gui

class Manager_Gui(User_Gui,Tk):

    def __init__(self, Estate_System):
        super().__init__(Manager)
        self.estate_system = Estate_System

        #list of components
        self.user_label = Label()


        self.user_list = Listbox()

        self.remove_t_button = Button()
        self.remove_p_button = Button()
        self.remove_h_button = Button()
        self.add_u_button = Button()
        self.remove_u_button = Button()

        #set window attributes
        self.title("Manager Menu")

        #add components
        self.remove_thoroughfare_button()

        self.remove_property_button()

        self.remove_household_button()
        self.add_user_label()
        self.add_user_button()
        self.remove_user_button()

    def remove_thoroughfare_button(self):
        self.remove_t_button.grid(row=3, column=0)
        self.remove_t_button.configure(text="Remove Thoroughfare")

    def remove_property_button(self):
        self.remove_p_button.grid(row=3, column=2)
        self.remove_p_button.configure(text="Remove Property")

    def remove_household_button(self):
        self.remove_h_button.grid(row=3, column=4)
        self.remove_h_button.configure(text="Remove Household")

    def add_user_label(self):
        # add
        self.user_label.grid(row=0, column=6)
        # style
        self.user_label.configure(text="Users")

    def add_user_button(self):
        self.add_u_button.grid(row=1, column=6)
        self.add_u_button.configure(text="Add User")
        self.add_u_button.bind("<ButtonRelease-1>", self.add_u_button_clicked)

    def add_u_button_clicked(self):
        user = self.estate_system.current_user
        name = simpledialog.askstring("User Creation", "Name of User")
        user.create_user(name)
        messagebox.showinfo("Create User", "User Created")

    def remove_user_button(self):
        self.remove_u_button.grid(row=2, column=6)
        self.remove_u_button.configure(text="Remove User")


if __name__ == '__main__':
    gui = Manager_Gui(Manager)
    gui.mainloop()
