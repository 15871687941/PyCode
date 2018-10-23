from tkinter import *
import requests

# 在线翻译网站 post:f t w
start_url = "http://fy.iciba.com/ajax.php?a=fy"
# 创建窗口
root = Tk()
# 窗口标题
root.title("中英互译")
# 窗口大小
root.geometry("370x100+500+300")
# 标签控件
label1 = Label(root, text="输入要翻译的文字：")
label1.grid(row=0, column=0)
label2 = Label(root, text="翻译之后的结果：")
label2.grid(row=1, column=0)
# 输入控件
entry1 = Entry(root, font=("微软雅黑", 15))
entry1.grid(row=0, column=1)
entry2 = Entry(root, font=("微软雅黑", 15))
entry2.grid(row=1, column=1)


# 按钮
def translate():
    entry2.delete(0, 'end')
    input_data = entry1.get()
    if not input_data.isalpha():
        input_data = input_data.lower()
        data = {
            "f": "auto",
            "t": "auto",
            "w": input_data
        }
        response = requests.post(start_url, data=data)
        result = response.json()
        output = result['content']['out']
    else:
        data = {
            "f": "auto",
            "t": "auto",
            "w": input_data
        }
        response = requests.post(start_url, data=data)
        result = response.json()
        output = result['content']['word_mean'][0]
    entry2.insert("insert", output)


button1 = Button(root, text="翻译", width=10, command=translate)
# sticky（对齐方式）：N S W E
button1.grid(row=2, column=0, sticky=W)
button1 = Button(root, text="退出", width=10, command=root.quit)
button1.grid(row=2, column=1, sticky=E)
# 显示窗口 消息循环
root.mainloop()
