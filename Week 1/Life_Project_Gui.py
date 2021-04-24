from tkinter import *

class Gui(Tk):

    def __init__(self):
        super().__init__()

        # set window attributes
        self.title("The Life Project")
        self.configure(bg="#f00")

        # add components
        self.__add_heading_label()
        self.__add_instruction_label()
        self.__add_universe_name()

    def __add_heading_label(self):
        # create
        self.heading_label = Label()
        # layout
        self.heading_label.grid(row=0, column=0)
        # style
        self.heading_label.configure(font="Arial 24",
                                     text="The Life Project")
    def __add_instruction_label(self):
        self.instruction_label = Label()
        self.instruction_label.grid(row=1, column=0)
        self.instruction_label.configure(font="Arial 18",
                                         text="What is the name of the Universe?")

    def __add_universe_name(self):
        self.universe_name = Entry()
        self.universe_name.grid(row=2, column=0)

if __name__ == '__main__':
    gui = Gui()
    gui.mainloop()