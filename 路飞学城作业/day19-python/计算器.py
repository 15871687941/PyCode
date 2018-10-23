import re


# 合法化检测
def check(string=""):
    flag = True
    # 检测是否有字母
    if re.findall(pattern="[a-zA-Z]", string=string):
        print("Invalid")
        flag = False
    return flag


# 格式化处理
def process(string=""):
    string = string.replace(" ", "")
    string = string.replace("++", "+")
    string = string.replace("+-", "-")
    string = string.replace("--", "+")
    string = string.replace("-+", "-")
    string = string.replace("*+", "*")
    string = string.replace("/+", "/")
    return string


# 乘除法的计算
def cal_mul_div(string=""):
    while re.search(pattern="[/*]", string=string):
        x, sign, y = re.search(pattern="(-?\d+\.?\d*)([/*])(-?\d+\.?\d*)", string=string).groups()
        # x, y = float(x), float(y)
        if sign == "*":
            z = float(x) * float(y)
        if sign == "/":
            z = float(x) / float(y)
        string = string.replace(x + sign + y, str(z))
    return string


# 加减法计算
def cal_add_sub(string=""):
    while re.search(pattern="(-?\d+\.?\d*)([-+])(-?\d+\.?\d*)", string=string):
        x, sign, y = re.search(pattern="(-?\d+\.?\d*)([-+])(-?\d+\.?\d*)", string=string).groups()
        # x, y = float(x), float(y)
        if sign == "+":
            z = float(x) + float(y)
        else:
            z = float(x) - float(y)
        string = string.replace(x + sign + y, str(z))
    return string


if __name__ == '__main__':
    source = "1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )"
    source = "1 - (2*8/4-6)+6"
    if check(source):
        s = process(source)
        while re.search(pattern="\(", string=s):
            strs = re.search(pattern=r"\([^()]+\)", string=s).group()  # (-40/5+8)
            strs_replace = cal_mul_div(string=strs)  # (-8+8)
            strs_replace = cal_add_sub(string=strs_replace)  # (0)
            s = s.replace(strs, strs_replace[1:-1])
            s = process(s)

        else:  # 循环结束后，仍然执行else语句，不同于if...else... 和 for...else...
            strs_replace = cal_mul_div(string=s)  # (-8+8)
            strs_replace = cal_add_sub(string=strs_replace)  # (0)
            s = s.replace(s, strs_replace)
        print("表达式的结果为>>>", float(s))
    else:
        print("表达式不合法！")
