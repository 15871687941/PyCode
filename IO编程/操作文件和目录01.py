import os, shutil
print(os.name)
# print(os.environ.keys())
# print(os.path.abspath('../'))
# print(os.path.join(r"\Users\michael", 'testdir.txt'))
# print(os.path.split(r"\Users\michael\testdir.txt"))
# print(os.path.splitext(r"\Users\michael\testdir.txt"))
# os.rename('example01.txt', 'test.txt')
# os.remove('test.txt')
print(os.listdir())
for dir in [x for x in os.listdir() if os.path.splitext(x)[1] == '.py']:
    print(dir)