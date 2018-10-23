import hashlib
import hmac


# m = hashlib.md5()
# m.update("admin".encode())  # 参数为bytes对象
# # m.update("root".encode())
# print(m.hexdigest())
# m = hashlib.sha1()
# m.update("admin".encode())
# print(m.hexdigest())

h = hmac.new("天王盖地虎".encode(), "宝塔镇河妖".encode())
print(h.hexdigest())
