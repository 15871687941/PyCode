import re
# string = "1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )"
# # print(re.findall(pattern="[+\-*/()]", string=string))
# # ret = re.search(pattern="\([^()]+\)", string=string)
# # print(ret.group())
# # string = "-5*6-7+8+5+7"
# # 1、检测
# check_alpha = re.findall(pattern="[a-zA-z]", string=string)
# check_bracket = re.findall(pattern="[()]", string=string)
# print(check_alpha, check_bracket)
# if len(check_alpha) != 0 or len(check_bracket)%2 != 0:
#     print("输入的算式格式有误！")
#
# # 2、去空格
# string = re.sub(pattern="\s", repl="", string=string)
# print(string)
# # 3、计算
# result_bracket = re.search(pattern="\([^()]+\)", string=string)
# while result_bracket:
#     result = result_bracket.group()
#     # 1、先乘除
#     result2 = re.search(pattern="(-?\d+)([*/])(\d+)", string=result)
#     while result2:
#         result3 = result2.groups()
#         result2 = result2.group()
#         print(result2, result3)
#         if result3[1] == "*":
#             result4 = int(result3[0]) * int(result3[2])
#             print(result4)
#             result = re.sub(pattern=result3[0] + "\\" + result3[1] + result3[2], repl=str(result4), string=result)
#             print(result)
#         if result3[1] == "/":
#             result4 = int(result3[0]) / int(result3[2])
#             print(result4)
#             result = re.sub(pattern=result3[0] + "\\" + result3[1] + result3[2], repl=str(result4), string=result)
#             print(result)
#         result2 = re.search(pattern="(\d+)([*/])(\d+)", string=result)
#     # 2.后加减
#     result2 = re.search(pattern="(\d+)([+-])(\d+)", string=result)
#     while result2:
#         result3 = result2.groups()
#         result2 = result2.group()
#         print(result3)
#         if result3[1] == "+":
#             result4 = int(result3[0]) + int(result3[2])
#             result = re.sub(pattern=result3[0] + "\\" + result3[1] + result3[2], repl=str(result4), string=result)
#             print(result)
#         if result3[1] == "-":
#             result4 = int(result3[0]) - int(result3[2])
#             result = re.sub(pattern=result3[0] + "\\" + result3[1] + result3[2], repl=str(result4), string=result)
#             print(result)
#         result2 = re.search(pattern="(\d+)([+-])(\d+)", string=result)
#     # 3、替换
#     result5 = re.search(pattern="[^()]+", string=result).group()
#     print(result5)
#     string = re.sub(pattern=result2, repl=result5, string=string)
#     result_bracket = re.search(pattern="\([^()]+\)", string=string)
# # 4、综合
# result2 = re.search(pattern="(\d+)([*/])(\d+)", string=string)
# while result2:
#     result3 = result2.groups()
#     result2 = result2.group()
#     print(result2, result3)
#     if result3[1] == "*":
#         result4 = int(result3[0]) * int(result3[2])
#         print(result4)
#         string = re.sub(pattern=result3[0] + "\\" + result3[1] + result3[2], repl=str(result4), string=string)
#         print(string)
#     if result3[1] == "/":
#         result4 = int(result3[0]) / int(result3[2])
#         print(result4)
#         string = re.sub(pattern=result3[0] + "\\" + result3[1] + result3[2], repl=str(result4), string=string)
#         print(result)
#     result2 = re.search(pattern="(\d+)([*/])(\d+)", string=string)
# result2 = re.search(pattern="(\d+)([+-])(\d+)", string=string)
# print(result2)
# while result2:
#     result3 = result2.groups()
#     result2 = result2.group()
#     print(result3)
#     if result3[1] == "+":
#         result4 = int(result3[0]) + int(result3[2])
#         string = re.sub(pattern=result3[0] + "\\" + result3[1] + result3[2], repl=str(result4), string=string)
#         print(string)
#     if result3[1] == "-":
#         result4 = int(result3[0]) - int(result3[2])
#         string = re.sub(pattern=result3[0] + "\\" + result3[1] + result3[2], repl=str(result4), string=string)
#         print(string)
#     result2 = re.search(pattern="(\d+)([+-])(\d+)", string=string)
# print(string)


def give_re(pattern):
    pattern = list(pattern)
    new_pattern = list()
    for j in pattern:
        if j in ".^$*?+{}[]|()\\":
            new_pattern.append("\\")
            new_pattern.append(j)
        else:
            new_pattern.append(j)
    new_pattern = "".join(new_pattern)
    return new_pattern


# 1、算式整理
def clear(string):
    string = re.sub(pattern="\s", repl="", string=string)
    return string


# 2、检测函数
def check(string):
    check_alpha = re.findall(pattern="[a-zA-Z]", string=string)
    check_bracket = re.findall(pattern="[()]", string=string)
    if len(check_alpha) != 0 or len(check_bracket) % 2 != 0:
        print("输入的算式格式有错误,请认真检查！")
        return False
    else:
        return True


# 3、提取括号
def get_bracket(string):
    result = re.search(pattern="\([^()]+\)", string=string)
    if result:
        result = result.group()
        result = re.sub(pattern="[()]", repl="", string=result)
        return result
    else:
        return None


# 4、先算乘除
def get_mul_div(expression):
    result = re.search(pattern="(\d+)([*/])(\d+)", string=expression)
    while result:
        if "*" == result.groups()[1]:
            res = int(result.groups()[0]) * int(result.groups()[2])
        if "/" == result.groups()[1]:
            res = int(result.groups()[0]) / int(result.groups()[2])
        print(str(res))
        result = give_re(result.group())
        expression = re.sub(pattern=result, repl=str(res), string=expression)
        result = re.search(pattern="(\d+)([*/])(\d+)", string=expression)
    return expression


# 5、后算加减
def get_add_sub(expression):
    result = re.search(pattern="(\d+)([-+])(\d+)", string=expression)
    while result:
        if "+" == result.groups()[1]:
            res = int(result.groups()[0]) + int(result.groups()[2])
        if "-" == result.groups()[1]:
            res = int(result.groups()[0]) - int(result.groups()[2])
        result = give_re(result.group())
        expression = re.sub(pattern=result, repl=str(res), string=expression)
        result = re.search(pattern="(\d+)([-+])(\d+)", string=expression)
    return expression


if __name__ == '__main__':
    # s = "1 - 2 * ( (60-30 +(40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (4*3)/ (16-3*2) )"
    s = "1+2+3+4+5*6/8-9"
    s = clear(string=s)
    print(s)
    if check(string=s):
        print("一切OK")
        result = get_bracket(string=s)
        while result:
            expression = get_mul_div(expression=result)
            expression = get_add_sub(expression=expression)
            s = re.sub(pattern="\(" + result + "\)", repl=expression, string=s)
            print(s)
            result = get_bracket(string=s)
        expression = get_mul_div(expression=s)
        expression = get_add_sub(expression=expression)
        pattern = give_re(s)
        s = re.sub(pattern=pattern, repl=expression, string=s)
        print(s)












