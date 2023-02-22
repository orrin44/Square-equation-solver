print("Введите коэффициенты a, b и c квадратного уравнения")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
d = b**2 - 4*a*c
if d > 0:
    x1 = (-b - d**(1/2))/(2*a)
    x2 = (-b + d**(1/2))/(2*a)
    print("x1 = %.1f" % x1)
    print("x2 = %.1f" % x2)
if d == 0:
    x = -b/(2*a)
    print("x = %.1f" % x)
if d < 0:
    print("Корней нет")