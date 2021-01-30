'''from itertools import count

for el in count(int(input('Введите стартовое число '))):
    if el == 10:
        break
    print(el) # цикл!'''
from itertools import cycle

my_list = [True, 'ABC', 123, None]
for el in cycle(my_list):
    if el == None:
        break
    print(el)  # беконечный цикл!
