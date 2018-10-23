# coding = UTF-8
from tkinter import *

windows = Tk()
windows.title("SCALE")
windows.geometry("200x200")

canvas = Canvas(windows, bg="blue", height=160, width=200)
image_file = PhotoImage(file=r"H:\桌面文件\2.gif")
image = canvas.create_image(0, 0, anchor="nw", image=image_file)
line = canvas.create_line(50, 50, 80, 80)
oval = canvas.create_oval(50, 50, 80, 80, fill="red")
arc = canvas.create_arc(100, 100, 130, 130, start=0, extent=180, fill="blue")
rect = canvas.create_rectangle(0, 0, 100, 100)
canvas.pack()


def move_it():
    canvas.move(oval, 0, 2)


b = Button(windows, text="move", command=move_it)
b.pack()
windows.mainloop()
