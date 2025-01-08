# Наследование классов. Практика

class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__sides = list(sides)
        self.__color = color
        self.filled = True

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        for color in (r, g, b):
            if isinstance(color, int) and 0 <= color <= 255:
                return True
            else:
                return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)
        return

    def __is_valid_sides(self, sides):
        for side in sides:
            if isinstance(side, int) and len(sides) == self.sides_count:
                return True
            else:
                return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if len(sides) == self.sides_count:
            pass
        else:
            self.set_sides(1)
        self.__radius = len(self) / 6.28

    def get_square(self):
        return 3.14 * self.__radius ** 2


'''
проверкой по задаче это не выявляется
в задаче говорится, что Метод get_square возвращает площадь круга (можно рассчитать как через длину, так и через радиус),
но если делать через радиус то
тут не меняется self.__radius при смене значения стороны, я так понимаю что при <init> радиус определяем и 
потом при смене значения стороны, соответственно меняется и длина(периметр), но хоть и длина участвует
в вычислении атрибута радиус, этот атрибут не меняется
получается при обращении к методу <get_square>, он выдергивает атрибут радиус который неизменяемый.
для меня решение это пока не использовать атрибут радиус, а вычислять через длину(периметр) так:
    <return 3.14 * (len(self) / 6.28) ** 2>
просто хотел бы 
понять есть ли решение с использованием атрибута радиус(раз уж и в инструкции говорится), или это лишние сложности
'''


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if len(sides) == self.sides_count:
            check_list = sorted(sides)
            if check_list[0] + check_list[1] > check_list[2]:
                pass
            else:
                print('Такого треугольника не существует. Сумма любых двух сторон должна быть больше третьей.')
        else:
            self.set_sides(1, 1, 1)

    def get_square(self):
        a, b, c = self.get_sides()
        p = (a + b + c) / 2
        return round((p * (p - a) * (p - b) * (p - c)) ** 0.5, 3)


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if len(sides) == 1:
            sides_list = []
            for count in range(self.sides_count):
                sides_list.append(*sides)
            self.set_sides(*sides_list)
        else:
            self.set_sides(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)

    def get_volume(self):
        # res_ = self.get_sides()[0]            ДЛЯ СЕБЯ
        # print(res_ ** 3)
        return self._Figure__sides[0] ** 3


'''
 ? сначала не понял можно ли сделать иначе, не используя <_Figure__sides[0]> 
 или здесь и был смысл показать, что можно обращаться к атрибуту так, через родителя.
 Потом сделал код для треугольника
 Потом опять решил вернуться и подумать, и понял, что в коде треугольника я и делал иначе не обращаясь к родителю )))
'''

circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())

cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())

circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

# доп проверка
print('\nдополнительная проверка')
circle2 = Circle((200, 200, 100), 10, 15, 6)
triangle1 = Triangle((200, 200, 100), 10, 6)
cube2 = Cube((200, 200, 100), 9)
cube3 = Cube((200, 200, 100), 9, 12)

print(circle2.get_sides())
print(triangle1.get_sides())
print(cube2.get_sides())
print(cube3.get_sides())

print('\nпроверка изменение стороны к изменению площади у круга')
print(circle1.get_sides())
print(circle1.get_square())
circle1.set_sides(10)
print(circle1.get_sides())
print(circle1.get_square())

print('\nпроверка правильности сторон треугольника')
triangle2 = Triangle((200, 200, 100), 3, 1, 2)
print(triangle2.get_square())
triangle3 = Triangle((200, 200, 100), 3, 4, 5)
print(triangle3.get_square())
