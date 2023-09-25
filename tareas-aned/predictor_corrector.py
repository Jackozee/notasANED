
def predcor(coefcorra, coefcorrb, coefpreda, coefpredb,
            h, f, t0, u0, tf, pece, m):
    ordencorr = max(len(coefcorra), len(coefcorrb) - 1)
    ordenpred = max(len(coefpreda), len(coefpredb) - 1)
    ordencopr = max(ordencorr, ordenpred)
    if (len(u0) < ordencopr):
        return [], []
    t = [t0 + n * h for n in range(0, ordencopr - 1)]
