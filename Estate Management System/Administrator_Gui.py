from tkinter import *
from tkinter import messagebox
from Administrator import Administrator
from Manager_Gui import Manager_Gui

class Administrator_Gui(Manager_Gui, Tk):

    def __init__(self):
        super().__init__()
        self.administrator = Administrator(input("Enter a name: "))

        #list of components
        self.estate_label = Label()
        self.estate_list = Listbox()
        self.add_button = Button()
        self.remove_button = Button()

        #set window attributes
        self.title("Estate Management System")

        #add components
        self.add_estate_label()
        self.add_estate_list()
        self.add_estate_button()
        self.remove_estate_button()

    def add_estate_label(self):
        # add
        self.estate_label.grid(row=0, column=8, columnspan=2)
        # style
        self.estate_label.configure(text="Estates")

    def add_estate_list(self):
        self.estate_list.grid(row=1, column=8, columnspan=2)

    def add_estate_button(self):
        self.add_button.grid(row=2, column=8)
        self.add_button.configure(text="Add Estate")
        self.add_button.bind("<ButtonRelease-1>", self.add_button_clicked)

    def add_button_clicked(self, event):
        messagebox.showinfo("Add Estate", "Estate has been created")
        self.destroy()
        self.add_estate_gui = Manager_Gui()
        self.add_estate_gui.mainloop()

    def remove_estate_button(self):
        self.remove_button.grid(row=2, column=9)
        self.remove_button.configure(text="Remove Estate")

#make a go back button from all areas
#messagebox for all
if __name__ == '__main__':
    gui = Administrator_Gui()
    gui.mainloop()
