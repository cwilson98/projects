from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog

class PropertyGui(Tk):
    def __init__(self, estate_system, property):
        super().__init__()
        self.estate_system = estate_system
        self.property = property

        self.title(self.estate_system.current_property)
        self.configure(bg="#eee",
                       height=500,
                       width=500)




        self.household_labell()
        self.add_household_button()
        self.remove_household_button()
        self.change_name()
        self.change_button()
        self.change_owner()
        self.view_property()


    def change_name(self):
        self.change_name_label = Label()
        self.change_name_label.grid(row=0, column=0)
        self.change_name_label.configure(text="Property")

    def change_button(self):
        self.change_name_button = Button()
        self.change_name_button.grid(row=1, column=0)
        self.change_name_button.configure(text="Change Name")
        self.change_name_button.bind("<ButtonRelease-1>", self.change_button_clicked)

    def change_button_clicked(self, event):
        name = simpledialog.askstring("Name Change", "Name of Property")
        self.property.change_name(name)
        messagebox.showinfo("Change Name", "Name Successfully Changed")

    def change_owner(self):
        self.owner_button = Button()
        self.owner_button.grid(row=2, column=0)
        self.owner_button.configure(text="Change Owner")
        self.owner_button.bind("<ButtonRelease-1>", self.change_owner_button_clicked)

    def change_owner_button_clicked(self, event):
        name = simpledialog.askstring("Owner Change", "Name of Owner")
        self.property.change_owner(name)
        messagebox.showinfo("Change Owner", "Owner Successfully Changed")

    def view_property(self):
        self.view_property_button = Button()
        self.view_property_button.grid(row=3, column=0)
        self.view_property_button.configure(text="View Property")
        self.view_property_button.bind("<ButtonRelease-1>", self.view_property_button_clicked)

    def view_property_button_clicked(self, event):
        print(self.property)

    def household_labell(self):
        # add
        self.household_label = Label()
        self.household_label.grid(row=0, column=1)
        # style
        self.household_label.configure(text="Households")

    def add_household_button(self):
        self.add_h_button = Button()
        self.add_h_button.grid(row=1, column=1)
        self.add_h_button.configure(text="Add Households")
        self.add_h_button.bind("<ButtonRelease-1>", self.add_h_button_clicked)

    def add_h_button_clicked(self, event):
        self.property.add_household()
        messagebox.showinfo("Add Household", "Households added to Property")

    def remove_household_button(self):
        self.remove_h_button = Button()
        self.remove_h_button.grid(row=2, column=1)
        self.remove_h_button.configure(text="Remove Households")
        self.remove_h_button.bind("<ButtonRelease-1>", self.remove_h_button_clicked)

    def remove_h_button_clicked(self, event):
        self.property.remove_household()
        messagebox.showinfo("Remove Household", "Households removed from Property")
