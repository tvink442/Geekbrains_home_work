from functools import reduce
from itertools import count, cycle
from math import factorial


def multiplication(a, b):
    return a * b


# Задание 1

from sys import argv

script_name, hour, money, premium = argv
argv = [int(temp) for temp in argv[1:]]
print((argv[0] * argv[1]) + argv[2])
"""получилось как-то коряво, но ничего лучше не придумал"""

# Задание 2
my_lst = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_my_lst = [temp for i, temp in enumerate(my_lst) if my_lst[i] > my_lst[i - 1] and i != 0]
print(new_my_lst)

# Задание 3

my_list2 = [temp for temp in range(20, 240) if temp % 20 == 0 or temp % 21 == 0]
print(my_list2)


# Задание 4

my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_my_list = [temp for temp in my_list if my_list.count(temp) == 1]
print(new_my_list)

# Задание 5
my_list1 = [temp for temp in range(100, 1001) if temp % 2 == 0]
print(my_list1)
result = reduce(multiplication, my_list1)
print(result)

# Задание 6
# a
for temp in count(int(input())):
    print(temp)
# b
my_list3 = [1, 2, 3]
other = cycle(my_list3)
stop = ''
while stop != 'q':
    print(next(other))
    stop = input()

# Задание 7
def my_fanc():
    for n in count(1):
        yield factorial(n)


out = 1
for i in my_fanc():
    print(f'factorial {out}! = {i}')
    if out == 10:
        break
    out += 1
