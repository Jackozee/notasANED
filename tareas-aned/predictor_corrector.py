import numpy as np


def predcor(coefcorra, coefcorrb, coefpreda, coefpredb,
            h, f, t0, tf, condini, iteracionescorr):
    T = tf - t0
    N = round(T / h)
    pasoscorr = max(len(coefcorra), len(coefcorrb) - 1)
    pasospred = max(len(coefpreda), len(coefpredb) - 1)
    pasoscorpr = max(pasoscorr, pasospred)
    if (len(condini) < pasoscorpr):
        return [], []
    us = condini[0:pasoscorpr]
    # y = condini[0:pasoscorpr]
    ts = [t0 + n * h for n in range(0, N + 1)]
    fs = [f(ts[i], us[i]) for i in range(0, pasoscorpr)]
    print(fs)

    # k = pasoscorpr
    # for t in ts[pasoscorpr:(N + 1)]:
    # ut = np.dot(coefpreda, u[k:k - pasospred + 1:-1])
    return us


def f(t, y):
    return y


atilde = [1]                # coeficientes predictor
btilde = [1 / 2, 1 / 2]     #
a = [1]                     # coeficientes corrector
b = [1]                     #
h = 0.1
t0 = 0
tf = 1
condini = [1, np.exp(1 + h)]
m = 1
us = predcor(a, b, atilde, btilde, h, f, t0, tf, condini, m)

print(us)
