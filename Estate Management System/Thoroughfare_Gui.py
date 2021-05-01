from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from Thoroughfare import Thoroughfare
from Estate_System import Estate_System
from System_Gui import System_Gui

class Thoroughfare_Gui(Tk):
    def __init__(self):
        super().__init__()

        self.title(Thoroughfare)
        self.configure(bg="#eee",
                       height=500,
                       width=500)

        self.change_name()
        self.change_entry()
        self.change_button()
        self.return_user()

    def change_name(self):
        self.change_name_label = Label()
        self.change_name_label.configure(text="New Thoroughfare Name")
        self.change_name_label.grid(row=0, column=0, columnspan=2)

    def change_button(self):
        self.change_name_button = Button()
        self.change_name_button.configure(text="Confirm Change")
        self.change_name_button.bind("<ButtonRelease-1>", self.change_clicked)
        self.change_name_button.grid(row=1, column=0)

    def change_clicked(self, event):
        user = self.estate_system.current_user
        name = simpledialog.askstring("Thoroughfare Name Change", "Enter New NAme")
        user.update_thoroughfare(name)
        messagebox.showinfo("Name Change Successful")

    def return_user(self):
        self.back_button = Button()
        self.back_button.configure(text="Return to main menu")
        self.back_button.grid(row=1, column=1)
        self.back_button.bind("<ButtonRelease-1>", self.return_clicked)

    def return_clicked(self, event):
        self.withdraw()
        system = Estate_System()
        gui = System_Gui(system)
        gui.mainloop()


