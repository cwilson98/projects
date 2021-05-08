from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from usergui import User_Gui

class Manager_Gui(User_Gui,Tk):

    def __init__(self, estate_system):
        super().__init__(estate_system)
        self.estate_system = estate_system

        #list of components
        self.user_label = Label()

        self.remove_t_button = Button()
        self.remove_p_button = Button()
        self.remove_h_button = Button()
        self.add_u_button = Button()
        self.view_users()
        self.remove_u_button = Button()

        #set window attributes
        self.title(self.estate_system.current_user)
        self.configure(bg="#eee",
                       height=500,
                       width=500)

        #add components
        self.remove_thoroughfare_button()

        self.remove_property_button()

        self.remove_household_button()
        self.add_user_label()
        self.add_user_button()
        self.remove_user_button()

    def remove_thoroughfare_button(self):
        self.remove_t_button.grid(row=4, column=1)
        self.remove_t_button.configure(text="Remove Thoroughfare")
        self.remove_t_button.bind("<ButtonRelease-1>", self.remove_t_button_clicked)

    def remove_t_button_clicked(self, event):
        user = self.estate_system.current_user
        name = simpledialog.askstring("Thoroughfare Removal", "Name of Thoroughfare")
        user.remove_thoroughfare(name)
        messagebox.showinfo("Remove Thoroughfare", "Thoroughfare Deleted")

    def remove_property_button(self):
        self.remove_p_button.grid(row=4, column=2)
        self.remove_p_button.configure(text="Remove Property")
        self.remove_p_button.bind("<ButtonRelease-1>", self.remove_p_button_clicked)

    def remove_p_button_clicked(self, event):
        user = self.estate_system.current_user
        name = simpledialog.askstring("Property Removal", "Name of Property")
        user.remove_property(name)
        messagebox.showinfo("Remove Property", "Property Deleted")

    def remove_household_button(self):
        self.remove_h_button.grid(row=4, column=3)
        self.remove_h_button.configure(text="Remove Household")
        self.remove_h_button.bind("<ButtonRelease-1>", self.remove_h_button_clicked)

    def remove_h_button_clicked(self, event):
        user = self.estate_system.current_user
        name = simpledialog.askstring("Household Removal", "Name of Household")
        user.remove_household(name)
        messagebox.showinfo("Remove Household", "Household Deleted")

    def add_user_label(self):
        # add
        self.user_label.grid(row=12, column=3)
        # style
        self.user_label.configure(text="User")

    def add_user_button(self):
        self.add_u_button.grid(row=13, column=3)
        self.add_u_button.configure(text="Create User")
        self.add_u_button.bind("<ButtonRelease-1>", self.add_u_button_clicked)

    def add_u_button_clicked(self, event):
        user = self.estate_system.current_user
        name = simpledialog.askstring("User Creation", "Name of User")
        user.create_user(name)
        messagebox.showinfo("Create User", "User Created")

    def view_users(self):
        self.view_user_button = Button()
        self.view_user_button.configure(text="View Users")
        self.view_user_button.grid(row=14, column=3)
        self.view_user_button.bind("<ButtonRelease-1>", self.view_u_button_clicked)

    def view_u_button_clicked(self, event):
        user = self.estate_system.current_user
        user.view_users()

    def remove_user_button(self):
        self.remove_u_button.grid(row=15, column=3)
        self.remove_u_button.configure(text="Remove User")
        self.remove_u_button.bind("<ButtonRelease-1>", self.remove_u_button_clicked)

    def remove_u_button_clicked(self, event):
        user = self.estate_system.current_user
        name = simpledialog.askstring("User Delete", "Name of User")
        user.remove_user(name)
        messagebox.showinfo("Remove User", "User Deleted")


