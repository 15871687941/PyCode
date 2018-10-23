menu = {
    "北京": {
        "海淀": {
            "五道口": {
                "soho": {},
                "网易": {},
                "google": {},
            },
            "中关村": {
                "爱奇艺": {},
                "汽车之家": {},
                "youku": {},
            },
            "上地": {
                "百度": {},
            },
        },
        "昌平": {
            "沙河": {
                "老男孩": {},
                "北航": {},
            },
            "天通苑": {},
            "回龙观": {},
        },
        "朝阳": {},
        "东城": {},
    },
    "上海": {
        "闵行": {
            "人民广场": {
                "炸鸡店": {},
            },
        },
        "闽北": {
            "火车站": {
                "携程": {},
            }
        },
        "浦东": {},
    },
    "山东": {},
}
menus_last = []
print("START".center(50, "-"))
while True:
    print("-".center(50, "-"))
    if len(menu) == 0:
        print("当前菜单为空，请返回上级菜单或退出！")
    print("当前菜单选项如下：")
    for i in menu:
        print(i, end="    ")
    print(end="\n")
    print("0:退出程序    1:进入下级菜单    2：返回上级菜单")
    index = int(input("请输入要执行的选项："))
    if index == 0:
        print("正在退出程序......")
        break
    elif index == 1:
        next_ = input("请输入要进入的下级菜单名称：")
        menus_last.append(menu)
        menu = menu.get(next_)
    else:
        if len(menus_last) == 0:
            print("当前菜单已经是最高一级菜单！")
        else:
            menu = menus_last.pop()
print("END".center(50, "-"))
print("程序已退出！")



