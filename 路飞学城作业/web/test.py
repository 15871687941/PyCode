# import bin
from bin import mul
import os
print(mul(1, 2, 3, 4))
print(__file__)
print(os.path.dirname(os.path.abspath(__file__)))
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))