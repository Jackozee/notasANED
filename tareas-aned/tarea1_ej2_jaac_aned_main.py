import matplotlib.pyplot as plt
import numpy as np
import metodos as jaac

# Considermos el problema de valores iniciales
#
# y'(t) = f(t,y)
# y(0) = y0
#
# en A < t < B, donde
A = 0
B = 2


def f(t, y):
    return y * t**3 - 1.5 * y

# que tiene solución exacta


def sol(t):
    return np.exp(t**4 / 4 - 3 * t / 2)


# Una solución aproximada se obtiene con el método de Euler
# con tamaño de paso h < (b-a).

ts, ys = jaac.euler(f, y0=1, a=A, b=B, h=0.2)

plt.subplot(211, title="Soluciones aproximadas")
plt.plot(ts, ys, 'bo', label="Euler")
plt.subplot(212, title="Error puntual")
plt.plot(ts, abs(ys - sol(ts)), 'bo', label="Euler")

# Otra aproximación se obtiene con el método de Heun
# con el mismo tamaño de paso h.

ts, ys = jaac.heun(f, y0=1, a=A, b=B, h=0.2)
#
plt.subplot(211, title="Soluciones aproximadas")
plt.plot(ts, ys, 'ro', label="Heun")
plt.subplot(212, title="Error puntual")
plt.plot(ts, abs(ys - sol(ts)), 'ro', label="Heun")

# Graficamos la solución exacta y ambas aproximaciones:

plt.subplot(211, title="Soluciones aproximadas")
plt.plot(np.arange(A, B, 0.01), sol(np.arange(A, B, 0.01)),
         label="Sol. Exacta")
plt.xlabel("t")
plt.ylabel("y")
plt.legend()

plt.subplot(212, title="Error puntual")
plt.xlabel("t")
plt.ylabel("error")
plt.legend()

plt.show()
