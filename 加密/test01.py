# coding = utf-8
# 字符串异或加密
import random
choice = input('加密（1）还是解谜（2）？')


def encode(str1, key):
    #设置秘钥种子
    random.seed(key)
    str2 = ''
    for c in str1:
        str2 += str(ord(c) ^ random.randint(0, 255))+','
    str2 = str2.strip(',')
    return str2


def decode(str2, key):
    random.seed(key)
    str1 = ''
    for i in str2.split(","):
        i = int(i)
        str1 += chr(i ^ random.randint(0, 255))
    return str1



if choice == '1':
    str1 = input("请输入要加密的明文：")
    key = input('请输入秘钥：')
    str2 = encode(str1, key)
    print(str2)
elif choice == '2':
    str2 = input("请输入密文，数字用逗号分隔：")
    key = input('请输入秘钥：')
    str1 = decode(str2, key)
    print(str1)
else:
    print("输入错误！")
