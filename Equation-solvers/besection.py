import math
import numpy as np
def f(x):
    return math.sin(x) - x

def dyhotomy(a, b, eps):
    root = None
    while abs(f(b) - f(a)) > eps:
        mid = (a + b) / 2
        if f(mid) == 0 or abs(f(mid)) < eps:
            root = mid
            break
        elif f(a)*f(mid) < 0:
            b = mid
        else:
            a = mid

    if root is None:
        print('Корень не найден')
    else:
        print("Корень по методу дихотомии находится в точке x = ", root)
a   = input("Начало отрезка в котором ищется корень: ")
a   = float(a)
b   = input("Конец отрезка в котором ищется корень: ")
b   = float(b)
eps = input("Точность поиска корня: ")
eps = float(eps)
dyhotomy(a, b, eps)





