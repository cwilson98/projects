from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from Manager_Gui import Manager_Gui
from admin import admin
from Estate import Estate

class admin_gui(Manager_Gui, Tk):

    def __init__(self, Estate_System):
        super().__init__(admin)
        self.estate_system = Estate_System

        self.create_label()
        self.create_entry()
        self.create_estate()
        self.view_estate()
        self.update_estate()
        self.remove_estate()


        self.title("Admin Menu")
        self.configure(bg="#eee",
                       height=500,
                       width=500)


    def create_label(self):
        self.create_estate_label = Label()
        self.create_estate_label.configure(text="Estate")
        self.create_estate_label.grid(row=10, column=1, columnspan=4)

    def create_entry(self):
        self.create_textbox = Entry()
        self.create_textbox.grid(row=11, column=1, columnspan=4)

    def create_estate(self):
        self.create_estate_button = Button()
        self.create_estate_button.configure(text="Create Estate")
        self.create_estate_button.grid(row=12, column=1)
        self.create_estate_button.bind("<ButtonRelease-1>", self.create_button_clicked)

    def create_button_clicked(self, event):
        user = self.estate_system.current_user
        name = simpledialog.askstring("Estate Creation","Name of Estate")
        user.create_estate(name)
        messagebox.showinfo("Create Estate", "Estate Created")

    def view_estate(self):
        self.view_estate_button = Button()
        self.view_estate_button.configure(text="View Estate")
        self.view_estate_button.grid(row=12, column=2)
        self.view_estate_button.bind("<ButtonRelease-1>", self.view_button_clicked)

    def view_button_clicked(self, event):
        user = self.estate_system.current_user
        user.view_estate()


    def update_estate(self):
        self.update_estate_button = Button()
        self.update_estate_button.configure(text="Update Estate")
        self.update_estate_button.grid(row=12, column=3)
        self.update_estate_button.bind("<ButtonRelease-1>", self.update_button_clicked)

    def update_button_clicked(self, event):
        user = self.estate_system.current_user
        name = simpledialog.askstring("Estate Update","Name of Estate")
        messagebox.showinfo("Update Estate", "Opening Estate Menu")
        self.destroy()
        user.update_estate(name)

    def remove_estate(self):
        self.remove_estate_button = Button()
        self.remove_estate_button.configure(text="Remove Estate")
        self.remove_estate_button.grid(row=12, column=4)
        self.remove_estate_button.bind("<ButtonRelease-1>", self.remove_button_clicked)

    def remove_button_clicked(self, event):
        user = self.estate_system.current_user
        name = simpledialog.askstring("Estate Removal","Name of Estate")
        user.remove_estate(name)
        messagebox.showinfo("Remove Estate", "Estate Deleted")



