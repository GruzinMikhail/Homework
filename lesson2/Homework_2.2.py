count = int(input("Введите кол-во элементов списка "))
list = []
a = 0
b = 0
while a < count:
    list.append(input("Введите следующее значение списка "))
    a += 1

for elem in range(int(len(list)/2)):
        list[b], list[b + 1] = list [b + 1], list[b]
        b += 2
print(list)