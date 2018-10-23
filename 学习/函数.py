# 参数顺序：
# 必选参数 默认参数 可变参数 命名关键字参数 关键字参数


# 1、位置参数
def print_info(name, age):
    print("I am {0}, I am {1} years old.".format(name, age))


print_info("Will", 21)
print_info(21, "Will")


# 2、默认参数
def print_info(name, age=20):
    print("I am {0}, I am {1} years old.".format(name, age))


print_info(20, "Will")


# 3、可变参数
def _sum(*numbers):
    s = 0
    for n in numbers:
        s += n
    print(s)


# 4、关键字参数
# def person(name, age, **kw):
#     print(type(kw))
#     print("name: ", name, "age: ", age, "others: ", kw)


# 5、命名关键字参数
def person(name, age, *, city, job):
    print("name: ", name, "age: ", age, "city: ", city, "job: ", job)


person("Will", 20, city="XiangYang", job="Student")
_sum(1, 2, 3, 5, 8, 9)
_sum(6, 5)
_sum()