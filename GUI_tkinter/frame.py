# coding = UTF-8
from tkinter import *

window = Tk()
window.title("FRAME")
window.geometry("400x300")
Label(window, text="on the window").pack()
frm = Frame(window, width=400)
frm_1 = Frame(frm, width=200)
frm_1.pack(side="left")
frm_r = Frame(frm, width=200)
frm_r.pack(side="right")
Label(frm_1, text="on the frm_l1").pack()
Label(frm_1, text="on the frm_l2").pack()
Label(frm_r, text="on the frm_r").pack()
frm.pack()


window.mainloop()