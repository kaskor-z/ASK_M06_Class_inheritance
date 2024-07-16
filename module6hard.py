import math

class Figure():
    """
    Реализовать классы Figure(родительский), Circle, Triangle и Cube, объекты которых
        будут обладать методами изменения размеров, цвета и т.д.
    Многие атрибуты и методы должны быть инкапсулированны и для них должны быть
        написаны интерфейсы взаимодействия (методы) - геттеры и сеттеры.

    Каждый объект класса Figure должен обладать следующими атрибутами:

    Атрибуты(инкапсулированные):
        __sides(список сторон(целые числа)),
        __color(список цветов в формате RGB)
    Атрибуты(публичные):
        filled(закрашенный, bool)

    И методами:
    """

    def __init__(self):
        self.sides_count = 0
        self.__sides = 0
        self.__color = (0, 0, 0)
        self.filled = True

    def get_color(self):
        """
        Метод get_color, возвращает список RGB цветов.
        """
        return list(self.__color)

    def __is_valid_color(self, new_color):
        """
        Метод __is_valid_color - служебный, принимает параметры r, g, b,
        проверяет корректность переданных значений перед установкой нового цвета.
        Корректным цвет: все значения r, g и b - целые числа в диапазоне от 0 до 255 (включительно).
        """
        is_valid_color = True if len(new_color) == 3 else False
        if not is_valid_color: return is_valid_color
        for item in new_color:
            is_valid_color = True if item in range(256) and type(item) == int else False
            if not is_valid_color: break
        return is_valid_color

    def set_color(self, *new_color):
        """
        Метод set_color принимает параметры r, g, b - числа, и изменяет атрибут __color на
        соответствующие значения, предварительно проверив их на корректность.
        Если введены не корректные данные, то цвет остаётся прежним, не изменяется.
        """
        if type(new_color[0]) == tuple: new_color = new_color[0]
        if self.__is_valid_color(new_color):
            self.__color = new_color
        else:
            print(f'***** Такого цвета ( r, g, b = {new_color}) - НЕ БЫВАЕТ!!! *****')

    def __is_valid_sides(self, new_sides):
        """
        Метод __is_valid_sides - служебный, принимает неограниченное кол-во сторон,
        возвращает True если все стороны целые положительные числа и
        кол-во новых сторон совпадает с текущим, False - во всех остальных случаях.
        """
        is_valid_sides = True if len(new_sides) == self.sides_count else False
        if not is_valid_sides: return is_valid_sides
        for item in new_sides:
            is_valid_sides = True if type(item) == int and item > 0 else False
            if not is_valid_sides: break
        return is_valid_sides

    def set_sides(self, new_sides):
        """
        Метод set_sides(self, *new_sides) должен принимать новые стороны, если их количество
         не равно sides_count, то не изменяет стороны, в противном случае - изменяет на новые.
        """
        if self.__is_valid_sides(new_sides):
            self.__sides = new_sides
        else:
            print(f'------ Недопустимые прараметры изменения сторон фигуры !!!!! ------')

    def get_sides(self):
        """
        Метод get_sides() возвращает список сторон - значение(я) атрибута __sides.
        """
        return list(self.__sides)

    def __len__(self):
        """
        Метод __len__ возвращает периметр фигуры.
        """
        return sum(self.__sides)


class Circle(Figure):
    """
    Каждый объект класса Circle должен обладать следующими атрибутами и методами:
    - Все атрибуты и методы класса Figure;
    - Атрибуты класса Circle: sides_count = 1 ;
    - Атрибут __radius, рассчитан исходя из длины окружности (одной единственной стороны).

    """

    def __init__(self, color_, *new_sides):
        super().__init__()
        self.sides_count = 1
        super().set_color(color_)
        super().set_sides(self.__check_and_chang_sides_Circle(new_sides))
        self.set_radius()

    def __check_and_chang_sides_Circle(self, new_sides):
        """
         Метод __check_and_chang_sides_Circle() - служебный, проверяет колличеству сторон в
         исходных параметрах метода на соответствие кругу (1 сторна, она-же окружность, она-же периметр). Затем, при несоответствии, исходные параметры изменяются:
         Если колличество сторон в параметрах не равно 1, то они заменяются на 1 сторону длинной 1,
            т.е. создёт кортеж (1, ).
        """
        if len(new_sides) != self.sides_count:
            new_sides = []; new_sides.append(1); new_sides = tuple(new_sides); return new_sides
        return new_sides

    def set_radius(self):
        """
        сеттер для установки служебного атрибута __radius
        """
        self.__radius = super().__len__() / 2 / math.pi
        return

    def get_radius(self):
        """
        геттер для получения радиуса окружности
        """
        return self.__radius

    def get_square(self):
        """
        Метод get_square() возвращает площадь круга (можно рассчитывать как через длину, так и через радиус).
        """
        return math.pi * self.get_radius() ** 2


