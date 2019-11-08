def my_func(arg_1, arg_2, arg_3):
    sequence = [arg_1, arg_2, arg_3]
    total = []
    max_1 = max(sequence)
    total.append(max_1)
    sequence.remove(max_1)
    max_2 = max(sequence)
    total.append(max_2)
    print(sum(total))
my_func(15, 8, 6)