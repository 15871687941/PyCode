# encoding = utf-8
# 用户登录程序
# 基础需求：
# 让用户输入用户名密码
# 认证成功后显示欢迎信息
# 输错三次后退出程序
import json
# count = 0
# while count < 3:
#     username = input("请输入用户名:")
#     password = input("请输入密码:")
#     if (username == "username") and (password == "password"):
#         print("认证成功，欢迎！")
#     else:
#         print("认证失败，请重新登录")
#     count += 1

# 升级需求：
# 可以支持多个用户登录 (提示，通过列表存多个账户信息)
# 用户3次认证失败后，退出程序，再次启动程序尝试登录时，还是锁定状态（提示:需把用户锁定的状态存到文件里)
# userInformation = {
#     "user0": {"password": "password0", "status": 0},
#     "user1": {"password": "password1", "status": 0},
#     "user2": {"password": "password2", "status": 0}
# }
# with open("userInformation.txt", "w") as fp:
#     json.dump(userInformation, fp)
with open("userInformation.txt", "rb") as fp:
    userInformation = json.load(fp)
while True:
    username = input("请输入用户名:")
    try:
        if userInformation[username]["status"] >= 3:
            print("您已经认证三次失败，账户进入锁定状态！")
            with open("userInformation.txt", "w") as fp:
                json.dump(userInformation, fp)
            break
        password = input("请输入密码:")
        if userInformation[username]["password"] == password:
            print("认证成功，欢迎！")
            break
        else:
            print("密码错误，请重新认证！")
            userInformation[username]["status"] += 1
    except KeyError:
        print("您输入的用户名不存在，请重新认证！")