class Triangle(Figure):
    """
    Каждый объект класса Triangle должен обладать следующими атрибутами и методами:
    Все атрибуты и методы класса Figure
    Атрибут класса Triangle: sides_count = 3
    Атрибут __height, высота треугольника (можно рассчитать зная все стороны треугольника)
    """

    def __init__(self, color_, *new_sides):
        super().__init__()
        self.sides_count = 3
        self.__height = 0
        super().set_color(color_)
        super().set_sides(self.__check_and_chang_sides_Triangle(new_sides))
        self.set_height()

    def __check_and_chang_sides_Triangle(self, new_sides):
        """
         Метод __check_and_chang_sides_Triangle() - служебный, для проверки соответствия
         колличеству сторон треугольника, колличеству в исходный параметрах метода.
         При несоответствии, параметры изменяются:
          - если колличество сторон в запросе не равно 3, то заменяет их на 3 стороны длинной 1,
            т.е. создат кортеж (1, 1, 1).
        """
        if len(new_sides) != self.sides_count:
            new_sides = []
            for i in range(self.sides_count): new_sides.append(1)
            new_sides = tuple(new_sides)
        return new_sides

    def get_square(self):
        """
        Метод get_square() возвращает площадь текущего экземпляра треугольника.
        """
        s_square = super().__len__()/2
        for item in super().get_sides(): s_square *= (super().__len__()/2 - item)
        return math.sqrt(s_square)

    def set_height(self):
        """
        сеттер для установки служебного атрибута __height ,
        представляющего собой словарь (основание (сторона, одна из 3-х) : высота треугольника).
        """
        h_triangle = []
        for item in super().get_sides(): h_triangle.append(self.get_square() / item)
        h_triangle = tuple(h_triangle)
        self.__height = dict(zip(super().get_sides(), h_triangle))

    def get_height(self):
        """
        геттер для получения высот треугольника (в виде словаря - (сонование : высота))
         в зависимости от принятого основания (одно из 3-х сторон)
        """
        return self.__height


class Cube(Figure):
    """
    Атрибуты класса Cube: sides_count = 12
    Каждый объект класса Cube должен обладать следующими атрибутами и методами:
    Все атрибуты и методы класса Figure.
    Переопределить __sides сделав список из 12 одинаковы сторон (передаётся 1 сторона)
    Метод get_volume, возвращает объём куба.

    """

    def __init__(self, color_, *new_sides):
        super().__init__()
        self.sides_count = 12
        super().set_color(color_)
        super().set_sides(self.__check_and_chang_sides_Cube(new_sides))

    def __check_and_chang_sides_Cube(self, new_sides):
        """
        Метод __check_and_chang_sides_Cube() - служебный, для проверка колличеству сторон
        куба (для куба задаётся 1 сторона - грань куба), колличеству в исходных параметрах метода.
         Затем:
          - переопределяет __sides , создав кортеж из 12 одинаковы сторон (передаётся 1 грань куба).
          - если в параметрах указана не 1 сторона (грань куба), то длина стороны принимеется = 1 и
            создаётся кортеж (1, 1, 1, 1, ..., 1, 1) из 12 единиц (по колличесву сторон куба).
        """
        new_sides_1 = 1 if len(new_sides) != 1 else list(new_sides)[0]
        new_sides = []
        for i in range(self.sides_count): new_sides.append(new_sides_1)
        new_sides = tuple(new_sides)
        return new_sides

    def _set_sides(self, cube_face):
        """
        Метод _set_sides() - служебный, принимает новую длину грани в качестве
        параметра для изменения текущего экземпляра куба.
        """
        new_sides = []; new_sides.append(cube_face); new_sides = tuple(new_sides)
        super().set_sides(self.__check_and_chang_sides_Cube(new_sides))
        return

    def get_cube_face(self):
        """
        Метод get_cube_face(), возвращает длину грани текущего экземпляра куба.
        """
        self.cube_face = list(super().get_sides())[0]
        return self.cube_face

    def get_volume(self):
        """
        Метод get_volume(), возвращает объём текущего экземпляра куба.
        """
        self.__sides = super().get_sides()
        return list(self.__sides)[0] ** 3


