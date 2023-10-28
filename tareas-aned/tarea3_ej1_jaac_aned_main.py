import matplotlib.pyplot as plt
import math
import RKF45 as jaac


def sol(t):
    return math.exp(t - t**2)


def unzip(lls):
    return [ls[0] for ls in lls], [ls[1] for ls in lls]


A = \
    [
        [0, 0, 0, 0, 0, 0],
        [1 / 4, 0, 0, 0, 0, 0],
        [3 / 32, 9 / 32, 0, 0, 0, 0],
        [1932 / 2197, -7200 / 2197, 7296 / 2197, 0, 0, 0],
        [439 / 216, -8, 3680 / 513, -845 / 4104, 0, 0],
        [-8 / 27, 2, -3544 / 2565, 1859 / 4104, -11 / 40, 0]
    ]
b = [25 / 216, 0, 1408 / 2565, 2197 / 4104, -1 / 5, 0]
bT = [16 / 135, 0, 6656 / 12825, 28561 / 556430, -9 / 50, 2 / 55]


def f(t, y):
    return (1 - 2 * t) * y


ts, us, pts, ptsrechazados = \
    jaac.RKF45(
        A, b, bT,
        f, tinicial=0, tfinal=4, condinicial=1,
        hmax=0.1, tolerancia=0.01, orden=4
    )

# plt.plot(ts, us)
# plt.title("Solución")
# plt.xlabel("t")
# plt.ylabel("y")
# plt.ylim([0, 2])


# err = [abs(us[i] - sol(ts[i])) for i in range(0, len(ts))]
# plt.plot(ts, err, "r")
# plt.title("Error")
# plt.xlabel("t")
# plt.ylabel("error")


ts, hs = unzip(ptsrechazados)
plt.plot(ts, hs, "rx")
ts, hs = unzip(pts)
plt.plot(ts, hs, "bo")
plt.title("Adaptación del tamaño de paso")
plt.xlabel("t")
plt.ylabel("tamaño de paso")

plt.show()
