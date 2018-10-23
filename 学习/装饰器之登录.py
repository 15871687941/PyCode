import pickle
login_status = False


def login(auto_type=""):
    def login1(func):
        def inner(*argc, **kw):
            global login_status
            if not login_status:
                if auto_type == "jingdong":
                    username = input("username:")
                    password = input("password:")
                    with open("jdaccount.txt", "rb") as fp:
                        jd = pickle.load(fp)
                        print(jd)
                    if username == jd["username"] and password == jd["password"]:
                        func(*argc, **kw)
                        login_status = True
                    else:
                        pass
                elif auto_type == "weixin":
                    username = input("username:")
                    password = input("password:")
                    with open("wxaccount.txt", "rb") as fp:
                        wx = pickle.load(fp)
                    if username == wx["username"] and password == wx["password"]:
                        func()
                        login_status = True
                    else:
                        pass
            else:
                func()
        return inner
    return login1


@login(auto_type="jingdong")
def home():
    print("welcome to home page")


@login(auto_type="weixin")
def finance():
    print("welcome to home finance page")


@login(auto_type="jingdong")
def book():
    print("welcome to book page")


if __name__ == '__main__':
    print("当前可进入的页面：")
    print("home    finance    book")
    while True:
        option = input("请输入要进入的页面：")
        if option == "home":
            home()
        elif option == "finance":
            finance()
        else:
            book()

