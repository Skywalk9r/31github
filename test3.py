import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

def gaussJordanMethod(a):
    n = len(a)
    m = len(a[0])
    #diagonal matrix
    for j in range(n):
        for i in range(n):
            if (i!=j):
                t = a[i][j]/a[j][j]
                for k in range(m):
                    a[i][k] -= a[j][k]*t
    for i in range(n):
        t = a[i][i]
        for j in range(m):
            a[i][j] /= t
    if (n==m-1):
        return([a[i][-1] for i in range(n)])
    else:
        printRoots(a, True)

def printRoots(a, isDiagonalized=False):
    n = len(a)
    m = len(a[0])
    if (not isDiagonalized):
        for j in range(n):
            for i in range(n):
                if (i!=j):
                    t = a[i][j]/a[j][j]
                    for k in range(m):
                        a[i][k] -= a[j][k]*t
        for i in range(n):
            t = a[i][i]
            for j in range(m):
                a[i][j] /= t
    freeRoots = [True for i in range(m-1)]
    answer = ""
    for i in range(n):
        for j in range(m-1):
            if (a[i][j])!=0:
                freeRoots[j] = False
                answer += "\nx" + str(j+1) + " = "
                if (a[i][m-1]!=0):
                    answer += ("- " if np.sign(a[i][m-1])<0 else "") + f'{abs(a[i][m-1]):g}' + " "
                for k in range(j+1, m-1):
                    if a[i][k]!=0:
                        answer += ("+ " if np.sign(a[i][k])<0 else "- ") + f'{abs(a[i][k]):g}' + "x" + str(k+1) + " "
                break
    for i in range(len(freeRoots)):
        if freeRoots[i]:
            answer += "\nx" + str(i+1) + " is free"
    return


def parabolaFitting(x_values, y_values):
    a = [\
        [len(x_values), sum(x_values), sum([x**2 for x in x_values]), sum(y_values)],\
        [sum(x_values), sum([x**2 for x in x_values]), sum([x**3 for x in x_values]), sum([x*y for x,y in zip(x_values,y_values)])],\
        [sum([x**2 for x in x_values]), sum([x**3 for x in x_values]), sum([x**4 for x in x_values]), sum([x**2*y for x,y in zip(x_values, y_values)])]]
    coefficents = gaussJordanMethod(a)
    return coefficents

def lineFitting(x_values, y_values):
    a = [\
        [len(x_values), sum(x_values), sum(y_values)],\
        [sum(x_values), sum([x**2 for x in x_values]), sum([x*y for x,y in zip(x_values,y_values)])]]
    coefficents = gaussJordanMethod(a)
    return coefficents

# def leastSquares(x_values, y_values):
# 	n = len(x_values)
# 	slope = n*sum([x*y for x,y in zip(x_values, y_values)])
# 	slope -= sum(x_values) * sum(y_values)
# 	slope /= n*sum([x**2 for x in x_values]) - sum(x_values)**2
# 	intercept = sum(y_values)/n - (slope*sum(x_values)/n)
	# return [intercept, slope]

plt.style.use('_mpl-gallery')
plt.xlabel('X')
plt.ylabel('Y')
plt.subplots_adjust(top=0.9, right=0.9, bottom=0.1, left=0.1)

# 1 task
# x = [0, 1, 2, 3, 4]
# y = [1, 1.8, 1.3, 2, 6.3]

# plt.xticks(x)
# coefficents = parabolaFitting(x, y)
# print(coefficents)
# func = lambda x: coefficents[0] + coefficents[1]*x + coefficents[2]*(x**2)

# plt.plot(
#     x, y,
#     "o", color="blue", label="Original")

# X_Y_Spline = make_interp_spline(x, [func(elem) for elem in x])
# X_ = np.linspace(x[0], x[-1], 500)
# Y_ = X_Y_Spline(X_)

# plt.plot(
#     X_, Y_,
#     marker='.', markersize=2, color="coral", label="Fitted into a parabola")


#2 task
# x = [6,7,7,8,8,8,9,9,10]
# y = [5,5,4,5,4,3,4,3,3]

# plt.xticks(x)
# coefficents = lineFitting(x,y)
# print(coefficents)
# func = lambda x: coefficents[0] + coefficents[1]*x

# plt.plot(
#     x, y,
#     marker='.', markersize=12, color="blue", label="Original")

# plt.plot(
#     x, [func(elem) for elem in x],
#     marker='.', markersize=12, color="coral", label="Fitted into a line")


# 3 task
# x = [0,1,2,3]
# y = [1.05, 2.10, 3.85, 8.30]

# plt.xticks(x)
# coefficents = lineFitting(x, [np.log(elem) for elem in y])
# coefficents[0] = np.e**coefficents[0]
# print(coefficents)
# func = lambda x: coefficents[0] * (np.e**(coefficents[1]*x))

# plt.plot(
#     x, y,
#     "o", color="blue", label="Original")

# X_Y_Spline = make_interp_spline(x, [func(elem) for elem in x])
# X_ = np.linspace(x[0], x[-1], 500)
# Y_ = X_Y_Spline(X_)

# plt.plot(
#     X_, Y_,
#     marker='.', markersize=2, color="coral", label=r"Fitted into a y=ae^(bx)")


#4 task
# x = [1,2,3,4,5]
# y = [1.8, 5.1, 8.9, 14.1, 19.8]

# plt.xticks(x)
# coefficents = lineFitting(x, [y_value/x_value for x_value,y_value in zip(x,y)])
# print(coefficents)
# func = lambda x: coefficents[0]*x + coefficents[1]*(x**2)

# plt.plot(
#     x, y,
#     "o", color="blue", label="Original")

# X_Y_Spline = make_interp_spline(x, [func(elem) for elem in x])
# X_ = np.linspace(x[0], x[-1], 500)
# Y_ = X_Y_Spline(X_)

# plt.plot(
#     X_, Y_,
#     marker='.', markersize=2, color="coral", label=r"Fitted into y=ax+bx^2 with a least squares method")

#5 task
x = [1,2,3,4,5,6,7,8]
y = [5.4, 6.3, 8.2, 10.3, 12.6, 14.9, 17.3, 19.5]

plt.xticks(x)
coefficents = lineFitting([x_value**2 for x_value in x], [x_value*y_value for x_value,y_value in zip(x,y)])
print(coefficents)
func = lambda x: coefficents[1]*x + coefficents[0]/x

plt.plot(
    x, y,
    "o", color="blue", label="Original")

X_Y_Spline = make_interp_spline(x, [func(elem) for elem in x])
X_ = np.linspace(x[0], x[-1], 500)
Y_ = X_Y_Spline(X_)

plt.plot(
    X_, Y_,
    marker='.', markersize=2, color="coral", label=r"Fitted into y=ax+b/x")

plt.legend(fontsize=12, loc='best', fancybox=True, shadow=True)

plt.show()