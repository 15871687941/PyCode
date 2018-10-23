import os, json


# 提现
def give_money():
    pass


# 登录
def login_atm():
    pass


# 转账
def change_money():
    with open("ATM.json", "r") as fp:
        users = json.load(fp)
    username = input("请输入你的用户名：")
    password = input("请输入您的密码：")
    for user in users:
        if user["username"] == username:
            if user["password"] == password:
                if user["status"]:
                    money = int(input("请输入转账金额："))
                    user["salary"] -= money
                    ouser = input("请输入被转账的用户名：")
                    for user in users:
                        if user["username"] == ouser:
                            if user["status"]:
                                user["salary"] += money
                                with open("ATM.json", "w") as fp:
                                    json.dump(users, fp)
                                print("转账成功！")
                                break
                            else:
                                print("账户已被冻结！")
                    else:
                        print("被转账的用户不存在！")
                else:
                    print("账户已被冻结！")
            else:
                print("密码错误！")
    else:
        print("用户名不存在！")


# 添加账户或用户额度
def add_user(option):
    if option == "U":
        if not os.path.exists("ATM.json"):
            with open("ATM.json", "w") as fp:
                users = []
                user = {}
                username = input("请输入用户名：")
                password = input("请输入密码：")
                repassword = input("请再输入密码：")
                if password == repassword:
                    user["username"] = username
                    user["password"] = password
                    user["salary"] = 15000
                    user["status"] = True
                    users.append(user)
                    json.dump(users, fp)
                else:
                    print("两次密码不一致！")
        else:
            with open("ATM.json", "r") as fp:
                users = json.load(fp)
            user = {}
            username = input("请输入用户名：")
            for user in users:
                if user["username"] == username:
                    print("用户名已存在！")
                    break
            else:
                password = input("请输入密码：")
                repassword = input("请再输入密码：")
                if password == repassword:
                    user["username"] = username
                    user["password"] = password
                    user["salary"] = 15000
                    user["status"] = True
                    users.append(user)
                    with open("ATM.json", "w") as fp:
                        json.dump(users, fp)
                else:
                    print("两次密码不一致！")
    elif option == "M":
        with open("ATM.json", "r") as fp:
            users = json.load(fp)
            # TODO hello world
        username = input("请输入你的用户名：")
        password = input("请输入您的密码：")
        for user in users:
            if user["username"] == username:
                if user["password"] == password:
                    if user["status"]:
                        money = int(input("请输入你要添加的用户额度："))
                        user["salary"] += money
                        with open("ATM.json", "w") as fp:
                            json.dump(users, fp)
                        print("添加成功")
                        break
                    else:
                        print("账户已被冻结！")
                else:
                    print("密码错误")
        else:
            print("用户名不存在！")


# 冻结账户
def stay_account():
    with open("ATM.json", "r") as fp:
        users = json.load(fp)
    username = input("请输入你的用户名：")
    password = input("请输入您的密码：")
    for user in users:
        if user["username"] == username:
            if user["password"] == password:
                user["status"] = False
                with open("ATM.json", "w") as fp:
                    json.dump(users, fp)
                print("冻结成功")
                break
            else:
                print("密码错误")
    else:
        print("用户名不存在！")


# 还款
def return_money():
    pass


if __name__ == '__main__':
    option = input("请输入操作选项：")
    while True:
        if option == "U":
            add_user(option=option)
        elif option == "M":
            add_user(option=option)
        elif option == "Q":
            exit(0)
        else:
            pass
        option = input("请输入操作选项：")