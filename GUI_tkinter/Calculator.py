from tkinter import *


class Calculator(object):
    def __init__(self):
        self.font = ("黑体", )
        self.width = 300
        self.height = 300
        self.result = ""
        self.result_windows = ""
        self.windows()


    def windows(self):
        root = Tk()
        root.title("Calculator")
        root.geometry("+500+250")
        frame_output = Frame(root, bg="green", width=320, height=20)
        frame_output.grid(row=0, column=0)
        frame_output.grid_propagate(0)
        frame_input = Frame(root, bg="red", width=320, height=168)
        frame_input.grid(row=1, column=0)
        frame_input.grid_propagate(0)
        self.out_windows = Entry(frame_output, width=320)
        self.out_windows.grid(sticky=N)
        row = 0
        for key in ["123", "456", "789", "-0.", "+-x", "/="]:
            column = 0
            for char in key:
                btn = Button(frame_input, text=char, width=13, font=self.font, command=lambda: self.submit(char))
                btn.grid(row=row, column=column)
                # btn.bind("<ButtonRelease-{}>".format(char), lambda:)
                column = column + 1
            row = row + 1
        row = 5
        column = 2
        btn = Button(frame_input, text="ctrl", width=13, font=self.font)
        btn.grid(row=row, column=column, columnspan=3)
        root.mainloop()

    def submit(self, param):
        self.out_windows.insert(END, param)
        self.result = self.result + param


if __name__ == '__main__':
    calculator = Calculator()


