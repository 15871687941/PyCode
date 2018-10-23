# coding = UTF-8
from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("登录")
window.geometry("400x350+500+150")
window['bg'] = "black"

Label(window, text="Username:", width=10, font=("楷体", 15)).place(x=60, y=100)
e1 = Entry(window, width=16, font=("楷体", 15))
e1.place(x=180, y=100)
Label(window, text="Password:", width=10, font=("楷体", 15)).place(x=60, y=140)
e2 = Entry(window, show="*", width=16, font=("楷体", 15))
e2.place(x=180, y=140)


def sign_up():
    var_username = e1.get()
    var_password = e2.get()
    if var_username == "root" and var_password == "123456":
        messagebox.showinfo(title="提示", message="恭喜你，登录成功！")
    else:
        messagebox.showerror(title="警告", message="登录失败！")


def login():
    window_sign_up = Toplevel(window)
    window_sign_up.title("登录")
    window_sign_up.geometry("400x350+600+150")
    window_sign_up['bg'] = "black"


Button(window, text="SIGN UP", width=10, font=("楷体", 15), command=login).place(x=160, y=250)
window.mainloop()