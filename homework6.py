from itertools import count, cycle
from time import sleep


# Задание 1

class TrafficLight():
    def __init__(self):
        self.__color = ['red', 'yellow', 'green']
        self.running()

    def running(self):
        for i in cycle(self.__color):
            print(i)
            if i == 'red':
                sleep(7)
            elif i == 'yellow':
                sleep(2)
            elif i == 'green':
                sleep(20)


obg1 = TrafficLight()


# Задание 2

class Road:
    def __init__(self, length, width):
        self._length = int(length)
        self._width = int(width)
        self._result()

    def _result(self):
        print(self._length * self._width * 25 * 5 // 1000, 't')


obg2 = Road(20, 5000)

# Задание 3


class Worker:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': int(input()), 'bonus': int(input())}


class Position(Worker):
    def get_full_name(self):
        print(f'name: {self.name}\nsurname {self.surname}')

    def get_total_income(self):
        print(f'income: {sum(self._income.values())}')


obj3 = Position('Jenya', 'Moskalenko', '...')
obj3.get_total_income()
obj3.get_full_name()

 # Задание 4
class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.show_speed()

    def go(self):
        print('go')

    def stop(self):
        print('stop')

    def turn(self, direction):
        print(f'tern {direction}')

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("Превышение скорости")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("Превышение скорости")


class PoliceCar(Car):
    pass


obj5 = WorkCar(80, 'red', 'mazda')
obj5.go()
obj5.turn('left')
obj5.stop()

# Задание 5

class Stationery:
    def __init__(self, title=None):
        self.title = title
        self.draw()

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        super().draw()
        print('Pen')


class Pencil(Stationery):
    def draw(self):
        super().draw()
        print('Pencil')


class Handle(Stationery):
    def draw(self):
        super().draw()
        print('Handle')


obj5 = Handle()
