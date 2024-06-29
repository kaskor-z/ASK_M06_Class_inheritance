class Vehicle():
    """
    owner (str)  -  владелец транспорта.(владелец может меняться)
    __model (str) - модель(марка) транспорта.(мы не можем менять название модели)
    __engine_power (int) - мощность двигателя.(мы не можем менять мощность двигателя самостоятельно)
    __color (str) - название цвета.(мы не можем менять цвет автомобиля своими руками)
                    А так же атрибут класса:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white', 'brown', 'lemon', 'orange']
                    Атрибут класса в который записан список допустимых цветов для окрашивания.
    """
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white', 'brown', 'lemon', 'orange']

    def __init__(self, owner, model, color, engine_power):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color
        pass

    def get_model(self):
        """ get_model() - метод возвращает строку: "Модель: <название модели транспорта> """
        print('Модель:', self.__model)

    def get_horsepower(self):
        """ get_horsepower() - метод возвращает строку: "Мощность двигателя: <мощность> """
        print('Мощность двигателя:', self.__engine_power)

    def get_color(self):
        """ get_color() - метод возвращает строку: "Цвет: <цвет транспорта> """
        print('Цвет:', self.__color)

    def print_info(self):
        """
        Распечатывает результаты методов (в том же порядке):
        get_model, get_horsepower, get_color; а так же владельца
        в конце в формате "Владелец: <имя>"
        """
        self.get_model()
        self.get_horsepower()
        self.get_color()
        print('Владелец:', self.owner)


    def set_color(self, new_color):
        """ set_color(new_color) - метод принимает аргумент new_color(str), меняет цвет __color на new_color,"""
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'\nНельзя изменить цвет на {new_color}.\n')


class Sedan(Vehicle):
    """ __PASSENGERS_LIMIT - константа (в седан может поместиться только 5 пассажиров)"""
    __PASSENGERS_LIMIT = 5


#     Создаём объект - ртанспортное средство
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
vehicle1.print_info()
#     Иеняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
#     Проверяем что изменилось
vehicle1.print_info()
