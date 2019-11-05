def summa(a):
    a = a.split()
    b = []
    for i in a:
        b.append(int(i))
    return sum(b)

s = 0
while 1:
    a = input("Введите числа через пробел, для выхода из программы введите q: ")
    if a == 'q': break
    s += summa(a)
    print('Summa:', s)