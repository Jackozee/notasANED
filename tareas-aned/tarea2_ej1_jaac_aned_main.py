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
B = 1


def f(t, y):
    return y

# que tiene solución exacta


def sol(t):
    return np.exp(t)


# Una solución aproximada se obtiene con el método de Euler.
# Usando la aproximación del error
#
# y_n - u_n = h t_n exp(t_n) / 2 + O(h²)
#
# estimamos que, para que el error en y(1) sea menor que 10⁻⁵,
# debemos tomar un tamaño de paso menor a
#
# 2/(10⁵e) aprox 7.3576*10⁻⁶
#
# Aplicamos el método y graficamos el error:
#

ts, ys = jaac.euler(f, y0=1, a=A, b=B, h=7.3576e-6)
plt.plot(ts, abs(ys - sol(ts)), 'b', label="Euler")

plt.title("Error puntual")
plt.xlabel("t")
plt.ylabel("error")
plt.ylim([0, 1e-5])
plt.legend()

plt.show()
