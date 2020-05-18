# Задание 1
def act(a, b):
    if b != 0:
        result = a / b
        return result
    else:
        return ("Ошибка, Делить на ноль нельзя")


print(act(int(input("Укажите первное число ")), int(input("Укажите второе число "))))


# Задание 2

def user(name, surname, year_of_birth, city, email, number_phone):
    print(f'{name}, {surname}, {year_of_birth}, {city}, {email}, {number_phone}')


user(name=input(), surname=input(), year_of_birth=input(), city=input(), email=input(), number_phone=input())


# Задание 3


def my_func(a, b, c):
    return max(a + b, a + c, b + c)


print(my_func(10, 20, 30))


# Заание 4

def my_other_func(x, y):
    result_x = x ** y
    result_y = y
    i = 1
    while True:
        if i < x:
            result_y *= y
            i += 1
            continue
        return (result_x, result_y)


print(my_other_func(8, 8))

# Задание 5

result = 0
while True:
    my_list = input("Введите числа через пробел. Для выхода нажмите * ").split()
    if my_list[-1] == "*":
        my_list.pop()
        my_list = [int(temp) for temp in my_list]  # или так list(map(int, my_list))
        result += sum(my_list)
        break
    else:
        my_list = [int(temp) for temp in my_list]
        result += sum(my_list)
        print(result)

print(result)

# Задание 6


def int_func(a):
    print(a.title())


int_func("задание")
int_func("надеюсь я правильно понял задание")
