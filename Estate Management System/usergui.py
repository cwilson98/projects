from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog

class User_Gui(Tk):
    def __init__(self, estatesystem):
        super().__init__()
        self.estate_system = estatesystem



        self.create_thoroughfare_label()
        self.create_thoroughfare_button()
        self.update_thoroughfare()
        self.view_thoroughfare_button()

        self.create_property_label()
        self.create_property_button()
        self.view_property_button()
        self.update_property()

        self.create_household_label()
        self.create_household_button()
        self.view_household_button()
        self.update_household()

        self.title(self.estate_system.current_user)
        self.configure(bg="#eee",
                       height=500,
                       width=500)

    def create_thoroughfare_label(self):
        self.thoroughfare_label = Label()
        # add
        self.thoroughfare_label.grid(row=0, column=1)
        # style
        self.thoroughfare_label.configure(text="Thoroughfares")

    def create_thoroughfare_button(self):
        self.create_t_button = Button()
        self.create_t_button.grid(row=1, column=1)
        self.create_t_button.configure(text="Create Thoroughfare")
        self.create_t_button.bind("<ButtonRelease-1>", self.create_t_button_clicked)

    def create_t_button_clicked(self, event):
        user = self.estate_system.current_user
        name = simpledialog.askstring("Thoroughfare Creation", "Name of Thoroughfare")
        user.create_thoroughfare(name)
        messagebox.showinfo("Create Thoroughfare", "Thoroughfare Created")

    def view_thoroughfare_button(self):
        self.view_t_button = Button()
        self.view_t_button.grid(row=2, column=1)
        self.view_t_button.configure(text="View Thoroughfares")
        self.view_t_button.bind("<ButtonRelease-1>", self.view_t_button_clicked)

    def view_t_button_clicked(self, event):
        user = self.estate_system.current_user
        user.view_thoroughfare()

    def update_thoroughfare(self):
        self.update_thoroughfare_button = Button()
        self.update_thoroughfare_button.configure(text="Update Thoroughfare")
        self.update_thoroughfare_button.grid(row=3, column=1)
        self.update_thoroughfare_button.bind("<ButtonRelease-1>", self.update_t_button_clicked)

    def update_t_button_clicked(self, event):
        user = self.estate_system.current_user
        name = simpledialog.askstring("Thoroughfare Update","Name of Estate")
        for thoroughfare in self.estate_system.thoroughfare:
            if thoroughfare.name == name:
                messagebox.showinfo("Update Thoroughfare", "Opening Thoroughfare Menu")
                self.destroy()
                self.estate_system.current_thoroughfare = name
                user.update_thoroughfare(name)
                break
            else:
                messagebox.showinfo("Update Thoroughfare", "Thoroughfare does not Exist")

    def create_property_label(self):
        self.property_label = Label()
        # add
        self.property_label.grid(row=0, column=2)
        # style
        self.property_label.configure(text="Properties")

    def create_property_button(self):
        self.create_p_button = Button()
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

    def update_property(self):
        self.update_property_button = Button()
        self.update_property_button.configure(text="Update Property")
        self.update_property_button.grid(row=3, column=2)
        self.update_property_button.bind("<ButtonRelease-1>", self.update_p_button_clicked)

    def update_p_button_clicked(self, event):
        user = self.estate_system.current_user
        name = simpledialog.askstring("Property Update","Name of Property")
        for property in self.estate_system.property:
            if property.name == name:
                messagebox.showinfo("Update Property", "Opening Property Menu")
                self.destroy()
                self.estate_system.current_property = name
                user.update_property(name)
                break
            else:
                messagebox.showinfo("Update Property", "Property does not Exist")


    def create_household_label(self):
        self.household_label = Label()
        # add
        self.household_label.grid(row=0, column=3)
        # style
        self.household_label.configure(text="Households")

    def create_household_button(self):
        self.create_h_button = Button()
        self.create_h_button.grid(row=1, column=3)
        self.create_h_button.configure(text="Create Household")
        self.create_h_button.bind("<ButtonRelease-1>", self.create_h_button_clicked)

    def create_h_button_clicked(self, event):
        user = self.estate_system.current_user
        name = simpledialog.askstring("Household Creation", "Name of Household")
        user.create_household(name)
        messagebox.showinfo("Create Household", "Household created")

    def view_household_button(self):
        self.view_h_button = Button()
        self.view_h_button.grid(row=2, column=3)
        self.view_h_button.configure(text="View Household")
        self.view_h_button.bind("<ButtonRelease-1>", self.view_h_button_clicked)

    def view_h_button_clicked(self, event):
        user = self.estate_system.current_user
        user.view_household()

    def update_household(self):
        self.update_household_button = Button()
        self.update_household_button.configure(text="Update Household")
        self.update_household_button.grid(row=3, column=3)
        self.update_household_button.bind("<ButtonRelease-1>", self.update_h_button_clicked)

    def update_h_button_clicked(self, event):
        user = self.estate_system.current_user
        name = simpledialog.askstring("Estate Household","Name of Household")
        for household in self.estate_system.household:
            if household.name == name:
                messagebox.showinfo("Update Household", "Opening Household Menu")
                self.destroy()
                self.estate_system.current_household = name
                user.update_household(name)
                break
            else:
                messagebox.showinfo("Update Household", "Household does not Exist")
