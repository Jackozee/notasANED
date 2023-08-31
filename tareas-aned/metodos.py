import numpy as np

# Considermos el problema de valores iniciales
#
# y'(t) = f(t,y)
# y(0) = y0
#
# en a < t < b. También tomaremos un tamaño de paso h < (b-a).
#
# Construimos una aproximación u de la solución como sigue


def euler(f, y0, a, b, h):
    # Sean

    T = b - a
    n = round(T / h)

    # el tamaño del intervalo y el número de pasos posibles,
    # respectivamente. Los puntos del tiempo son t[n]=a+ih,
    # desde i=0 hasta i=n, es decir, habrá n+1 puntos en el tiempo:

    ts = np.linspace(a, b, n + 1)

    # La solución deseada

    us = np.zeros(n + 1)

    # se construye poniendo la condición inicial

    us[0] = y0

    # y luego usando la solución en tiempos posteriores
    # para construir la siguiente:

    for i in range(1, n + 1):
        us[i] = us[i - 1] + h * f(ts[i], us[i - 1])
    return ts, us
