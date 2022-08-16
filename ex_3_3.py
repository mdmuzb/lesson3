
def my_func(var1, var2, var3):
    min_numb = min(var1, var2, var3)
    cort = var1, var2, var3

    for elem in cort:
        if (elem) != min_numb:
            print(elem)


#param1 = input("Введите параметр (1) :")
#param2 = input("Введите параметр (2) :")
#param3 = input("Введите параметр (3) :")

list_param = input("Введите 3 числа разделяя символом ""','"":").split(',')

my_func(list_param[0], list_param[1], list_param[2])
