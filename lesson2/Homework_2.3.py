list_seasons = ['зима', 'весна', 'лето', 'осень']
dict_seasons = {1 : 'зима', 2 : 'весна', 3 : 'лето', 4 : 'осень'}
month = int(input("Введите номер месяца "))
if month ==1 or month == 12 or month == 2:
        print(dict_seasons.get(1))
        print(list_seasons[0])
elif month == 3 or month == 4 or month ==5:
    print(dict_seasons.get(2))
    print(list_seasons[1])
elif month == 6 or month == 7 or month == 8:
    print(dict_seasons.get(3))
    print(list_seasons[2])

elif month == 9 or month == 10 or month == 11:
    print(dict_seasons.get(4))
    print(list_seasons[3])
else:
        print("Такого месяца не существует")