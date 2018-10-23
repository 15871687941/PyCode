# from colorama import init, Fore
# init(autoreset=True)


# 红色高亮打印
import pickle


def print_red(string):
    print("\033[1;31;40m%s\033[0m" % string)


# 绿色高亮打印
def print_green(string):
    print("\033[1;33;40m%s\033[0m" % string)


# 辅助参数信息
goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998}
]
buy_goods = []
status = {}

username = input("请输入用户名：")
password = input("请输入密码：")
# 验证用户名密码
if username != "root" and password != "123456":
    print_red("用户名密码错误！")
# 购买
else:
    with open("status.txt", "rb") as fp:
        status = pickle.load(fp)
    salary = status["rest_of_salary"]
    buy_goods = status["consume_record"]
    if not salary:
        salary = int(input("请输入工资："))
    print("正在打印商品列表......")
    for index, value in enumerate(goods, 1):
        print(index, value["name"], value["price"])
    print_red("您的余额为{}".format(salary))
    while True:
        index = int(input('''
-1 查询消费记录     0 退出程序
请选择所要购买的商品的序号(输入序号0可退出)：'''))
        if index == -1:
            print("您的消费记录为：")
            for i in buy_goods:
                print_red(i)
        elif index == 0:
            print("正在退出中......")
            print("您已经购买了：")
            for i in buy_goods:
                print(i, sep="  ")
            break
        elif index < len(goods) + 1:
            if goods[index - 1]["price"] > salary:
                print_red("余额不够！")
            else:
                print("正在加入购物车中......")
                salary -= goods[index - 1]["price"]
                buy_goods.append(goods[index - 1]["name"])
                print_red("商品已加入购物车！")
                print_red("您的余额还剩{}".format(salary))
        else:
            print_red("您输入的商品序号不存在，请重新输入！")
    # 存储购买信息
    status["rest_of_salary"] = salary
    status["consume_record"] = buy_goods
    with open("status.txt", "wb") as fp:
        pickle.dump(status, fp)
print("退出成功")




