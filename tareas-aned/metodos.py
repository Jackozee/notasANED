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
    N = round(T / h)

    # el tamaño del intervalo y el número de pasos posibles,
    # respectivamente. Los puntos del tiempo son t[n]=a+nh,
    # desde n=0 hasta n=N, es decir, habrá N+1 puntos en el tiempo:

    ts = np.linspace(a, b, N + 1)

    # La solución deseada

    us = np.zeros(N + 1)

    # se construye poniendo la condición inicial

    us[0] = y0

    # y luego usando la solución en tiempos posteriores
    # para construir la siguiente:

    for n in range(0, N):
        us[n + 1] = us[n] + h * f(ts[n], us[n])
    return ts, us


def heun(f, y0, a, b, h):
    # Sean

    T = b - a
    N = round(T / h)

    # el tamaño del intervalo y el número de pasos posibles,
    # respectivamente. Los puntos del tiempo son t[n]=a+nh,
    # desde n=0 hasta n=N, es decir, habrá N+1 puntos en el tiempo:

    ts = np.linspace(a, b, N + 1)

    # La solución deseada

    us = np.zeros(N + 1)

    # se construye poniendo la condición inicial

    us[0] = y0

    # y luego usando la solución en tiempos posteriores
    # para construir la siguiente:

    for n in range(0, N):
        us[n + 1] \
            = us[n] \
            + h * \
            (
            f(ts[n], us[n]) +
            f(ts[n + 1], us[n] + h * f(ts[n], us[n]))
        ) / 2
    return ts, us


def euler2var(f1, f2, y0, z0, a, b, h):
    # Sean

    T = b - a
    N = round(T / h)

    # el tamaño del intervalo y el número de pasos posibles,
    # respectivamente. Los puntos del tiempo son t[n]=a+nh,
    # desde n=0 hasta n=N, es decir, habrá N+1 puntos en el tiempo:

    ts = np.linspace(a, b, N + 1)

    # La solución deseada

    us = np.zeros(N + 1)
    vs = np.zeros(N + 1)

    # se construye poniendo la condición inicial

    us[0] = y0
    vs[0] = z0

    # y luego usando la solución en tiempos posteriores
    # para construir la siguiente:

    for n in range(0, N):
        us[n + 1] = us[n] + h * f1(ts[n], us[n], vs[n])
        vs[n + 1] = vs[n] + h * f2(ts[n], us[n], vs[n])
    return ts, us, vs


def heun2var(f1, f2, y0, z0, a, b, h):
    # Sean

    T = b - a
    N = round(T / h)

    # el tamaño del intervalo y el número de pasos posibles,
    # respectivamente. Los puntos del tiempo son t[n]=a+nh,
    # desde n=0 hasta n=N, es decir, habrá N+1 puntos en el tiempo:

    ts = np.linspace(a, b, N + 1)

    # La solución deseada

    us = np.zeros(N + 1)
    vs = np.zeros(N + 1)

    # se construye poniendo la condición inicial

    us[0] = y0
    vs[0] = z0

    # y luego usando la solución en tiempos posteriores
    # para construir la siguiente:

    for n in range(0, N):
        us[n + 1] \
            = us[n] \
            + h * \
            (
            f1(ts[n], us[n], vs[n]) +
            f1
            (
                ts[n + 1],
                us[n] + h * f1(ts[n], us[n], vs[n]),
                vs[n] + h * f2(ts[n], us[n], vs[n]),
            )
        ) / 2
        vs[n + 1] \
            = vs[n] \
            + h * \
            (
            f2(ts[n], us[n], vs[n]) +
            f2
            (
                ts[n + 1],
                us[n] + h * f1(ts[n], us[n], vs[n]),
                vs[n] + h * f2(ts[n], us[n], vs[n]),
            )
        ) / 2
    return ts, us, vs
