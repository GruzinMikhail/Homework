def my_del (agr_1, agr_2):
    try:
        agr_0 = agr_1 / agr_2
        return agr_0
    except ZeroDivisionError:
        return "Делить на 0 нельзя"

print (my_del(int(input("Введите первое число: ")), int(input("Введите второе число: "))))