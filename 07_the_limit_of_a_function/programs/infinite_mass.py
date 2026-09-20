import math as m

c = 299792458
v = c - 0.0000000000000001*c

print(v**2/c**2)
print(1 - (v**2 / c**2))
print(m.sqrt(1 - (v**2 / c**2)))

mass = 1/m.sqrt(1 - (v**2 / c**2))

print(mass, "kg")