import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (x - 1) / (x**2 - 1)

h = float(input("Enter the step size (h) for approaching the limit (>0.000001): "))
start = float(input("Enter the starting point for the graph (e.g., 0.5): "))
end = float(input("Enter the ending point for the graph (e.g., 1.5): "))

if start > end:
    x_values_1 = np.arange(1-h, start, -h)
    x_values_2 = np.arange(1+h, end, h)
    x_values = np.concatenate((x_values_1, x_values_2))
elif start < end:
    x_values_1 = np.arange(start, 1-h, h)
    x_values_2 = np.arange(1+h, end, h)
    x_values = np.concatenate((x_values_1, x_values_2))
elif start == end:
    print("Start and end points cannot be the same. Please enter different values.")

plt.plot(x_values, f(x_values), label='f(x) = (x - 1) / (x^2 - 1)', color='blue')
plt.scatter([1], [0.5], edgecolor='red', facecolor='none')
plt.xlabel('x', fontsize=14, fontweight='bold')
plt.ylabel('f(x)', fontsize=14, fontweight='bold')
plt.xticks(fontsize=12, fontweight='bold')
plt.yticks(fontsize=12, fontweight='bold')
plt.grid(True)
plt.show()