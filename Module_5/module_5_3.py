# Перегрузка операторов

class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует')

        else:
            for i in range(1, new_floor + 1):
                print(i)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {len(self)}'

    def __eq__(self, other):
        return isinstance(other, House) and len(self) == len(other)

    def __lt__(self, other):
        return isinstance(other, House) and len(self) < len(other)

    def __le__(self, other):
        return isinstance(other, House) and len(self) <= len(other)

    def __gt__(self, other):
        return isinstance(other, House) and len(self) > len(other)

    def __ge__(self, other):
        return isinstance(other, House) and len(self) >= len(other)

    def __ne__(self, other):
        return isinstance(other, House) and len(self) != len(other)

    def __add__(self, other):
        if isinstance(other, int):
            self.number_of_floors = len(self) + other
        return self

    def __radd__(self, other):
        if isinstance(other, int):
            return self + other

    def __iadd__(self, other):
        if isinstance(other, int):
            return self + other


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)  # __eq__

h1 = h1 + 10  # __add__
print(h1)
print(h1 == h2)

h1 += 10  # __iadd__
print(h1)

h2 = 10 + h2  # __radd__
print(h2)

print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__
