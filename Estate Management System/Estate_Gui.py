from tkinter import *
from tkinter import messagebox
from Thoroughfare import Thoroughfare
from Estate import Estate


class Estate_Gui(Estate, Tk):
    def __init__(self):
        super(Estate, self).__init__()


        self.thoroughfare_label = Label()

        self.thoroughfare_list = Listbox()

        self.add_t_button = Button()


        self.add_Thoroughfare()
        self.add_Thoroughfare_button()


        self.title("Estate Menu")

    def add_Thoroughfare(self):
        # add
        self.thoroughfare_label.grid(row=0, column=0, columnspan=2)
        # style
        self.thoroughfare_label.configure(text="Thoroughfares")

    def add_Thoroughfare_button(self):
        self.add_t_button.grid(row=2, column=0)
        self.add_t_button.configure(text="Add Thoroughfare")
        self.add_t_button.bind("<ButtonRelease-1>", self.add_t_button_clicked)

    def add_t_button_clicked(self, event):
        self.add_thoroughfare(Thoroughfare)
        messagebox.showinfo("Add Thoroughfare", "Thoroughfare added to Estate")





if __name__ == '__main__':
    gui = Estate_Gui()
    gui.mainloop()