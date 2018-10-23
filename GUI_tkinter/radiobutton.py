# coding = UTF-8
from tkinter import *

windows = Tk()
windows.title("RADIOBUTTON")
windows.geometry("600x450")
var = StringVar()
# params:height bg font
l1 = Label(windows, bg="yellow", width=40)
l1.pack()


def print_selection():
    l1.config(text="You have selected option " + var.get())


r1 = Radiobutton(windows, text="Option A", variable=var, value="A",  indicatoron=0, command=print_selection)
r1.deselect()
r1.pack()
r2 = Radiobutton(windows, text="Option B", variable=var, value="B", command=print_selection)
r2.flash()
r2.pack()
r3 = Radiobutton(windows, text="Option C", variable=var, value="C", command=print_selection)
r3.deselect()
r3.pack()
r4 = Radiobutton(windows, text="Option D", variable=var, value="D", command=print_selection)
r4.deselect()
r4.pack()
windows.mainloop()