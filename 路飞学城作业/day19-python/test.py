import re
string = "-1+-2*-3.6/-8.9"
x, sign, y = re.search(pattern="([-]?\d+\.?\d*)([/*])([-]?\d+\.?\d*)", string=string).groups()
x, y = float(x), float(y)
print(x, y)