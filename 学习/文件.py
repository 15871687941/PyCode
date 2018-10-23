with open("test1.txt", "r", encoding="utf-8") as fp:
    # print(fp.read())
    print(fp.tell())
    print(fp.name)
    print(fp.buffer)
    print(fp.closed)
    print(fp.encoding)
    print(fp.seek(0, 2))
    print(fp.tell())
    # fp.write('''
    #  我想摸你的头发，
    #  是最简单的生长。
    #  你好low呀！
    # ''')
