#Задание 1
number = input("Введите любое число ")
print("Вы ввели :" + number)
string = input("Введите текст ")
print("Вы ввели :" + string)

#Задание 2
time = int(input("Введите количество секунд "))
second = time % 60
hour = time // 3600
minute = time // 60 - hour * 60 
print(f'{hour}:{minute}:{second}')

#Задание 3
n = input("Введите число ")
print(int(n) + int(n + n) + int(n + n + n))

#Задание 4 
user_number =int(input("Введите любое число "))

max_in_number = 0
num = user_number
while  num > 0:
	temp = num % 10
	if temp > max_in_number:
		max_in_number = temp
	num = num // 10 

print("Самая большая цифра в числе: ", max_in_number)

#Задание 5

proceeds = int(input("Укажите колличество выручки: "))
cost = int(input("Укажите колличество издержек фирмы: "))

result = proceeds - cost

if result > 0:
	print("Фирмa работает в прибыль ", result)
	print("Рентабильность " ,proceeds/cost)
	workers = int(input("Укажите колличество сотрудников: "))
	print("Зп ", result/workers)
elif result < 0:
	print("Фирмa работает в убыток")
else:
	print("Фирма работает в 0")


#Задание 6 
a = float(input("Укажите результат первого дня: "))
b = float(input("Укажите цель: "))
temp = a
days = 1

while True:
	if temp >= b :
		print(f"Цель достигныта на {days}-й день.")
		break
	temp = temp + temp * 0.1
	days +=1
