import random as rd
import matplotlib.pyplot as plt

ws = []
N = 10000
for n in range(1, N):
    z = complex(6 * (rd.random() - 0.5), 6 * (rd.random() - 0.5))
    w = 1 + z + z**2 / 2
    if (abs(w) < 1):
        ws.append(z)


def lmap(f, lst):
    return [f(x) for x in lst]


plt.title("Región del plano complejo con |1+z+z²/2|<1")
plt.scatter(lmap(lambda x: x.real, ws), lmap(lambda x: x.imag, ws))
plt.xlim([-3, 3])
plt.ylim([-3, 3])
plt.xlabel("Re(z)")
plt.ylabel("Im(z)")
plt.show()
