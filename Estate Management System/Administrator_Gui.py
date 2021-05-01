from tkinter import *
from tkinter import messagebox

class Administrator_Gui(Tk):
    def __init__(self, Estate_System):
        super().__init__()
        self.estate_system = Estate_System



        self.title("Admin Menu")
        self.configure(bg="#eee",
                       height=500,
                       width=500)

        self.create_estate()
        self.create_entry()

    def create_estate(self):
        self.create_estate_button = Button()
        self.create_estate_button.configure(text="Create Estate")
        self.create_estate_button.pack()
        self.create_estate_button.bind("<ButtonRelease-1", self.button_clicked)

    def create_entry(self):
        self.create_textbox = Entry()
        self.create_textbox.pack()

    def button_clicked(self, event):
        user = self.estate_system.current_user
        name = self.create_textbox
        self.estate_system.estates.append(user.create_estate(name))
        messagebox.showinfo("Create Estate", "Estate has been created")