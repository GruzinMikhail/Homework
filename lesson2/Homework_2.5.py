my_list = [7, 5, 3, 3, 2]
print(f"Рейтинг - {my_list}")
numbers = int(input("Введите любое число "))
while True:
    for el in range(len(my_list)):
        if my_list[el] == numbers:
            my_list.insert(el + 1, numbers)
            break
        elif my_list[0] < numbers:
            my_list.insert(0, numbers)
        elif my_list[-1] > numbers:
            my_list.append(numbers)
        elif my_list[el] > numbers and my_list[el + 1] < numbers:
            my_list.insert(el + 1, numbers)
    print(f"текущий список - {my_list}")
    numbers = int(input("Введите число "))