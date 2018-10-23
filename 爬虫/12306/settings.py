username = "15871687941"
password = "asd2743075"
point = {
    '1': "38,43",
    '2': "106,46",
    '3': "175,46",
    '4': "262,41",
    '5': "39,116",
    '6': "125,115",
    '7': "184,116",
    '8': "249,116"
}


def get_answer():
    index = input("请输入验证码的坐标：")
    index = index.split(',')
    temp = []
    for item in index:
        temp.append(point[item])
    return ','.join(temp)