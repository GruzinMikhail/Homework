def fibo_gen(number):
    count = 1
    while count <= number:
        yield count
        count += 1
i = 1
fibo_gen_2 = []
for el in fibo_gen(5):
    if i > 15:
        break
    else:
        fibo_gen_2.append(el)
        i += 1
print(fibo_gen_2)