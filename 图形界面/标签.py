# coding=utf-8
from tkinter import *
root = Tk()
root.geometry("480x320+400+200")
root.title("标签")
label1 = Label(root, text="URL:")
entry1 = Entry(root, width=200)
label1.pack(side=LEFT, pady=10)
entry1.pack(side=LEFT, pady=10)
mainloop()
