from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from manager import Manager
from estate import Estate


class EstateGui(Tk):
    def __init__(self, estate_system, estate):
        super().__init__()
        self.estate_system = estate_system
        self.estate = estate

        self.change_name()
        self.change_button()
        self.change_manager()
        self.view_estate()
        self.add_Thoroughfare()
        self.add_Thoroughfare_button()
        self.remove_Thoroughfare_button()
        self.property_label()
        self.add_property()
        self.remove_property()
        self.view_invoice()

        self.title(self.estate_system.current_estate)
        self.configure(bg="#eee",
                       height=500,
                       width=500)


    def change_name(self):
        self.change_name_label = Label()
        self.change_name_label.configure(text="Estate")
        self.change_name_label.grid(row=0, column=0)

    def change_button(self):
        self.change_name_button = Button()
        self.change_name_button.configure(text="Name Change")
        self.change_name_button.grid(row=1, column=0)
        self.change_name_button.bind("<ButtonRelease-1>", self.change_clicked)

    def change_clicked(self, event):
        user = self.estate_system.current_user
        name = simpledialog.askstring("Estate Name Change", "Enter New Name")
        user.update_estate(name)
        messagebox.showinfo("Name Change", "Name Change Successful")

    def change_manager(self):
        self.change_manager_button = Button()
        self.change_manager_button.grid(row=2, column=0)
        self.change_manager_button.configure(text="Change Manager")
        self.change_manager_button.bind("<ButtonRelease-1>", self.change_manager_button_clicked)

    def change_manager_button_clicked(self, event):
        name = simpledialog.askstring("Manager Change", "Enter New Name")
        for user in self.estate_system.users:
            if user.username == name and isinstance(user, Manager):
                self.estate.change_manager(user)
                messagebox.showinfo("Manager Change", "Manager Change Successful")
            else:
                messagebox.showinfo("Manager Change", "Manager does not Exist")

    def view_estate(self):
        self.view_estate_button = Button()
        self.view_estate_button.grid(row=3, column=0)
        self.view_estate_button.configure(text="View Estate")
        self.view_estate_button.bind("<ButtonRelease-1>", self.view_estate_button_clicked)

    def view_estate_button_clicked(self, event):
        print(self.estate)

    def add_Thoroughfare(self):
        # add
        self.thoroughfare_label = Label()
        self.thoroughfare_label.grid(row=0, column=1)
        # style
        self.thoroughfare_label.configure(text="Thoroughfares")

    def add_Thoroughfare_button(self):
        self.add_t_button = Button()
        self.add_t_button.grid(row=1, column=1)
        self.add_t_button.configure(text="Add Thoroughfares")
        self.add_t_button.bind("<ButtonRelease-1>", self.add_t_button_clicked)

    def add_t_button_clicked(self, event):
        for thoroughfare in self.estate_system.thoroughfare:
            if thoroughfare in self.estate_system.thoroughfare:
                self.estate.add_thoroughfare()
                messagebox.showinfo("Add Thoroughfares", "Thoroughfares added to Estate")
                break
        else:
            messagebox.showinfo("Add Thoroughfares", "Nothing to be added")

    def remove_Thoroughfare_button(self):
        self.remove_t_button = Button()
        self.remove_t_button.grid(row=2, column=1)
        self.remove_t_button.configure(text="Remove Thoroughfare")
        self.remove_t_button.bind("<ButtonRelease-1>", self.remove_t_button_clicked)

    def remove_t_button_clicked(self, event):
        self.estate.remove_thoroughfare()
        messagebox.showinfo("Remove Thoroughfares", "Thoroughfares removed from Estate")

    def property_label(self):
        self.add_property_label = Label()
        self.add_property_label.grid(row=0, column=2)
        self.add_property_label.configure(text="Property")

    def add_property(self):
        self.add_p_button = Button()
        self.add_p_button.grid(row=1, column=2)
        self.add_p_button.configure(text="Add Properties")
        self.add_p_button.bind("<ButtonRelease-1>", self.add_p_button_clicked)

    def add_p_button_clicked(self, event):
        for property in self.estate_system.property:
            if property in self.estate_system.property:
                self.estate.add_property()
                messagebox.showinfo("Add Properties", "Properties added to Estate")
                break
            else:
                messagebox.showinfo("Add Properties", "Nothing to be added")

    def remove_property(self):
        self.remove_p_button = Button()
        self.remove_p_button.grid(row=2, column=2)
        self.remove_p_button.configure(text="Remove Properties")
        self.remove_p_button.bind("<ButtonRelease-1>", self.remove_p_button_clicked)

    def remove_p_button_clicked(self, event):
        for property in self.estate_system.property:
            if property in self.estate_system.property:
                self.estate.remove_property()
                messagebox.showinfo("Remove Properties", "Properties removed from Estate")
                break
            else:
                messagebox.showinfo("Remove Properties", "Nothing to be removed")

    def view_invoice(self):
        self.invoice_button = Button()
        self.invoice_button.grid(row=1, column=3)
        self.invoice_button.configure(text="View Invoice")
        self.invoice_button.bind("<ButtonRelease-1>", self.view_invoice_button_clicked)

    def view_invoice_button_clicked(self, event):
        messagebox.showinfo("View Invoice", f'The price for {self.estate_system.current_estate} is {Estate.PRICE}')
