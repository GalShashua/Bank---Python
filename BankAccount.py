# Name: Gal Shashua             ID: 315878397

from tkinter import *
import tkinter.messagebox
import time


'''
#################################################################################
#                              Account class                                    #
#################################################################################
'''

class Account:
    def __init__(self, name, account_number, balance, framework):
        self.name = name
        self.account_number = account_number
        self.balance = balance
        if framework is None:
            self.framework = 1500
        else:
            self.set_framework(framework)
        self.expense = 0

    def set_framework(self, framework):
        self.framework = framework

    def deposit(self, amount):
        if amount.isnumeric():
            amount = int(amount)
            self.balance += amount
            return True
        else:
            print("Please enter a Positive number to deposit")
            return False

    def attract(self, amount):
        if amount.isnumeric():
            amount = int(amount)
            if (self.expense+amount) <= self.framework:
                self.expense += amount
                self.balance -= amount
                return True
            else:
                tkinter.messagebox.showerror("Error", "your framework is %d" % self.framework)
                return False
        else:
            print("Please enter a Positive number to attract")

    def __str__(self):
        return "name %s number %d balance %d" % (self.name, self.account_number, self.balance)

    def get_name(self):
        return self.name

    def get_expense(self):
        return self.expense

    def get_balance(self):
        return self.balance

    def get_framework(self):
        return self.framework

    def get_account_number(self):
        return self.account_number


'''
#################################################################################
#                                FUNCTIONS                                      #
#################################################################################
'''


def gen_func_balance(n):
    for item in n:
        yield item


def decorator_date(func):
    date = time.strftime("%x")

    def wrapper(*args, **kwargs):
        print(str(func.__name__) + "Transaction date: " + str(date))
        return func(*args, **kwargs)
    return wrapper


def set_text(text):
    entry_name.delete(0, END)
    entry_name.insert(0, text)
    return


def click_right():
    global i
    if i < len(customers)-1:
        i = i + 1
        initialize_entries(i)


def click_left():
    global i
    if i != 0:
        i = i - 1
        initialize_entries(i)


def initialize_entries(x):
    v0.set(customers[x].get_name())
    v1.set(customers[x].get_account_number())
    v2.set(customers[x].get_balance())
    v3.set(customers[x].get_framework())


global i
i = 0
person1 = Account("Gal", 54387, 2000, None)
person2 = Account("Melany", 87326, 6000, 4600)
person3 = Account("Tom", 94279, 1500, None)
person4 = Account("Ben", 14696, 3500, 2500)
customers = [person1, person2, person3, person4]
gen = gen_func_balance(customers)
for obj in gen:
    print("Account owner: %s, Balance: %d" % (obj.get_name(), obj.get_balance()))


'''
#################################################################################
#                                    GUI                                        #
#################################################################################
'''

@decorator_date
def print_balance():
    tkinter.messagebox.showinfo("Receiving", customers[i].get_balance())

def deposit():
    def check_the_amount():
        amount = entry.get()
        c = customers[i].deposit(str(amount))
        if c:
            get_entry_var1()
        else:
            root1.destroy()

    @decorator_date
    def get_entry_var1():
        root1.destroy()
        v2.set(customers[i].get_balance())

    root1 = Tk()
    root1.title("Deposit money")
    bt = Button(root1, text="Confirm", command=lambda: check_the_amount())
    bt.grid(row=5, sticky=E, padx=10, pady=10)
    l1 = Label(root1, text="How much money you want to deposit? ")
    l1.grid(row=0, padx=10, pady=10)
    v = StringVar()
    entry = Entry(root1, textvariable=v)
    entry.grid(row=0, column=1, sticky=W, padx=10, pady=10)
    root1.mainloop()


def attraction():
    def check_the_amount():
        amount = entry.get()
        c = customers[i].attract(str(amount))
        if c:
            get_entry_var()
        else:
            root2.destroy()

    @decorator_date
    def get_entry_var():
        root2.destroy()
        v2.set(customers[i].get_balance())

    root2 = Tk()
    root2.title("Withdraw")
    bt = Button(root2, text="Confirm", command=lambda: check_the_amount())
    bt.grid(row=5, sticky=E, padx=10, pady=10)
    l1 = Label(root2, text="How much money you want to withdraw?")
    l1.grid(row=0, padx=10, pady=10)
    v = StringVar()
    entry = Entry(root2, textvariable=v)
    entry.grid(row=0, column=1, sticky=W, padx=10, pady=10)
    root2.mainloop()


