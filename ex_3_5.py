res=0
flag = 0

while True:
    list_var = input("Введите строку чисел разделенный пробелом:").split(" ")
    el_len = len(list_var)
    i = 0
    while i<el_len:
        if list_var[i] != "q":
            res +=int(list_var[i])
            i += 1
        else:
            flag = 1
            break
    print(f"Сумма введенных чисел: {res}")
    if flag==1:
        break





