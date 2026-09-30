import numpy as np
import matplotlib.pyplot as plt

def snd(x):
    return 1/(np.sqrt(2*np.pi))*np.exp(-x**2/2)

def sndd(x):
    return -x/(np.sqrt(2*np.pi))*np.exp(-x**2/2)

def snddd(x):
    return (x**2 - 1)/(np.sqrt(2*np.pi))*np.exp(-x**2/2)

x = np.linspace(-4, 4, 1000)
y = snd(x)

xps = np.array([-2.0, -0.4, 0.4, 2.0])
yps = snd(xps)
mps = sndd(xps)
cops = snddd(xps)
cps = yps - mps*xps
print(mps)
print(cops)

for i in range(len(xps)):
    plt.figure(figsize=(9, 5))
    plt.plot(x, y, '-k', linewidth=2)
    plt.plot([xps[i]-1, xps[i]+1], [mps[i]*(xps[i]-1)+cps[i], mps[i]*(xps[i]+1)+cps[i]], '--r', linewidth=2)
    plt.xlabel("x-axis", size=18, weight='bold')
    plt.ylabel("y-axis", size=18, weight='bold')
    plt.xticks(size=18, weight='bold')
    plt.yticks(size=18, weight='bold')
    plt.xlim([-4.1, 4.1])
    plt.ylim([0, 0.5])
    plt.text(-3.8, 0.45, f"m={mps[i]:<7.4f}, con={cops[i]:.4f}", size=18, weight='bold')
    plt.tight_layout()
    plt.savefig(f"slope_{i:d}.png")