#           Код для проверки:
#
circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color((300, 70, 15)) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides((5, 3, 12, 4, 5)) # Не изменится
print(cube1.get_sides())
circle1.set_sides((15,)) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

# #
# #                   КОД ДЛЯ РАСШИРЕННОЙ ПРОВЕРКИ!!
# #
# print(f'\n**************           РАСШИРЕННАЯ ПРОВЕРКИ!!!         **************\n')
# #
# #           ТРЕУГОЛЬНИК!!!!
# triangle_1 = Triangle((0, 255, 223), 11, 15, 12)
# print(f'\n Triangle_1 Создан новый экземпляр треуголника - New_Sides = {triangle_1.get_sides()} New_Color = {triangle_1.get_color()}')
# #       проверка изменения цвета
# print(f'\n Triangle_1 Текущий цвет треугольник = {triangle_1.get_color()}')
# new_color_ = 111, 255, 210
# print(f' Triangle_1 Изменяем цвет на новый цвет = {new_color_}')
# triangle_1.set_color(new_color_)
# print(f' Triangle_1 Новый цвет треугольника = {triangle_1.get_color()} ===========')
# #       проверка изменения сторон
# print(f'\n Triangle_1 Текущий длины сторон теругольника = {triangle_1.get_sides()}')
# new_sides_ = 20, 25, 30
# print(f' Triangle_1 Изменяем длину сторон треугольника = {new_sides_}')
# triangle_1.set_sides(new_sides_)
# print(f' Triangle_1 Новые длины сторон треугольника = {triangle_1.get_sides()} ===========')
# #       проверка других характеристик
# print(f'\n Triangle 01  ***************    Стороны треуголника (Triangle sides) = {triangle_1.get_sides()}  ***************')
# print(f' Triangle 02  ***************    Площадь треуголника (Triangle area) = {triangle_1.get_square()}  ***************')
# print(f' Triangle 03  ***************    Высоты треугольника (в зависимости от основания) H = {triangle_1.get_height()}\n')
#
# #           КРУГ (ОКРУЖНОСТЬ)!!!!
# circle2 = Circle((0, 200, 100), 20)
# print(f'\n circle2 Создан новый экземпляр круга - new_sides = {circle2.get_sides()} new_color = {circle2.get_color()}')
# print(f' circle2 Радиус окружности = {circle2.get_radius()}')
# #       проверка изменения цвета
# print(f'\n circle2 Текущий цвет фигуры = {circle2.get_color()}')
# new_color_ = 155, 166, 177
# print(f' circle2 Изменяем цвет на новый = {new_color_}')
# circle2.set_color(new_color_)
# print(f' circle2 Новый цвет фигуры = {circle2.get_color()} ===========')
# #       проверка изменения длины окружности
# print(f'\n circle2 Текущая длины окружности P = {circle2.__len__()}')
# P_ = 100
# print(f' circle2 Изменяем длину окружности = {P_}')
# new_sides_ = []; new_sides_.append(P_); new_sides_ = tuple(new_sides_)
# circle2.set_sides(new_sides_)
# print(f' circle2 Новая длины окружности = {circle2.__len__()} ===========')
# #       проверка других характеристик
# print(f'\n Circle  001 ***************    длина окружности P = {circle2.__len__()} **************')
# circle2.set_radius()
# print(f' Сircle  002 ***************    радиус окружности = {circle2.get_radius()} **************')
# print(f' Circle  003 ***************    площадь круга = {circle2.get_square()} **************')
# #          КУБ!!!!
# cube1 = Cube((10, 210, 250), 12)
# print(f'\n circle1 Создан новый экземпляр куба - Cube_Face = {cube1.get_cube_face()} Color = {cube1.get_color()}')
# #       проверка изменения цвета
# print(f'\n cube1 Текущий цвет фигуры = {cube1.get_color()}')
# new_color_ = 111, 255, 210
# print(f' circle1 Изменяем цвет на новый = {new_color_}')
# cube1.set_color(new_color_)
# print(f' cube1 Новый цвет фигуры = {cube1.get_color()} ===========')
# #       проверка изменения длины окружности
# print(f'\n cube1 Текущие длины граней куба __sides = {cube1.get_sides()}')
# cube_face_ = 10
# print(f' cube1 Изменяем длинну грани куба = {cube_face_}')
# cube1._set_sides(cube_face_)
# print(f' cube1 Новые длины грани куба cube_face = {cube1.get_cube_face()} ===========')
# #       проверка других характеристик
# print(f' Cube() ****** Объём куба = {cube1.get_volume()} **************\n')
# print('*************************************************************************\n')
