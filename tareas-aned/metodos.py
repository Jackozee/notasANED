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


# Método de Runge-Kutta-Fehlberg 4,5 ##


def dot(a, b):
    return sum([a[i] * b[i] for i in range(0, len(a))])


# Consideremos el problema de valor inicial
#
#           y'(t) = f(t,y(t))           ti < t < tf
#           y(t_0) = y_0 = condinicial
#
# El método Runge-Kutta-Fehlberg de orden 4 usa dos
# métodos de s=6 pasos, uno de orden 4 con coeficientes c, A, b
# y otro de orden 5 con coeficientes c, A, \hat b.
# Se puede representar con el tablero de Butcher modificado
#
#                   c | A
#                   -------
#                     | b^T
#                     | \hat b^T
#                   -------
#                     | E^T
#
# En este caso, la matríz A es estrictamente triangular
# inferior, así que el método es explicito.


def RKF45(A, b, bhat,
          f, tinicial, tfinal, condinicial,
          hinicial, hmin, tolerancia):
    # el número de pasos del método es
    s = len(A)

    # Los coeficientes c son

    c = [sum(A[i]) for i in range(0, s)]
    E = [b[i] - bhat[i] for i in range(0, len(b))]

    # Se comienza tomando u_0 = y_0

    ts = [tinicial]
    us = [condinicial]
    K = [0 for i in range(0, s)]

    # y luego se hacen estimaciones sucesivas
    # hasta alcanzar el tiempo final tf
    while (ts[-1] < tfinal):
        while True:

            # el tamaño de paso se inicializa como

            h = hinicial

            # luego calculamos el vector de los K_i en este punto del tiempo:

            tactual = ts[-1]
            uactual = us[-1]
            for i in range(0, s):
                acum = dot(A[i], K)
                K[i] = f(tactual + c[i] * h, uactual + h * acum)

            # El vector E = b - \hat b  se usa para estimar
            # el error de truncamiento local como

            errorEstimado = dot(E, K)

            # si el error es menor que la tolerancia
            # o si alcanzamos hmin, guardamos los valores actuales y
            # continuamos al siguiente paso

            if (errorEstimado < tolerancia or h < hmin):
                ts.append(tactual + h)
                us.append(dot(b, K))
                break
            else:
                h = h / 2
    return ts, us
