import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(np.pi / x)


x_left = np.linspace(-1, -0.0003, 10000)
x_right = np.linspace(0.0003, 1, 10000)

y_left = f(x_left)
y_right = f(x_right)

plt.plot(x_left, y_left, linewidth=2)
plt.plot(x_right, y_right, linewidth=2)
plt.xticks(fontsize=12, fontweight='bold')
plt.yticks(fontsize=12, fontweight='bold')
plt.xlabel('x', fontsize=14, fontweight='bold')
plt.ylabel('f(x)', fontsize=14, fontweight='bold')
plt.grid(True)
plt.show()
