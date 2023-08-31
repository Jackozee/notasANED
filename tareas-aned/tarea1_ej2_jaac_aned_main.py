import matplotlib.pyplot as plt
import numpy as np
import metodos as ja

# Considermos el problema de valores iniciales
#
# y'(t) = f(t,y)
# y(0) = y0
#
# en a < t < b, donde


def f(t, y):
    return y * t**3 - 1.5 * y

# Una solución aproximada se obtiene con el método de Euler
# con tamaño de paso h < (b-a).


ts, ys = ja.euler(f, y0=1, a=0, b=2, h=0.2)

# La solución exacta es


def sol(t):
    return np.exp(t**4 / 4 - 3 * t / 2)

# Graficamos ambas soluciones:


plt.plot(ts, sol(ts))
plt.plot(ts, ys, 'bo')
plt.show()
