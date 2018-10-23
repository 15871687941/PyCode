import time, datetime
print(time.time())  # 时间戳
# time.sleep(3)
print(time.clock())  # CPU执行的时间
print(time.localtime())
print(time.gmtime())
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print(time.ctime())
print(time.strptime("2015-06-23 12-14-23", "%Y-%m-%d %H-%M-%S"))
print(time.mktime(time.localtime()))
print(datetime.time())
print(datetime.datetime.now())  # 2018-10-14 18:03:33.136200
print(datetime.datetime.time())