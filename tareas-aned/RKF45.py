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
          hmax, tolerancia, orden):
    # el número de pasos del método es
    s = len(A)

    # Los coeficientes c son

    c = [sum(A[i]) for i in range(0, s)]
    E = [b[i] - bhat[i] for i in range(0, len(b))]

    # Se comienza tomando u_0 = y_0

    ts = [tinicial]
    us = [condinicial]
    hs = []
    hsrechazados = []
    K = [0 for i in range(0, s)]
    h = (tfinal - tinicial) / 20

    # y luego se hacen estimaciones sucesivas
    # hasta alcanzar el tiempo final tf
    while (ts[-1] + h < tfinal):
        while True:
            # el tamaño de paso se inicializa como

            # luego calculamos el vector de los K_i en este punto del tiempo:

            tactual = ts[-1]
            uactual = us[-1]
            for i in range(0, s):
                acum = dot(A[i], K)
                K[i] = f(tactual + c[i] * h, uactual + h * acum)

            # El vector E = b - \hat b  se usa para estimar
            # el error como
            #
            #   errorEstimado   = |u_{n+1} - \hat u_{n+1}|
            #                   = |u_n + h*b·K - u_n - h*\hat b·K|
            #                   = h|b·K - \hat b·K|
            #                   = h|E·K|

            errorEstimado = h * abs(dot(E, K))

            # si el error es menor que la tolerancia,
            # guardamos los valores actuales y
            # continuamos al siguiente paso

            if (errorEstimado <= tolerancia):
                ts.append(tactual + h)
                us.append(uactual + h * dot(b, K))
                hs.append([tactual, h])
                # print("t=", tactual, "h=", h, "yes")
                h = min([hmax, h * (tolerancia / errorEstimado)**(1 / orden)])
                break
            else:
                hsrechazados.append([tactual, h])
                # print("t=", tactual, "h=", h, "no")
                h = min([hmax, h * (tolerancia / errorEstimado)**(1 / orden)])
    return ts, us, hs, hsrechazados
