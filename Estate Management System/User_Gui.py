from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from User import User

class User_Gui(Tk, User):
    def __init__(self, Estate_System):
        super().__init__()
        self.estate_system = Estate_System

        self.thoroughfare_label = Label()
        self.property_label = Label()
        self.household_label = Label()

        self.create_t_button = Button()
        self.create_p_button = Button()
        self.create_h_button = Button()

        self.create_thoroughfare_label()
        self.create_thoroughfare_button()
        self.view_thoroughfare_button()

        self.create_property_label()
        self.create_property_button()
        self.view_property_button()

        self.create_household_label()
        self.create_household_button()
        self.view_household_button()

        self.title("User Menu")
        self.configure(bg="#eee",
                       height=500,
                       width=500)

    def create_thoroughfare_label(self):
        # add
        self.thoroughfare_label.grid(row=0, column=0)
        # style
        self.thoroughfare_label.configure(text="Thoroughfares")

    def create_thoroughfare_button(self):
        self.create_t_button.grid(row=1, column=0)
        self.create_t_button.configure(text="Create Thoroughfare")
        self.create_t_button.bind("<ButtonRelease-1>", self.create_t_button_clicked)

    def create_t_button_clicked(self, event):
        user = self.estate_system.current_user
        name = simpledialog.askstring("Thoroughfare Creation", "Name of Thoroughfare")
        user.create_thoroughfare(name)
        messagebox.showinfo("Create Thoroughfare", "Thoroughfare Created")

    def view_thoroughfare_button(self):
        self.view_t_button = Button()
        self.view_t_button.grid(row=2, column=0)
        self.view_t_button.configure(text="View Thoroughfares")
        self.view_t_button.bind("<ButtonRelease-1>", self.view_t_button_clicked)

    def view_t_button_clicked(self, event):
        user = self.estate_system.current_user
        user.view_thoroughfare()

    def create_property_label(self):
        # add
        self.property_label.grid(row=0, column=2)
        # style
        self.property_label.configure(text="Properties")

    def create_property_button(self):
        self.create_p_button.grid(row=1, column=2)
        self.create_p_button.configure(text="Create Property")
        self.create_p_button.bind("<ButtonRelease-1>", self.create_p_button_clicked)

    def create_p_button_clicked(self, event):
        user = self.estate_system.current_user
        name = simpledialog.askstring("Property Creation", "Name of Property")
        user.create_property(name)
        messagebox.showinfo("Create Property", "Property Created")

    def view_property_button(self):
        self.view_p_button = Button()
        self.view_p_button.grid(row=2, column=2)
        self.view_p_button.configure(text="View Properties")
        self.view_p_button.bind("<ButtonRelease-1>", self.view_p_button_clicked)

    def view_p_button_clicked(self, event):
        user = self.estate_system.current_user
        user.view_property()

    def create_household_label(self):
        # add
        self.household_label.grid(row=0, column=4)
        # style
        self.household_label.configure(text="Households")

    def create_household_button(self):
        self.create_h_button.grid(row=1, column=4)
        self.create_h_button.configure(text="Create Household")
        self.create_h_button.bind("<ButtonRelease-1>", self.create_h_button_clicked)

    def create_h_button_clicked(self, event):
        user = self.estate_system.current_user
        name = simpledialog.askstring("Household Creation", "Name of Household")
        user.create_household(name)
        messagebox.showinfo("Create Household", "Household created")

    def view_household_button(self):
        self.view_h_button = Button()
        self.view_h_button.grid(row=2, column=4)
        self.view_h_button.configure(text="View Household")
        self.view_h_button.bind("<ButtonRelease-1>", self.view_h_button_clicked)

    def view_h_button_clicked(self, event):
        user = self.estate_system.current_user
        user.view_household()

if __name__ == '__main__':
    gui = User_Gui(User)
    gui.mainloop()


















