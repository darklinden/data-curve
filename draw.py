#!/python3
# -*- utf8 -*-

import numpy as np
import matplotlib.pyplot as plt

# 等级区间
x = np.linspace(1, 1000, 1000)

# 三次方曲线
a = np.linspace(-1, 1, 1000)
b = np.power(a, 3)
y = (b + 1) * 200
plt.plot(x, y, color='red', label='property level')

# Logistic模型 对数曲线
c = np.linspace(-3.82, 3.82, 1000)
d = 1.0 / (1.0 + np.exp(-c))
yy = d * 400
plt.plot(x, yy, color='blue', label='property level')

plt.legend()

plt.show()
