from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog

class HouseholdGui(Tk):
    def __init__(self, estate_system, household):
        super().__init__()
        self.estate_system = estate_system
        self.household = household

        self.title(self.estate_system.current_household)
        self.configure(bg="#eee",
                       height=500,
                       width=500)

        self.change_names()
        self.change_names_button()
        self.occupant()
        self.add_occupant()
        self.remove_occupant()
        self.view_occupant()
        self.make_pay()
        self.make_pay_button()

    def change_names(self):
        self.change_name = Label()
        self.change_name.grid(row=0, column=0)
        self.change_name.configure(text="Change Name")

    def change_names_button(self):
        self.change_name_button = Button()
        self.change_name_button.grid(row=1, column=0)
        self.change_name_button.configure(text="Change Name")
        self.change_name_button.bind("<ButtonRelease-1>", self.change_button_clicked)

    def change_button_clicked(self, event):
        name = simpledialog.askstring("Name Change", "Name of Household")
        self.household.change_name(name)
        messagebox.showinfo("Change Name", "Name of Household Changed")


    def occupant(self):
        self.occupants = Label()
        self.occupants.grid(row=0, column=2)
        self.occupants.configure(text="Occupants")

    def add_occupant(self):
        self.add_occupants = Button()
        self.add_occupants.grid(row=1, column=2)
        self.add_occupants.configure(text="Add Occupants")
        self.add_occupants.bind("<ButtonRelease-1>", self.add_occupants_button_clicked)

    def add_occupants_button_clicked(self, event):
        self.household.add_occupant()
        messagebox.showinfo("Add Occupants", "Occupant added to household")

    def remove_occupant(self):
        self.remove_occupants = Button()
        self.remove_occupants.grid(row=2, column=2)
        self.remove_occupants.configure(text="Remove Occupants")
        self.remove_occupants.bind("<ButtonRelease-1>", self.remove_occupants_button_clicked)

    def remove_occupants_button_clicked(self, event):
        self.household.remove_occupant()
        messagebox.showinfo("Remove Occupants", "Occupant removed to household")

    def view_occupant(self):
        self.view_occupants = Button()
        self.view_occupants.grid(row=2, column=0)
        self.view_occupants.configure(text="Check Population")
        self.view_occupants.bind("<ButtonRelease-1>", self.view_occupants_button_clicked)

    def view_occupants_button_clicked(self, event):
        print(self.household)

    def make_pay(self):
        self.make_payment = Label()
        self.make_payment.grid(row=0, column=3)
        self.make_payment.configure(text="Household Payment")

    def make_pay_button(self):
        self.make_payment_button = Button()
        self.make_payment_button.grid(row=1, column=3)
        self.make_payment_button.configure(text="Make Payment")
        self.make_payment_button.bind("<ButtonRelease-1>", self.make_payment_button_clicked)

    def make_payment_button_clicked(self, event):
        self.household.make_payment()
        messagebox.showinfo("Make Payment", "Household Payment Made")








        