from io import StringIO
from io import BytesIO
# s = StringIO()
# s.write('asdfdsasdf')
# s.write('zxcvbnm')
# print(s.getvalue())
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
# f.write('中文'.encode())
print(f.getvalue().decode())