# Задание 1
class Matrix:

    def __init__(self, lst):
        self.lst = lst

    def __str__(self):
        return '\n' + '\n'.join([' '.join([str(j) for j in i]) for i in self.lst])

    def __add__(self, other):
        temp = []
        for i in range(max(len(self.lst), len(other.lst))):
            temp.append(list(map(sum, zip(self.lst[i], other.lst[i]))))
        return Matrix(temp)


lst1 = Matrix([[21, 34, 21, 54], [1, 2, 3, 4], [6, 5, 4, 3]])
lst2 = Matrix([[1, 4, 2, 5], [51, 22, 13, 64], [1, 2, 3, 3]])
print(lst1)
print(lst2)
obj3 = lst1 + lst2
print(obj3)

# Задание 2

from abc import ABC, abstractmethod


class Clothes(ABC):  # Одежда
    def __init__(self, arg):
        self.arg = arg

    @abstractmethod
    def result(self):
        pass


class Costume(Clothes):  # Костюм
    @property
    def result(self):
        return (2 * self.arg) + 0.3


class Coat(Clothes):  # Пальто
    @property
    def result(self):
        return round((self.arg / 6.5) + 0.5, 2)


coat = Coat(20)
cost = Costume(20)
print(coat.result)
print(coat.result)


# Задание 3

class Cells:
    def __init__(self, arg):
        self.arg = arg

    def mace_order(self, num):
        return '\n'.join(['*' * num for _ in range(self.arg // num)]) + '\n' + '*' * (self.arg % num)

    def __add__(self, other):
        return self.arg + other.arg

    def __sub__(self, other):
        return self.arg - other.arg if self.arg - other.arg > 0 else 'error'

    def __mul__(self, other):
        return self.arg * other.arg

    def __truediv__(self, other):
        return self.arg / other.arg


cell = Cells(12)
cell2 = Cells(5)
print(cell + cell2)
print(cell - cell2)
print(cell * cell2)
print(cell / cell2)
print(cell.mace_order(5))
