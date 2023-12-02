import matplotlib.pyplot as plt
import numpy as np


def bisectionMethod(f, a, b, errorTolerance, iterations=10):
    if (f(a) * f(b) >= 0):
        print("wrong input")
        return
    x0 = (a + b) / 2
    roots = [x0]
    while (len(roots) < iterations and (f(a) * f(b)) < 0 and (f(x0) != 0) and (np.abs(f(x0)) > errorTolerance)):
        if (np.sign(f(x0)) == np.sign(f(a))):
            a = x0
        else:
            b = x0
        x0 = (a + b) / 2
        roots.append(x0)
    return roots


def secantMethod(f, x0, x1, errorTolerance, iterations=10):
    if (x0 >= x1 or f(x0) * f(x1) >= 0):
        print("wrong input")
        return
    roots = []
    while (len(roots) < iterations):
        x2 = x1 - (f(x1) * (x1 - x0) / (f(x1) - f(x0)))
        roots.append(x2)
        if (x2 != 0 and np.abs((x2 - x1) / x2) > errorTolerance):
            x0 = x1
            x1 = x2
        else:
            return roots


def iterationMethod(f, g, a, b, errorTolerance, iterations=10):
    if (a >= b or f(a) * f(b) >= 0):
        print("wrong input")
        return
    x = (a + b) / 2
    roots = [x]
    while (len(roots) < iterations and np.abs(g(x) - x) > errorTolerance):
        roots.append(x)
        x = g(x)
    return roots


def newtonRaphsonMethod(f, a, b, errorTolerance, iterations=10):
    if (a >= b and f(a) * f(b) >= 0):
        print("wrong input")
        return
    h = 1e-10
    x = (a + b) / 2
    roots = [x]
    while (len(roots) < iterations and f(x) != 0 and np.abs(x) > errorTolerance):
        x = x - (f(x) / ((f(x + h) - f(x - h)) / (2 * h)))
        roots.append(x)
    return roots


def falsePositionMethod(f, x0, x1, errorTolerance, iterations=10):
    if (f(x0) * f(x1) > 0):
        print("wrong input")
        return
    x = x0 - ((x1 - x0) / (f(x1) - f(x0))) * f(x0)
    roots = []
    while (len(roots) < iterations and np.abs(f(x0)) > errorTolerance):
        if (np.sign(f(x)) == np.sign(f(x0))):
            x0 = x
        else:
            x1 = x
        x = x0 - ((x1 - x0) / (f(x1) - f(x0))) * f(x0)
        roots.append(x)
    return roots


plt.style.use('_mpl-gallery')

plt.xlabel('Iterations')
plt.ylabel('Roots')
plt.subplots_adjust(top=0.9, right=0.9, bottom=0.1, left=0.1)

plt.plot(
    bisectionMethod(lambda x: x ** 3 - x - 1, 1, 2, 0.001),
    marker='.', markersize=12, color="red", label=r"x^3 - x - 1 = 0")

plt.plot(
    bisectionMethod(lambda x: x - np.cos(x), -2, 2, 0.001),
    marker='.', markersize=12, color="blue", label=r"x - cos(x) = 0")

plt.plot(
    bisectionMethod(lambda x: np.e ** (-x) - x, -2, 1, 0.001),
    marker='.', markersize=12, color="green", label=r"e^(-x) - x = 0")

plt.title(r"2x - log(x) = 7")

plt.legend(fontsize=12)

plt.show()
