import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as col


def cond1(z):
    w = 1 + z + z**2 / 2
    return (abs(w) < 1)


def cond2(z):
    r0 = (2 + np.sqrt(1 + 2 * z)) / (3 - 2 * z)
    r1 = (2 - np.sqrt(1 + 2 * z)) / (3 - 2 * z)
    return (abs(r0) < 1 and abs(r1) < 1)


m = 1000
n = 1000

plt.title("(Amarillo) Región del plano complejo con |1+z+z²/2|<1")
xmin, xmax = -3, 3
ymin, ymax = -3, 3
f = cond1

# plt.title("(Amarillo) Región del plano complejo con |r0(z)|<1 y |r1(z)|<1")
# xmin, xmax = -4, 4
# ymin, ymax = -3, 3
# f = cond2

xs, ys = np.meshgrid(np.linspace(xmin, xmax, m), np.linspace(ymin, ymax, n))
zs = [[complex(xs[i, j], ys[i, j]) for j in range(0, m)] for i in range(0, n)]
resultado = [[f(zs[i][j]) for j in range(0, m)] for i in range(0, n)]

plt.imshow(resultado,
           extent=(xs.min(), xs.max(), ys.min(), ys.max()),
           origin="lower",
           cmap=col.ListedColormap(['#93E740', '#F2F226'])
           )
plt.xlabel("Re(z)")
plt.ylabel("Im(z)")
plt.show()
