import matplotlib.pyplot as plt
import metodos as jaac

# Considermos el problema de valores iniciales
#
# (y'(t),z'(t)) = (f1(t,y,z),f2(t,y,z))
# (y(0),z(0)) = (y0,z0)
#
# en A < t < B, donde
A = 0
B = 8
H = 0.1


def f1(t, y, z):
    return z


def f2(t, y, z):
    return -(y**2 - 1) * z - y


# Una solución aproximada se obtiene con el método de Euler
# con tamaño de paso h < (b-a).

plt.subplot(211, title="Euler")
ts, ys, zs = jaac.euler2var(f1, f2, y0=0, z0=1, a=A, b=B, h=H)
plt.plot(ys, zs, 'b')
plt.plot(0, 1, 'bo')
ts, ys, zs = jaac.euler2var(f1, f2, y0=-2, z0=3, a=A, b=B, h=H)
plt.plot(ys, zs, 'r')
plt.plot(-2, 3, 'ro')
plt.ylabel("y'")

# Otra aproximación se obtiene con el método de Heun
# con el mismo tamaño de paso h.

plt.subplot(212, title="Heun")
ts, ys, zs = jaac.heun2var(f1, f2, y0=0, z0=1, a=A, b=B, h=H)
plt.plot(ys, zs, 'b')
plt.plot(0, 1, 'bo')
ts, ys, zs = jaac.heun2var(f1, f2, y0=-2, z0=3, a=A, b=B, h=H)
plt.plot(ys, zs, 'r')
plt.plot(-2, 3, 'ro')

# Graficamos ambas aproximaciones:

plt.xlabel("y")
plt.ylabel("y'")
plt.show()
