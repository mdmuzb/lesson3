def my_func(x, y):
    result = 1
    result2 = 1
    x = int(x)
    y = int(y)
    result = x**y
    print(f"{result}")
    y2 = y * (-1)

    for i in range(y2):
        result2 *= x
    print(1/result2)


x = input("Введите положительное число:")
y = input("Введите отрицательно число:")

my_func(x, y)