import numpy as np

def slope_func(x):
    return (x**2 - 1) / (x - 1)

x = float(input("Enter starting value for x (near 1): "))
h = float(input("Enter step size h (> 0.000001): "))

if x > 1:
    vals = np.arange(x, 1.0+0.000001, -h)
    outs = slope_func(vals)
elif x < 1:
    vals = np.arange(x, 1.0-0.000001, h)
    outs = slope_func(vals)

print("    x            m    ")
print("---------    ---------")
for counter, val in enumerate(vals):
    print(f"{val:<9.6f}    {outs[counter]:<9.6f}")