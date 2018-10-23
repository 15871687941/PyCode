import pickle
import os
if os.path.exists("userinfo.txt"):
    with open("userinfo.txt", "rb") as fp:
        informations = pickle.load(fp)
else:
    # 用户名    密码  登录次数
    informations = [
    ["root1", "123456", 0],
    ["root2", "123456", 0],
    ["root3", "123456", 0],
    ["root4", "123456", 0],
    ["root5", "123456", 0],
    ["root6", "123456", 0],
]
while True:
    username = input("请输入用户名：")
    password = input("请输入密码：")
    for user in informations:
        if username == user[0]:
            if user[2] < 2:
                if password == user[1]:
                    print("认证成功,欢迎用户 %s " % username)
                    exit(0)
                else:
                    user[2] += 1
                    print("密码错误请重新输入！")
                    break
            else:
                print("您已经输错三次，账号已被锁定！")
                with open("userinfo.txt", "wb") as fp:
                    pickle.dump(informations, fp)
                exit(0)
        else:
            print("用户名不存在！")
            break


