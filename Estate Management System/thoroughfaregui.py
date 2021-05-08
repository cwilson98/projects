from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog

class ThoroughfareGui(Tk):
    def __init__(self, estate_system, thoroughfare):
        super().__init__()
        self.estate_system = estate_system
        self.thoroughfare = thoroughfare

        self.change_name()
        self.change_button()
        self.view_thoroughfare()
        self.property_label()
        self.add_property()
        self.remove_property()

        self.title(self.estate_system.current_thoroughfare)
        self.configure(bg="#eee",
                       height=500,
                       width=500)

    def change_name(self):
        self.change_name_label = Label()
        self.change_name_label.configure(text="Thoroughfare")
        self.change_name_label.grid(row=0, column=0)

    def change_button(self):
        self.change_name_button = Button()
        self.change_name_button.configure(text="Name Change")
        self.change_name_button.bind("<ButtonRelease-1>", self.change_clicked)
        self.change_name_button.grid(row=1, column=0)

    def change_clicked(self, event):
        name = simpledialog.askstring("Name Change", "Name of Thoroughfare")
        self.thoroughfare.change_name(name)
        messagebox.showinfo("Change Name", "Name Successfully Changed")

    def view_thoroughfare(self):
        self.view_thoroughfare_button = Button()
        self.view_thoroughfare_button.grid(row=2, column=0)
        self.view_thoroughfare_button.configure(text="View Thoroughfare")
        self.view_thoroughfare_button.bind("<ButtonRelease-1>", self.view_thoroughfare_button_clicked)

    def view_thoroughfare_button_clicked(self, event):
        print(self.thoroughfare)

    def property_label(self):
        self.add_property_label = Label()
        self.add_property_label.grid(row=0, column=1)
        self.add_property_label.configure(text="Property")

    def add_property(self):
        self.add_p_button = Button()
        self.add_p_button.grid(row=1, column=1)
        self.add_p_button.configure(text="Add Properties")
        self.add_p_button.bind("<ButtonRelease-1>", self.add_p_button_clicked)

    def add_p_button_clicked(self, event):
        for property in self.estate_system.property:
            if property in self.estate_system.property:
                self.thoroughfare.add_property()
                messagebox.showinfo("Add Properties", "Properties added to Thoroughfare")
                break
            else:
                messagebox.showinfo("Add Properties", "Nothing to be added")

    def remove_property(self):
        self.remove_p_button = Button()
        self.remove_p_button.grid(row=2, column=1)
        self.remove_p_button.configure(text="Remove Properties")
        self.remove_p_button.bind("<ButtonRelease-1>", self.remove_p_button_clicked)

    def remove_p_button_clicked(self, event):
        for property in self.estate_system.property:
            if property in self.estate_system.property:
                self.thoroughfare.remove_property()
                messagebox.showinfo("Remove Properties", "Properties removed from Thoroughfare")
                break
            else:
                messagebox.showinfo("Remove Properties", "Nothing to be removed")




