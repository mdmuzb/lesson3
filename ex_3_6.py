def int_func(*txt):
   # i = 0
   #print(type(txt))
   for item in txt:
       for item_lst in item:
       #   print(type(item_lst))
           print(item_lst.capitalize())


my_str = input("введите текст:").split(" ")
#my_str = input("введите текст:")
int_func(my_str)
