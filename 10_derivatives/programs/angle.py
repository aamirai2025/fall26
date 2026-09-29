import numpy as np


m = np.cos(np.pi/4)
c = 0.1513

x1 = 0.0
y1 = m*x1 + c

x2 = np.pi/2
y2 = m*x2 + c

pi = np.array([x1, y1])
pf = np.array([x2, y2])

a = pf - pi

b = np.array([np.pi/2, 0.0])

adotb = np.dot(a, b)

am = np.linalg.norm(a)

bm = np.linalg.norm(b)

term = adotb/(am*bm)

theta = np.arccos(term)

print(np.tan(theta))