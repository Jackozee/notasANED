import numpy as np


def dot(xs, ys):
    return (
        sum([xs[i] * ys[i] for i in range(0, min(len(xs), len(ys)))])
    )


def predcor(coefpreda, coefpredb, coefcorra, coefcorrb,
            h, f, t0, tf, condini, iteracionescorr):
    T = tf - t0
    N = round(T / h)
    pasospred = max(len(coefpreda) - 1, len(coefpredb) - 1)
    pasoscorr = max(len(coefcorra) - 1, len(coefcorrb) - 2)
    pasos = max(pasoscorr, pasospred)
    if (len(condini) <= pasos):
        return [], []
    ts = [t0 + n * h for n in range(0, N + 1)]
    us = np.zeros(N + 1)
    us[0:(pasos + 1)] = condini[0:(pasos + 1)]
    fs = np.zeros(N + 1)
    for i in range(0, pasos + 1):
        fs[i] = f(ts[i], us[i])
    for n in range(pasos, N):
        us[n + 1] = (
            dot(coefpreda, us[n::-1])
            +
            h *
            dot(coefpredb, fs[n::-1])
        )
        for k in range(0, iteracionescorr):
            fs[n + 1] = f(ts[n + 1], us[n + 1])  # f_{n+1}^{(k)}
            us[n + 1] = (                        # u_{n+1}^{(k+1)}
                dot(coefcorra, us[n::-1])
                + h *
                coefcorrb[0] * fs[n + 1]
                + h *
                dot(coefcorrb[1:], fs[n::-1])
            )
    return ts, us
