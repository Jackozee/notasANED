import matplotlib.pyplot as plt
import numpy as np
import predictor_corrector as pc


def f(t, y):
    return np.exp(-y)


def lmap(f, xs):
    return [f(x) for x in xs]


def sol(t):
    return np.log(1 + t)


# parámetros para todos los métodos
a = [1]                                     # coeficientes corrector
b = [bi / 24 for bi in [9, 19, -5, 1]]      #
t0 = 0
tf = 1
hs = [1 / r for r in [1300, 600, 250, 110, 50, 20, 10]]

# parámetros variables según el método:
atilde = [1]                                # coeficientes predictor
btildes = [[3 / 2, -1 / 2], [1], [1]]       #
m = [1, 1, 2]                               # iteraciones de corrección
marks = ['v', 'o', 's']
labels = ['AB2-AM3, m=1', 'AB1-AM3, m=1', 'AB1-AM3, m=2']

# para graficar:
finalerrors = [[], [], []]

for i in [0, 1, 2]:
    for h in hs:
        condini = [0, sol(h), sol(2 * h)]
        ts, us = pc.predcor(
            atilde, btildes[i], a, b, h, f, t0, tf, condini, m[i]
        )
        finalerrors[i].append(abs(us[-1] - np.log(2)))
        # plt.semilogy(
        #     ts,
        #     abs(us - lmap(sol, ts)),
        #     color=(0.1, 10 * h, 0.5),
        #     label=h
        # )
    plt.loglog(hs, finalerrors[i], marks[i], label=labels[i])

plt.title("Error en el valor final de la solución obtenida")
plt.xlabel("h")
plt.ylabel("|y(1)-u_N|")
plt.legend()
plt.ylim([10**(-12), 10**(-2)])

plt.show()
