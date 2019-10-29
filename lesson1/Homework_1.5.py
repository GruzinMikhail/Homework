inc = int(input("Введите выручку: "))
cos = int(input("Введите издержки: "))


if inc > cos:
    ren = ((inc - cos) / inc) * 100
    print (f"Фирма работает в приибыль: {ren}")
    while True:
        sot = int(input("Введите число сотрудников: "))
        vrod = ren / sot
        print(f"Выручка на одного работника: {vrod}")
        break
else:
    print("Фирма работает в убыток")


