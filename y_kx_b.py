print("Введите первую точку")

x1 = float(input('X: '))

y1 = float(input('Y: '))

print("\nВведите вторую точку")

x2 = float(input('X: '))

y2 = float(input('Y: '))

x_diff = abs(x1 - x2)

y_diff = abs(y1 - y2)

if x1 == x2:
    result = 'x = ' + str(x1)
elif y1 == y2:
    result = "y = " + str(y1)
else:
    k = y_diff / x_diff
    b = y2 - k * x2
    result = "y = " + str(k) + " * x + " + str(b)

print("\nУравнение прямой, проходящей через эти точки:")

print(result)