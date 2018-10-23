import pickle
import json
import shelve
# data = {"k1": 123, "k2": "Hello"}
# p_str = pickle.dumps(data)
# print(p_str)
# with open("result.pk", "wb") as fp:
#     pickle.dump(data, fp)
# with open("result.json", "w") as fp:
#     json.dump(data, fp)
d = shelve.open("shelve_test")


class Test:
    def __init__(self, n):
        self.n = n


for k in d:
    print(d[k])
d.close()

