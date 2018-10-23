# coding = UTF-8
from tkinter import *
import tkinter.messagebox
window = Tk()
window.title("MESSAGEBOX")
window.geometry("400x350")


def hit_me():
    # tkinter.messagebox.showinfo("提示", message="You hit me!")
    # tkinter.messagebox.showwarning("警告", message="You hit me!")
    tkinter.messagebox.ask
    tkinter.messagebox.showerror("提示", message="You hit me!")



Button(window, text="Hit me!", command=hit_me).pack()
window.mainloop()