def my_func(arg_1, arg_2):
    r = arg_1 / arg_2
    return r

try:
    delimoe = int(input("Введите делимое число:"))
    delitel = int(input("Введите делитель:"))
    resultat = my_func(delimoe, delitel)
    print(resultat)
except ZeroDivisionError:
    print("Деление на ноль")
#else:
#    resultat = my_func(delimoe, delitel)
#    print(resultat)
