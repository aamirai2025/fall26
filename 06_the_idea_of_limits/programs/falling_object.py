import numpy as np
import matplotlib.pyplot as plt

def distance(t):
    return 4.9*t**2

h = float(input("Enter step size h (> 0.000001): "))

t_values = np.arange(0, 10, h)
distances = distance(t_values)

slope = (distance(5+h) - distance(5))/h
c = distance(5) - slope*5

x = np.array([0, 10])
y = slope*x + c

plt.plot(t_values, distances, '-b', linewidth=2)
plt.plot(x, y, '-r', linewidth=2)
plt.scatter(5, distance(5), color='k', s=100)
plt.xlabel('t', fontsize=14, fontweight='bold')
plt.ylabel('s', fontsize=14, fontweight='bold')
plt.xticks(fontsize=12, fontweight='bold')
plt.yticks(fontsize=12, fontweight='bold')
plt.title('Velocity of Falling Object', fontsize=14, fontweight='bold')
plt.grid(True)
plt.show()