def transfer():
    def check():
        amount = entry1.get()
        for x in customers:
            if x.get_name() == str(entry2.get()) and x.get_account_number() == int(entry3.get()):
                if customers[i].attract(str(amount)) is True:
                    get_entry_var2(amount, x)
                    return
        print("Error in data")
        root3.destroy()

    @decorator_date
    def get_entry_var2(amount, x):
        x.deposit(str(amount))
        var2.set(customers[i].get_balance())
        var2.set(x.get_balance())

        click_right()
        click_left()
        root3.destroy()

    root3 = Tk()
    root3.title("Bank Transfer")
    bt = Button(root3, text="Confirm", command=lambda: check())
    bt.grid(row=5, sticky=E, padx=10, pady=10)
    l1 = Label(root3, text="How much money you want to transfer?")
    l1.grid(row=0, padx=10, pady=10)
    l2 = Label(root3, text="what name of customer?")
    l2.grid(row=1, padx=10, pady=10)
    l2 = Label(root3, text="what bank number of customer?")
    l2.grid(row=2, padx=10, pady=10)
    var1 = StringVar()
    entry1 = Entry(root3, textvariable=var1)
    entry1.grid(row=0, column=1, sticky=W, padx=10, pady=10)
    var2 = StringVar()
    entry2 = Entry(root3, textvariable=var2)
    entry2.grid(row=1, column=1, sticky=W, padx=10, pady=10)
    var3 = StringVar()
    entry3 = Entry(root3, textvariable=var3)
    entry3.grid(row=2, column=1, sticky=W, padx=10, pady=10)
    root3.mainloop()


root = Tk()
BACKGROUND='midnight blue'
blank_space =" "
root.title(90*blank_space+"BANK")
root.geometry('690x330')

bank_icon = PhotoImage(file='icons/bank.png')
bank_button = Label(root, image=bank_icon, compound=CENTER, bg="white")

root.configure(background=BACKGROUND)
root.resizable(True, True)

v0 = StringVar()
v1 = StringVar()
v2 = StringVar()
v3 = StringVar()
initialize_entries(0)
tool_buttons1 = Frame(root, bg=BACKGROUND)
tool_buttons2 = Frame(root,bg=BACKGROUND)
tool_text = Frame(root,bg=BACKGROUND)
tool_entries = Frame(root,bg=BACKGROUND)
framework_label = Label(tool_text, text="Account framework: ",bg=BACKGROUND,fg='white', font=("Helvetica", "14"))\
    .pack(side=BOTTOM, padx=2, pady=4)
balance_label = Label(tool_text, text="Current balance: ", bg=BACKGROUND,fg='white',font=("Helvetica", "14"))\
    .pack(side=BOTTOM, padx=2, pady=4)
account_num_label = Label(tool_text, text="Bank account number: ",bg=BACKGROUND,fg='white', font=("Helvetica", "14"))\
    .pack(side=BOTTOM, padx=2, pady=4)
name_label = Label(tool_text, text="Bank account owner: ", bg=BACKGROUND,fg='white', font=("Helvetica", "16", "bold"))\
    .pack(side=BOTTOM, padx=2, pady=4)

deposit_icon = PhotoImage(file='icons/deposit.png')
withdraw_icon = PhotoImage(file='icons/withdraw.png')
loan_icon = PhotoImage(file='icons/loan.png')
balance_icon = PhotoImage(file='icons/cbalance.png')
right_icon = PhotoImage(file='icons/right.png')
left_icon = PhotoImage(file='icons/left.png')

deposit_button = Button(tool_buttons1, image=deposit_icon, text="DEPOSIT\n", compound=BOTTOM,bg='white', height=110, width=110, command=deposit)
deposit_button.pack(side=RIGHT, padx=20, pady=2)
attract_button = Button(tool_buttons2, text="WITHDRAW\n", compound=BOTTOM, bg='white',image=withdraw_icon, height=110, width=110, command=attraction)\
    .pack(side=LEFT, padx=0, pady=2)
balance_button = Button(tool_buttons2, text="GET BALANCE\n", compound=BOTTOM, bg='white',image=balance_icon, height=110, width=110,command=print_balance)\
    .pack(side=LEFT, padx=15, pady=2)
transfer_button = Button(tool_buttons1, text="BANK TRANSFER\n", compound=BOTTOM, bg='white',image=loan_icon, height=110, width=110, command=transfer)\
    .pack(side=RIGHT, padx=0, pady=2)

right_button = Button(root, image=right_icon, fg="white", command=lambda: click_right())
left_button = Button(root, image=left_icon, fg="white", command=lambda: click_left())

entry_framework = Entry(tool_entries, textvariable=v3, font=("Helvetica", "12"), justify='center')\
    .pack(side=BOTTOM, padx=2, pady=6)
entry_balance = Entry(tool_entries, textvariable=v2, font=("Helvetica", "12"), justify='center')\
    .pack(side=BOTTOM, padx=2, pady=6)
entry_num = Entry(tool_entries, textvariable=v1, font=("Helvetica", "12"), justify='center')\
    .pack(side=BOTTOM, padx=2, pady=6)
entry_name = Entry(tool_entries, textvariable=v0, font=("Helvetica", "12"), justify='center')\
    .pack(side=BOTTOM, padx=2, pady=6)

right_button.grid(row=0, column=3, padx=10, pady=10, sticky=W)
left_button.grid(row=0, column=0, padx=10, pady=10, sticky=W)
tool_buttons1.grid(row=2, column=1, sticky=E, pady=10)
tool_buttons2.grid(row=2, column=2, sticky=W, pady=10)
tool_text.grid(row=0, column=1, sticky=NE, padx=10, pady=10)
tool_entries.grid(row=0, column=2, sticky=W)
root.mainloop()
