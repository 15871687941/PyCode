import random
# print(random.random())  # 0.23819965127161502(0~1)
# print(random.randint(1, 8))  # 8
# print(random.choice("Hello"))  # o 可以随机一个序列
# print(random.shuffle([1, 2, 5, 6]))
# print(random.randrange(1, 3))
# print(random.sample(["H", "0", "1", "5", [1, 2, 3]], 2))


def v_code():
    code = ""
    for i in range(5):
        add = random.choice([random.randrange(10), chr(random.randrange(65, 91))])
        code += str(add)
    return code


if __name__ == '__main__':
    li = [1, 2, 5, 6, 'a']
    random.shuffle(li)
    print(li)
    print(v_code())
    # print(ord('a'))
    # print(ord('z'))
    # print(ord('A'))
    # print(ord('Z'))
    # print(random.randrange(10))

