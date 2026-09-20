import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(x) / x

x_values = np.linspace(-0.0000001, 0.0000001, 1000)

plt.plot(x_values, f(x_values), linewidth=2, color='k')
plt.xticks(fontsize=12, fontweight='bold')
plt.yticks(fontsize=12, fontweight='bold')
plt.xlabel('x', fontsize=14, fontweight='bold')
plt.ylabel('f(x)', fontsize=14, fontweight='bold')
plt.title("Microscopic Step Increments in x", fontsize=16, fontweight='bold')
plt.grid(True)
plt.show()