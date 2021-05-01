from tkinter import *
from admin import admin
from admin_gui import admin_gui
from Manager import Manager
from Manager_Gui import Manager_Gui
from User import User
from User_Gui import User_Gui

class System_Gui(Tk):

    def __init__(self, Estate_System):
        super().__init__()
        self.estate_system = Estate_System

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
                if isinstance(user, admin):
                    self.destroy()
                    self.estate_system.current_user = user
                    admingui = admin_gui(self.estate_system)
                    admingui.mainloop()
                elif isinstance(user, Manager):
                    self.destroy()
                    self.estate_system.current_user = user
                    managergui = Manager_Gui(self.estate_system)
                    managergui.mainloop()
                elif isinstance(user, user):
                    self.destroy()
                    self.estate_system.current_user = user
                    usergui = User_Gui(self.estate_system)
                    usergui.mainloop()




