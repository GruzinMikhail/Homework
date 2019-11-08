seconds = int(input("Введите целое число - "))
second = seconds % 60
minutes = seconds % 3600 // 60
hours = seconds // 3660
print('%d:%d:%d' % (hours, minutes, second))

