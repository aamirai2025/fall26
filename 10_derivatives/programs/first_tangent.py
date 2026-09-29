import numpy as np
import matplotlib.pyplot as plt

def func(x):
    return np.sin(x)

def dydx(x):
    return np.cos(x)

def newy(x, m, c):
    return m*x + c

x = np.linspace(0, 2*np.pi, 1000)
y = func(x)

x1 = np.deg2rad(float(input("Enter the angle (in degrees): ")))
y1 = func(x1)

m = dydx(x1)

c = y1 - m*x1

xl = x1 - np.pi/4
xh = x1 + np.pi/4

yl = newy(xl, m, c)
yh = newy(xh, m, c)

plt.plot(x, y, '-k')
plt.plot([xl, xh], [yl, yh], '--r')
plt.plot([-0.10, 2*np.pi],[0, 0], '-b')
plt.plot([0, 0], [-1.1, 1.1], '-b')
plt.scatter(x1, y1, s=50, c='r')
plt.xlim([-0.10, 2*np.pi])
plt.ylim([-1.1, 1.1])
plt.xlabel(r'$\theta$', size=14, weight='bold')
plt.ylabel('Functions', size=14, weight='bold')
plt.show()