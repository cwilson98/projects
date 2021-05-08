from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from managergui import Manager_Gui
from estate import Estate

class admin_gui(Manager_Gui, Tk):

    def __init__(self, estate_system):
        super().__init__(estate_system)
        self.estate_system = estate_system

        self.create_label()
        self.create_estate()
        self.view_estate()
        self.update_estate()
        self.manager_label()
        self.remove_estate()
        self.create_manager()
        self.view_managers()
        self.remove_manager()
        self.add_invoice()
        self.view_invoice()
        self.update_invoice()
        self.delete_invoice()


        self.title("Admin Menu")
        self.configure(bg="#eee",
                       height=500,
                       width=500)


    def create_label(self):
        self.create_estate_label = Label()
        self.create_estate_label.configure(text="Estate")
        self.create_estate_label.grid(row=0, column=0)

    def create_estate(self):
        self.create_estate_button = Button()
        self.create_estate_button.configure(text="Create Estate")
        self.create_estate_button.grid(row=1, column=0)
        self.create_estate_button.bind("<ButtonRelease-1>", self.create_button_clicked)

    def create_button_clicked(self, event):
        user = self.estate_system.current_user
        name = simpledialog.askstring("Estate Creation","Name of Estate")
        user.create_estate(name)
        messagebox.showinfo("Create Estate", "Estate Created")

    def view_estate(self):
        self.view_estate_button = Button()
        self.view_estate_button.configure(text="View Estate")
        self.view_estate_button.grid(row=2, column=0)
        self.view_estate_button.bind("<ButtonRelease-1>", self.view_button_clicked)

    def view_button_clicked(self, event):
        user = self.estate_system.current_user
        user.view_estate()


    def update_estate(self):
        self.update_estate_button = Button()
        self.update_estate_button.configure(text="Update Estate")
        self.update_estate_button.grid(row=3, column=0)
        self.update_estate_button.bind("<ButtonRelease-1>", self.update_button_clicked)

    def update_button_clicked(self, event):
        user = self.estate_system.current_user
        name = simpledialog.askstring("Estate Update","Name of Estate")
        for Estate in self.estate_system.estates:
            if Estate.name == name:
                messagebox.showinfo("Update Estate", "Opening Estate Menu")
                self.destroy()
                self.estate_system.current_estate = name
                user.update_estate(name)
                break
            else:
                messagebox.showinfo("Update Estate", "Estate does not Exist")

    def remove_estate(self):
        self.remove_estate_button = Button()
        self.remove_estate_button.configure(text="Remove Estate")
        self.remove_estate_button.grid(row=4, column=0)
        self.remove_estate_button.bind("<ButtonRelease-1>", self.remove_button_clicked)

    def remove_button_clicked(self, event):
        user = self.estate_system.current_user
        name = simpledialog.askstring("Estate Removal","Name of Estate")
        for Estate in self.estate_system.estates:
            if Estate.name == name:
                user.remove_estate(name)
                messagebox.showinfo("Remove Estate", "Estate Deleted")
            else:
                messagebox.showinfo("Remove Estate", "Estate does not Exist")

    def manager_label(self):
        self.create_manager_label = Label()
        self.create_manager_label.configure(text="Manager")
        self.create_manager_label.grid(row=12, column=1)

    def create_manager(self):
        self.create_manager_button = Button()
        self.create_manager_button.configure(text="Create Manager")
        self.create_manager_button.grid(row=13, column=1)
        self.create_manager_button.bind("<ButtonRelease-1>", self.create_m_button_clicked)

    def create_m_button_clicked(self, event):
        user = self.estate_system.current_user
        name = simpledialog.askstring("Manager Creation", "Name of Manager")
        user.create_manager(name)
        messagebox.showinfo("Create Manager", "Estate Manager Created")

    def view_managers(self):
        self.view_manager_button = Button()
        self.view_manager_button.configure(text="View Managers")
        self.view_manager_button.grid(row=14, column=1)
        self.view_manager_button.bind("<ButtonRelease-1>", self.view_m_button_clicked)

    def view_m_button_clicked(self, event):
        user = self.estate_system.current_user
        user.view_managers()

    def remove_manager(self):
        self.remove_manager_button = Button()
        self.remove_manager_button.configure(text="Remove Manager")
        self.remove_manager_button.grid(row=15, column=1)
        self.remove_manager_button.bind("<ButtonRelease-1>", self.remove_m_button_clicked)

    def remove_m_button_clicked(self, event):
        user = self.estate_system.current_user
        name = simpledialog.askstring("Manager Removal", "Name of Manager")
        user.remove_manager(name)
        messagebox.showinfo("Remove Manager", "Estate Manager Removed")


    def add_invoice(self):
        self.invoice_label = Label()
        self.invoice_label.grid(row=0, column=4)
        self.invoice_label.configure(text="Invoice")

    def view_invoice(self):
        self.invoice_button = Button()
        self.invoice_button.grid(row=1, column=4)
        self.invoice_button.configure(text="View Invoice")
        self.invoice_button.bind("<ButtonRelease-1>", self.view_invoice_button_clicked)

    def view_invoice_button_clicked(self, event):
        if len(self.estate_system.estates) >= 1:
            messagebox.showinfo("View Invoice", f"The price for all estates is ${(1000000) * len(self.estate_system.estates)}")
        else:
            messagebox.showinfo("View Invoice", "Not Available at this time")

    def update_invoice(self):
        self.update_invoice_button = Button()
        self.update_invoice_button.grid(row=2, column=4)
        self.update_invoice_button.configure(text="Update Invoice")
        self.update_invoice_button.bind("<ButtonRelease-1>", self.update_invoice_button_clicked)

    def update_invoice_button_clicked(self, event):
        if len(self.estate_system.estates) >= 1 and len(self.estate_system.household) >= 1:
            messagebox.showinfo("Update Invoice",  f'Payments have been made by {len(self.estate_system.household)} households. The new price of all estates is {Estate.PRICE - (1250 * len(self.estate_system.household))}')
        else:
            messagebox.showinfo("Update Invoice", "Not Available at this time")

    def delete_invoice(self):
        self.delete_invoice_button = Button()
        self.delete_invoice_button.grid(row=3, column=4)
        self.delete_invoice_button.configure(text="Delete Invoice")
        self.delete_invoice_button.bind("<ButtonRelease-1>", self.delete_invoice_button_clicked)

    def delete_invoice_button_clicked(self, event):
        if len(self.estate_system.estates) >= 1:
            messagebox.showinfo("Delete Invoice", "This is only possible if all estates have been purchased")
        else:
            messagebox.showinfo("Delete Invoice", "All estates have been purchased")

