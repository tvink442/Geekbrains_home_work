#Задание 1
list_other = [1, 2.5, "wow", True, {1 : "Зима"},[1, 2, 3],('time','time')]
for k in list_other:
	print(type(k))

#Задание 2

my_another_list = list(input())
for i in range(1, len(my_another_list), 2):
	my_another_list[i - 1],my_another_list[i] = my_another_list[i],my_another_list[i-1]

print(my_another_list)
#Задание 3

month = int(input("Укажите номер месяца "))
list_seasons = ["Зима","Зима","Весна","Весна","Весна","Лето","Лето","Лето","Осень","Осень","Осень","Зима"]
print(list_seasons[month - 1])
seasons = {
	1 : "Зима", 2 : "Зима", 12 : "Зима",
	3 : "Весна", 4 : "Весна", 5 : "Весна",
	6 : "Лето", 7 : "Лето", 8 : "Лето",
	9 : "Осень" , 10 : "Осень", 11 : "Осень"
	}
print(seasons[month])


#Задание 4 

words = input("Введите слова через пробел ")
words = words.split(' ')
for i in words: print(i[:10])

#Задание 5

my_list = [7, 5, 3, 3, 2]

user = int(input())
my_list.append(user)
my_list.sort(reverse=True)
print(my_list)

