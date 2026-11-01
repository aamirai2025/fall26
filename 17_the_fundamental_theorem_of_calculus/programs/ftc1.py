import numpy as np
import matplotlib.pyplot as plt

def g(x):
    return -np.cos(x) + np.cos(0)
    
t = np.array([0, (np.pi)/4, (np.pi)/2, (3*np.pi)/4, np.pi, (5*np.pi)/4])
area = g(t)
print(area)

