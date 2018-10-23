import pickle, json

d = dict(name='鲍勃', age=20, score=88)
# res = pickle.dumps(d)
# res = pickle.loads(b'\x80\x03}q\x00(X\x04\x00\x00\x00nameq\x01X\x03\x00\x00\x00Bobq\x02X\x03\x00\x00\x00ageq\x03K\x14X\x05\x00\x00\x00scoreq\x04KXu.')
# with open("example.txt", "wb") as f:
    # pickle.dump(d, f)
# with open("example.txt", "rb") as f:
    # res = pickle.load(f)
    #print(res)


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }


if __name__ == '__main__':
    d = dict(name='鲍勃', age=20, score=88)
    s = Student('Bob', 20, 88)
    print(json.dumps(d, ensure_ascii=False))
    print(json.dumps(s, default=lambda obj: obj.__dict__))
