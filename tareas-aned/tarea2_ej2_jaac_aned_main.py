import random as rd
import numpy as np
import matplotlib.pyplot as plt

ws = []
N = 15000


def cond1(z):
    w = 1 + z + z**2 / 2
    return (abs(w) < 1)


def cond2(z):
    r0 = (2 + np.sqrt(1 + 2 * z)) / (3 - 2 * z)
    r1 = (2 - np.sqrt(1 + 2 * z)) / (3 - 2 * z)
    return (abs(r0) < 1 and abs(r1) < 1)


for n in range(1, N):
    z = complex(8 * (rd.random() - 0.5), 8 * (rd.random() - 0.5))
    if cond2(z):
        ws.append(z)


def lmap(f, lst):
    return [f(x) for x in lst]


# plt.title("Región del plano complejo con |1+z+z²/2|<1")
plt.title("Región del plano complejo con |r0(z)|<1 y |r1(z)|<1")
plt.scatter(lmap(lambda x: x.real, ws), lmap(lambda x: x.imag, ws))
plt.xlim([-4, 4])
plt.ylim([-3, 3])
plt.xlabel("Re(z)")
plt.ylabel("Im(z)")
plt.show()
