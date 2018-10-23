# 登陆次数
count = 0
while True:
    if count == 3:
        print("您已经输错三次，自动退出程序")
        break
    username = input("请输入用户名：")
    password = input("请输入密码：")
    if username == "root" and password == "123456":
        print("认证成功,欢迎用户 %s " % username)
        break
    else:
        print("用户名密码错误，请重新输入！")
        count += 1
print("已退出程序！")

