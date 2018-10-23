# coding = UTF-8
from tkinter import *

windows = Tk()
windows.title("SCALE")
windows.geometry("400x350")
# params:height bg font
l1 = Label(windows, bg="yellow", width=40, height=2, font=("楷体", 25))
l1.pack()
v = StringVar()

# 参数为默认的，为scale的值
def print_selection(v):
    l1.config(text="You have selected " + v)


s1 = Scale(windows, label="try me", from_=0, to=100, tickinterval=20, resolution=0.01, length=400, orient=HORIZONTAL,
           command=print_selection)
s1.pack()
windows.mainloop()