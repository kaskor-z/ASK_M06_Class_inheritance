class Animal():
    alive = True
    fed = False

    def eat(self, food):
        if food.edible: print(F'{self.name} съел {food.name}'); self.fed = True
        else: print(f'{self.name} не стал есть {food.name}'); self.alive = False


class Mammal(Animal):

    def __init__(self, name):
        self.name = name


class Predator(Animal):

    def __init__(self, name):
        self.name = name


class Plant():
    edible = False

    def __init__(self):
        self.name = ''


class Flower(Plant):

    def __init__(self, name):
        self.name = name


class Fruit(Plant):
    edible = True

    def __init__(self, name):
        self.name = name


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)

# Что произошло: Хищник попытался съесть цветок и погиб, млекопитающее съело фрукт и насытилось.
