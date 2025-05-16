import math

def F(x):
    return  math.pow(x, 3) - 1 

def F1(x):
    res= 3 * math.pow(x, 2)
    return res

def Method(a, b):
    try:
        x0 = (a + b) / 2
        xn = F(x0)
        xn1 = xn - F(xn) / F1(xn)
        while abs(xn1 - xn) > math.pow(10, -5):
            xn = xn1  
            xn1 = xn - F(xn) / F1(xn)
        print("Корень: ", xn1)
        return xn1
    except ValueError:
        print("Value not invalidate")

if __name__ == '__main__':
    x=float(input("Начальное приближение:"))
    a=float(input("Начало отрезка: "))
    b=float(input("Конец отрезка: "))
    F(x)
    F1(x)
    Method(a, b)
