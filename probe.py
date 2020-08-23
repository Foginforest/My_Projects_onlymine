# -*- coding: utf-8 -*-

from random import randint

# Реализуем модель человека.
# Человек может есть, работать, играть, ходить в магазин.
# У человека есть степень сытости, немного еды и денег.
# Если сытость < 0 единиц, человек умирает.
# Человеку надо прожить 365 дней.
from termcolor import cprint


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None
        self.cat = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10

    def watch_mtv(self):
        cprint('{} смотрел MTV целый день'.format(self.name), color='green')
        self.fullness -= 10

    def buy_cat_food(self):
        print('{} купил кошачей еды'.format(self.name))
        self.house.cat_food += 50
        self.house.money -= 50

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} Вьехал в дом'.format(self.name), color='cyan')

    def clean_house(self):
        print('{} убрался в доме.'.format(self.name))
        self.house.purity += 100
        self.fullness -= 20

    def take_cat(self, cat):
        cprint('{} взял кота домой'.format(self.name), 'green')
        self.cat = cat
        self.cat.house = self.house

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness <= 20:
            self.eat()
        elif self.house.food <= 20:
            self.shopping()
        elif self.house.purity <= 0:
            self.clean_house()
        elif self.house.money < 50:
            self.work()
        elif self.house.cat_food < 10:
            self.buy_cat_food()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_mtv()


class Cat:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я кот - {}, сытость {}'.format(
            self.name, self.fullness)

    def cat_eat(self):
        cprint('Кот {} поел'.format(self.name), 'magenta')
        self.fullness += 20
        self.house.cat_food -= 10

    def destroy_wallpapers(self):
        cprint('Кот {} ободрал обои...'.format(self.name), 'red')
        self.house.purity -= 5
        self.fullness -= 10

    def cat_sleep(self):
        cprint('Кот {} спал целый день.'.format(self.name), 'blue')
        self.fullness -= 10

    def shit_everywhere(self):
        cprint('Кот {} обосрал все вокруг...'.format(self.name), 'red')
        self.fullness -= 20
        self.house.purity -= 40

    def act(self):
        if self.fullness < 0:
            cprint('Кот {} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 7)
        if self.fullness <= 10:
            self.cat_eat()
        elif self.house.cat_food < 10:
            self.destroy_wallpapers()
        elif self.fullness == 50:
            self.cat_sleep()
        elif dice == 1:
            self.cat_eat()
        elif dice == 2 or dice == 3:
            self.destroy_wallpapers()
        elif dice == 4:
            self.shit_everywhere()
        else:
            self.cat_sleep()


class House:

    def __init__(self):
        self.food = 50
        self.cat_food = 0
        self.money = 0
        self.purity = 100

    def __str__(self):
        return 'В доме еды осталось {}, денег осталось {}, чистота {}, кошачей еды осталось {}'.format(
            self.food, self.money, self.purity, self.cat_food)


cats = [
    Cat(name='Мурзик'),
    Cat(name='Тошка'),
    Cat(name='Лобзик')
]

citizens = [
    Man(name='Бивис'),
    Man(name='Батхед'),
    Man(name='Кенни'),
]

my_sweet_home = House()
for citisen in citizens:
    citisen.go_to_the_house(house=my_sweet_home)

for cat in range(len(cats)):
    citizens[cat].take_cat(cat=cats[cat])

for day in range(1, 366):
    print('================ день {} =================='.format(day))
    for citisen in citizens:
        citisen.act()
    for cat in cats:
        cat.act()
    print('--- в конце дня ---')
    for citisen in citizens:
        print(citisen)
    for cat in cats:
        cprint(cat, 'yellow')

    cprint(my_sweet_home, 'green')

# Создадим двух людей, живущих в одном доме - Бивиса и Батхеда
# Нужен класс Дом, в нем должн быть холодильник с едой и тумбочка с деньгами
# Еда пусть хранится в холодильнике в доме, а деньги - в тумбочке.
