# coding = UTF-8
from tkinter import *

Windows = Tk()
Windows.title("MY WINDOWS")
Windows.geometry("200x200")
e1 = Entry(Windows, show="*", width=16, font=("楷体", 10))
e1.pack()

def insert_point():
    var = e1.get()
    t1.insert("insert", var)

b1 = Button(Windows, text="Insert Point", width=16, command=insert_point)
b1.pack()


def insert_end():
    var = e1.get()
    t1.insert("end", var + "\n")


b2 = Button(Windows, text="Insert End", width=16, command=insert_end)
b2.pack()

t1 = Text(Windows)
t1.pack()

Windows.mainloop()
