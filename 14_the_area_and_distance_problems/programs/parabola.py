import numpy as np

def f(x):
    return x**2
    
start = float(input("Enter the starting point: "))
stop = float(input("Enter the stopping point: "))
sub_intervals = int(input("Enter the number of subintervals: "))

delta_x = np.linspace(start, stop, sub_intervals+1)
width = delta_x[1]

areas = width*f(delta_x)

sum_right = np.sum(areas[1:])
print(f"R = {sum_right:.6f}")

sum_left = np.sum(areas[:-1])
print(f"L = {sum_left:.6f}")

