# coding = UTF-8
from tkinter import *

windows = Tk()
windows.title("SCALE")
windows.geometry("400x350")
# params:height bg font
l1 = Label(windows, bg="yellow", width=40, height=2, font=("楷体", 25))
l1.pack()
var1 = IntVar()


def print_selection():
    if var1.get() == 1 and var2.get() == 0:
        l1.config(text="You have selected Python")
    elif var1.get() == 0 and var2.get() == 1:
        l1.config(text="You have selected C++")
    else:
        l1.config(text="You have selected both")

c1 = Checkbutton(
    windows,
    text="Python",
    variable=var1,
    onvalue=1, offvalue=0,
    command=print_selection
)
c1.pack()
var2 = IntVar()
c2 = Checkbutton(
    windows,
    text="C++",
    variable=var2,
    onvalue=1, offvalue=0,
    command=print_selection
)
c2.pack()
windows.mainloop()