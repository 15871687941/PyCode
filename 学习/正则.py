# start
# 1、使用正则表达式是干什么的？ 匹配字符串的
# s = "hello world"
# ret = s.find("ll")  # 2
# ret = s.find("k")  # -1
# ret = s.index("k")  # error
# res = s.replace('o', 'P')
# 字符串提供的方法是完全匹配
# 正则表达式是进行模糊匹配
import re
# 普通字符:
# 元字符:
#   .  匹配除了换行符(\n)之外的所有字符（通配符）
#   ^  以最开始的位置匹配（尖角符）
#   $  以结尾的位置匹配
#   *  重复匹配0到无穷次 {0，}
#   ？ 重复匹配0或1次 {0， 1}
print(re.findall(pattern="a?b", string="aaaaaabb"))
#   +  重复匹配1或无穷次 {1，}
#   {n}  重复匹配n次    {m,n}  重复匹配m到n次
print(re.findall(pattern="b{0,1}a", string="bbbba"))
#   [0-9] [a-z] [A-Z] [1,2,3,4]  字符集 代指其中字符之一
#   [^] 匹配除了括号内部字符的其他字符
print(re.findall(pattern="[^ab]", string="babab,a"))
#   | 或（管道符）
print(re.findall(pattern="b{0,1}", string="bbbba"))
#   ()  分组
ret = re.search(pattern="(as)+", string="sadadadasas")
print(ret.group())
ret = re.search(pattern="(as)|3+", string="as3")
print(ret.group())
ret = re.search(pattern=r"(?P<id>\d{3})\\(?P<name>\d{3})", string=r"123\456")
print(ret.group())
print(ret.group("id"))
print(ret.group("name"))

#   \   后跟元字符去除元字符特殊功能，后跟普通字符实现特殊功能：
#       \d=[0-9]  数字  \w=[a-zA-Z0-9]  字母   \D=[^0-9]  \W=[^a-zA-Z0-9]
#       \s=[\t\n\r\f\v]  空白字符  \S=[^\t\n\r\f\v]  \b  特殊字符（除字母）边界
print(re.findall(pattern=r"\.", string="I.am a Student."))
# 匹配出满足第一个条件的结果
# <_sre.SRE_Match object; span=(0, 1), match='a'>
ret = re.search(pattern=r"\\", string=r"b\low")
print(ret.group())
print(re.findall(r"[+\-*/()]", "1+2-3/8*6"))
# 11个元字符
# 》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》
# 正则表达式的方法：
# 1.findall() :所有的结果都返回一个列表里
# 2.search() :返回匹配到的一个对象（object)，对象可以调用group()返回结果
# 3.match() :只在字符串开始匹配,也返回匹配到的一个对象（object），对象可以调用group()返回结果
ret = re.match(pattern="asd", string="asdasd")
print(ret.group())
# 4.split() :
print(re.split(pattern="[j,s]", string="sdjksal"))
# 5.sub() :替换 脏话和谐
print(re.sub(pattern="操你妈", repl="***", string="assd操你妈aadad55ada5"))
# 6.compile: 将模式固定
# pattern = re.compile(pattern="\.com")
# pattern.findall()
# pattern.search()
# pattern.match()
# pattern.split()
# pattern.sub()
ret = re.search(pattern="(\d)(\w)", string="4a5s6d5d5f5c2f5fg")
print(ret.groups())







