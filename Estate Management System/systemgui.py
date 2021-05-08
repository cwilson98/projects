from tkinter import *
from admin import Admin
from admin_gui import admin_gui
from manager import Manager
from managergui import Manager_Gui
from user import User
from usergui import User_Gui

class System_Gui(Tk):

    def __init__(self, estate_system):
        super().__init__()
        self.estate_system = estate_system

        self.title("Login")
        self.configure(bg="#eee",
                       height=500,
                       width=500)

        self.add_username_label()
        self.add_username_entry()
        self.add_submit_button()

    def add_username_label(self):
        self.username_label = Label()
        self.username_label.configure(text="Enter Username")
        self.username_label.pack()

    def add_username_entry(self):
        self.username_entry = Entry()
        self.username_entry.pack()

    def add_submit_button(self):
        self.submit_button = Button()
        self.submit_button.configure(text="Submit")
        self.submit_button.pack()
        self.submit_button.bind("<ButtonRelease-1>", self.submit_button_clicked)

    def submit_button_clicked(self, event):
        un = self.username_entry.get()
        for user in self.estate_system.users:
            if user.username == un:
                if isinstance(user, Admin):
                    self.destroy()
                    self.estate_system.current_user = user
                    admingui = admin_gui(self.estate_system)
                    admingui.mainloop()
                elif isinstance(user, Manager):
                    self.destroy()
                    self.estate_system.current_user = user
                    managergui = Manager_Gui(self.estate_system)
                    managergui.mainloop()
                elif isinstance(user, User):
                    self.destroy()
                    self.estate_system.current_user = user
                    usergui = User_Gui(self.estate_system)
                    usergui.mainloop()




