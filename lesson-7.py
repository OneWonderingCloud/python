__author__ = "Nikolay Donetskiy"


# task 1
class Matrix:
    def __init__(self, mat=[]):
        self.__matrix = mat
        self.__rowcount = len(mat)
        self.__colcount = len(mat[0])
        for i in self.__matrix:
            if len(i) != self.__colcount:
                raise Exception("This is not a matrix")

    @property
    def colcount(self):
        return self.__colcount

    @property
    def rowcount(self):
        return self.__rowcount

    def __str__(self):
        str_out = ""
        for i in self.__matrix:
            cur_str = []
            for j in i:
                cur_str.append(str(j))
            str_out += " ".join(cur_str) + "\n"
        return str_out

    def __getitem__(self, item):
        return self.__matrix[item]

    def __add__(self, other):
        if (self.colcount == other.colcount) and (self.rowcount == other.rowcount):
            res = self
            for i in range(0, self.rowcount):
                for j in range(0, self.colcount):
                    res[i][j] += int(other[i][j])
            return res
        else:
            raise Exception("Matrices dimensions do not match")


a = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a)
b = Matrix([[10, 20], [40, 50], [70, 80], [110, 120]])
c = Matrix([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
d = a + c
print(d)

# task 2
from abc import ABC, abstractmethod


class Clothing(ABC):

    def __init__(self, name):
        self.__name = name

    @property
    @abstractmethod
    def getname(self):
        pass


class Coat(Clothing):
    """ Создает экземпляр класса Coat.
                name - наименование модели пальто
                V - размер пальто
    """

    def __init__(self, name, v):
        super().__init__(name)
        self.__name = name
        self.__v = v

    @property
    def getname(self):
        # должно быть что-то вроде super.__name
        return self.__name

    @property
    def textile_consumption(self): return float(self.__v / 6.5 + 0.5)


class Suit(Clothing):
    """ Создает экземпляр класса Suit.
                    name - наименование модели костюма
                    V - рост человека для которого предназначен костюм
    """

    def __init__(self, name, h):
        super().__init__(name)
        # по идее он должен наследовать параметр __name от родителя
        # выше даже конструктор родителя вызывается
        # но если в Coat __name прописать отдельно от конструктора
        # это будет один общий параметр для всех Coat и потомков
        # а как просто получить параметр __name, который определяется в конструкторе родителя,
        # от этого родителя - не понятно
        self.__name = name
        self.__h = h

    @property
    def getname(self):
        # должно быть что-то вроде super.__name
        return self.__name

    @property
    def textile_consumption(self): return float(2 * self.__h + 0.3)


a = Coat("m1", 68)
print(a.getname)
print(a.textile_consumption)
b = Suit("m2", 182)
print(b.getname)
print(b.textile_consumption)
print()


# task 3

class Cell:
    def __init__(self, cell_count):
        self.__cell_count = cell_count

    def __add__(self, other):
        return Cell(self.__cell_count + other.__cell_count)

    def __sub__(self, other):
        if (self.__cell_count - other.__cell_count) > 0:
            return Cell(self.__cell_count - other.__cell_count)
        else:
            print("Cell count <= 0")

    def __mul__(self, other):
        return Cell(self.__cell_count * other.__cell_count)

    def __truediv__(self, other):
        if type(other) is Cell:
            return Cell(int(self.__cell_count / other.__cell_count))
        else:
            if type(other) is int:
                return Cell(int(self.__cell_count / other))

    def make_order(self, cell_in_row):
        return ("*" * cell_in_row + "\n") * (self.__cell_count // cell_in_row) + "*" * (
                self.__cell_count % cell_in_row) + "\n"


a = Cell(18)
b = Cell(12)
c = a + b
print(c.make_order(7))
d = a - b
print(d.make_order(4))
e = a - d
f = c * a
print(d.make_order(8))
g = f / b
print(d.make_order(4))
g = g / 4
print(d.make_order(6))
