import numpy as np

def f(x):
    return x**2

a = float(input("Enter the start of domain: "))
b = float(input("Enter the domain end: "))
n = int(input("Enter the number of rectangles: "))

dx = (b - a)/n

width = np.linspace(a, b, n+1)

rsum = 0
lsum = 0

print("S. No.     R_Sum           L_Sum")
print("=======    ============    ============")

for counter in range(len(width)-1):
    rsum += f(width[counter + 1])*dx
    lsum += f(width[counter])*dx
    print(f"{counter + 1:<11d}{rsum:<16.4g}{lsum:<16.4g}")