from tkinter import *
from tkinter import messagebox

class Gui(Tk):
    def __init__(self):
        super().__init__()

        # set window attributes
        self.title("The Life Project")
        self.configure(bg="#f00",
                       height=500,
                       width=500)
        self.__add_heading_label()
        self.__add_instruction_label()
        self.__add_tickets_entry()
        self.__add_submit_button()

    def __add_heading_label(self):
        # create the component
        self.heading_label = Label()
        self.heading_label.grid(row=0, column=0)

        #style the component
        self.heading_label.configure(font="Arial 24",
                                     text="Universe Creator")

        #assign event handlers to the component

    def __add_instruction_label(self):
        self.instruction_label = Label()
        self.instruction_label.grid(row=1, column=0)
        self.instruction_label.configure(font="Arial 18",
                                         text="How many tickets are needed?")

    def __add_tickets_entry(self):
        self.tickets_entry = Entry()
        self.tickets_entry.grid(row=2, column=0)

    def __add_submit_button(self):
        self.submit_button = Button()
        self.submit_button.grid(row=3, column=0)
        self.submit_button.configure(text="SUBMIT")
        self.submit_button.bind("<ButtonRelease-1>", self.__submit_button_clicked)

    def __submit_button_clicked(self, event):
        messagebox.showinfo("Submit", "Tickets Purchased")

if __name__ == '__main__':
    gui = Gui()
    gui.mainloop()

