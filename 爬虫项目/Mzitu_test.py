import requests
from bs4 import BeautifulSoup
# import sqlite3
# res = requests.get("http://m.mzitu.com/152059/3")
# html = res.text
# soup = BeautifulSoup(html, "lxml")
# img = soup.select("figure p a img")[0]
# print(img.attrs["src"])
# conn = sqlite3.connect('test.db')
# print("Opened database successfully")
# c = conn.cursor()
# c.execute('''Create TABLE COMPANY
# (ID INT PRIMARY KEY NOT NULL,
# NAME TEXT NOT NULL,
# AGE INT NOT NULL,
# ADDRESS CHAR(50),
# SALARY REAL
# );''')
# c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
# VALUES(1, 'Paul', 32, 'California', 20000.00)")
# c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (2, 'Allen', 25, 'Texas', 15000.00 )")
#
# c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )")
#
# c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )")
# print("Table created successfully")
# cursor = c.execute("SELECT * FROM COMPANY")
# print(cursor)
# for row in cursor:
#     print('''
#     ID = {},
#     NAME = {},
#     ADDRESS = {},
#     SALARY = {}
#     '''.format(row[0], row[1], row[2], row[3]))
# c.execute("UPDATE COMPANY SET SALARY = 25000.00 WHERE ID = 1")
# c.execute("DELETE FROM COMPANY WHERE ID = 2")
# conn.commit()
# cursor = conn.execute("SELECT * FROM COMPANY")
# for row in cursor:
#     print('''
#     ID = {},
#     NAME = {},
#     ADDRESS = {},
#     SALARY = {}
#     '''.format(row[0], row[1], row[2], row[4]))
# # print("Records created successfully")
# conn.close()
# import pymongo
# client = pymongo.MongoClient("mongodb://localhost:27017/")
# db_list = client.list_database_names()
# if 'test' in db_list:
#     print("数据库已存在！")
# else:
#     print("数据库不存在！")
# import sqlite3
# conn = sqlite3.connect("Mzitu.db")
# cursor = conn.cursor()
# # cursor.execute('''CREATE TABLE PICTURE
# # (ID INT PRIMARY KEY NOT NULL,
# # CLASS CAHR(50),
# # URL TEXT
# # );''')
# data = cursor.execute("SELECT * FROM PICTURE")
# for row in data:
#     print(row)
# # cursor.execute("DELETE FROM PICTURE")
# # print("deleted successfully!")
# conn.commit()
# cursor.close()
# conn.close()
import pymongo
my_client = pymongo.MongoClient("mongodb://localhost:27017/")
# my_db = my_client['test']
# print("successfully")
my_dbs = my_client.list_database_names()
print(my_dbs)
my_db = my_client["movie"]
my_col = my_db["next_us"]
# # my_col.update({"name": "RUNOOB"}, {"$set": {"aleax": "1236545555", "name": "菜鸟"}})
# # print(my_col.find_one())
count = 0
for i in my_col.find():
    count += 1
    print(count, i)
# my_col.remove()
# # my_dict = {"name": "RUNOOB", "aleax": "10000", "url": "https://www.runoob.com"}
# # x = my_col.insert_one(my_dict)
# # print(x)


