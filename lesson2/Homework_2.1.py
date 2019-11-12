int = 8
float = 8.8
str = "My name is Mikhail"
set = { 9,4,7,3,6,1}
list = ['m', '8']
tuple = ('a', '4')
dict = {'game': 'Destiny', 'developers': 'Bunge' }

my_list = [int, float, str, set, list, tuple, dict]
for i in my_list:
    print(f'{i} is {type(i)}')
