my_list = [3, 5, 9, 2, 89, 45, 65, 62, 78, 12, 59, 12, 36]
b = [el for el in my_list if el > my_list [my_list.index(el)-1]]
print (b)
