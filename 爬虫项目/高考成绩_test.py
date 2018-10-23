import matplotlib.pyplot as plt
import numpy as np
import math

# x = np.linspace(0, 5, 50)
# y = [math.sin(i) for i in x]
# plt.bar(x, y, facecolor='#9999ff', edgecolor='white')
x = [i for i in range(0, 20)]
y = [i for i in x]
plt.figure()
plt.plot(x, y)
plt.xlabel("Hello")
plt.ylabel("World")
plt.xticks([i for i in range(0, 20, 1)])
plt.show()