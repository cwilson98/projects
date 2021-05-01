from tkinter import *
from tkinter import messagebox
from Administrator import Administrator
from Manager_Gui import Manager_Gui
from Estate_Gui import Estate_Gui

class Administrator_Gui(Manager_Gui, Tk):

    def __init__(self, estate_system):
        super().__init__()
        self.administrator = Administrator(input("Please enter a username: "))

        #list of components
        self.estate_label = Label()
        self.estate_list = Listbox()
        self.create_button = Button()
        self.view_button = Button()
        self.remove_button = Button()

        #set window attributes
        self.title("Estate Management System - Admin Access")

        #add components
        self.create_estate_label()
        self.create_estate_list()
        self.create_estate_button()
        self.view_estate_button()
        self.remove_estate_button()

    def create_estate_label(self):
        # add
        self.estate_label.grid(row=0, column=8, columnspan=2)
        # style
        self.estate_label.configure(text="Estates")

    def create_estate_list(self):
        self.estate_list.grid(row=1, column=8, columnspan=2)

    def create_estate_button(self):
        self.create_button.grid(row=2, column=8)
        self.create_button.configure(text="Create Estate")
        self.create_button.bind("<ButtonRelease-1>", self.add_button_clicked)

    def add_button_clicked(self, event):
        messagebox.showinfo("Create Estate", "Estate has been created")
        self.administrator.create_estate()

    def view_estate_button(self):
        self.view_button.grid(row=2, column=9)
        self.view_button.configure(text="View Estate")
        self.view_button.bind("<ButtonRelease-1>", self.view_button_clicked)

    def view_button_clicked(self, event):
        self.administrator.display_estate()
        messagebox.showinfo("View Estate", "Bringing you to the Estate")
        self.destroy()
        self.estate_gui = Estate_Gui()
        self.estate_gui.mainloop()

    def remove_estate_button(self):
        self.remove_button.grid(row=2, column=10)
        self.remove_button.configure(text="Remove Estate")
        self.remove_button.bind("<ButtonRelease-1>", self.remove_button_clicked)

    def remove_button_clicked(self, event):
        messagebox.showinfo("Remove Estate", "Estate has been deleted")

#make a go back button from all areas
#messagebox for all

