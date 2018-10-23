# 1、作用域
# 2、高阶函数
# 3、闭包
# 4、开放封闭原则
import pickle
import time


def outer():
    x = 10

    def inner():
        print(x)

    print(x)
    return inner


def show_time(func):
    def inner(*argc, **kw):
        start = time.time()
        s = func(*argc, **kw)
        end = time.time()
        print(s, end - start)
    return inner


def foo():
    print("foo......")
    time.sleep(3)


@show_time
def bar():
    print("bar......")
    time.sleep(2)


@show_time
def add(*a):
    sums = 0
    for i in a:
        sums += i
    print(sums)


# foo = show_time(foo)  # @show_time
# bar = show_time(bar)
# foo()
# bar()
# add(1, 2, 5, 6, 5)
@show_time
def fib1(n):
    time.sleep(1)
    if n == 1 or n == 2:
        return 1
    else:
        return fib1(n - 1) + fib1(n - 2)


@show_time
def fib2(n):
    time.sleep(1)
    a = 1
    b = 1
    for i in range(1, n):
        a, b = b, a + b
    print(a)


if __name__ == '__main__':
    # with open("jdaccount.txt", "wb") as fp:
    #     pickle.dump({"username": "root", "password": "123456"}, fp)
    #
    # with open("wxaccount.txt", "wb") as fp:
    #     pickle.dump({"username": "root", "password": "123456"}, fp)
    print(fib2(10))
    print(fib1(10))




