from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)


def button_clicked():
    my_label4.config(text=int(int(inp.get())*1.60934))

# Label


my_label = Label(text="", font=("Arial", 14))
my_label.grid(column=0, row=0)
my_label.config(padx=20)

inp = Entry()
inp.grid(column=1, row=0)
inp.config(width=15)

my_label2 = Label(text="Miles", font=("Arial", 14))
my_label2.grid(column=2, row=0)
my_label2.config(padx=20)

my_label3 = Label(text="is equal to", font=("Arial", 14))
my_label3.grid(column=0, row=1)
my_label3.config(padx=20)

my_label4 = Label(text="", font=("Arial", 14))
my_label4.grid(column=1, row=1)
my_label4.config(padx=20)

my_label5 = Label(text="Km", font=("Arial", 14))
my_label5.grid(column=2, row=1)
my_label5.config(padx=20)

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)
#
# button = Button(text="New Button", command=button_clicked)
# button.grid(column=2, row=0)


window.mainloop()

