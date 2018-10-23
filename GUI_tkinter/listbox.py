# coding = UTF-8
from tkinter import *

Windows = Tk()
Windows.title("MY WINDOWS")
Windows.geometry("400x350")

lvar1 = StringVar()
l1 = Label(Windows, textvariable=lvar1, width=5, bg="yellow", font=("楷体", 20))
l1.pack()


def print_selection():
    var = list1.get(list1.curselection())
    list1.insert("end", 1)
    lvar1.set(var)


b1 = Button(Windows, text="Print Selection", command=print_selection)
b1.pack()
listvar1 = StringVar()
listvar1.set((11, 3, 6, 5, 6))
list1 = Listbox(Windows, listvariable=listvar1)
list1.pack()

Windows.mainloop()