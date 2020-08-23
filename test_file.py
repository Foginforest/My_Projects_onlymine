from random import randint
import termcolor as t


class Men:

    def __init__(self, name):
        self.name = name
        self.fullness = 20
        self.mood = 100
        self.house = None

    def __str__(self):
        return 'У {} сытость {}, уровень настроения {}'.format(
            self.name, self.fullness, self.mood)

    def eat(self):
        t.cprint('{} поел'.format(self.name), 'magenta')
        self.house.food -= 10
        self.fullness += 10

    def work(self):
        t.cprint('{} сходил на работу'.format(self.name), 'cyan')
        self.house.money += 30
        self.fullness -= 10
        self.mood -= 50

    def shopping(self):
        print('{} сходил в магазин за продуктами'.format(self.name))
        self.house.money -= 50
        self.house.food += 50
        self.mood += 10

    def play_games(self):
        print('{} играл в игры целый день'.format(self.name))
        self.mood += 50
        self.fullness -= 10

    def watching_tv(self):
        print('{} смотрел телевизо целый день'.format(self.name))
        self.fullness -= 10
        self.mood += 50

    def move_into_house(self, house):
        self.house = house
        t.cprint('{} заехал в дом'.format(self.name), color='cyan')

    def feed_the_cat(self):
        print('{} покормил кота {}'.format(self.name, self.house.cat.name))
        self.house.cat.fullness += 20
        self.house.food -= 20

    def play_with_cat(self):
        print('{} поиграл с котом'.format(self.name))
        self.mood += 10
        self.house.cat.sleeping += 20
        self.house.cat.fullness -= 20
        self.house.cat.play -= 20

    def act(self):
        dice = randint(1, 6)
        if self.fullness <= 0:
            t.cprint('{} уиер....'.format(self.name), 'yellow')
        elif self.house.food <= 10:
            self.shopping()
        elif self.fullness <= 10:
            self.eat()
        elif self.house.cat.play <= 50 and self.fullness > 20:
            self.play_with_cat()
        elif self.house.money < 50:
            self.work()
        elif self.house.cat.fullness < 60:
            self.feed_the_cat()
        elif dice == 1 or dice == 3:
            self.watching_tv()
        elif dice == 2:
            self.work()
        elif dice == 4:
            self.watching_tv()
        else:
            self.play_games()


class House:

    def __init__(self):
        self.money = 200
        self.food = 200
        self.cat = None

    def __str__(self):
        return 'В доме денег {} еды {}'.format(self.money, self.food)

    def cat_is_into_house(self, cat):
        self.cat = cat
        t.cprint('Кот {} поселился в доме'. format(self.cat.name), color='cyan')


class Cat:

    def __init__(self, name):
        self.name = name
        self.fullness = 100
        self.play = 0
        self.sleeping = 0

    def __str__(self):
        return 'Кот {} сыт на {}% хочет играть на {}% хочет спать на {}%'.format(
            self.name, self.fullness, self.play, self.sleeping)

    def cat_living(self):
        self.fullness -= 10
        self.play += 20
        self.sleeping += 20
        if self.sleeping >= 100:
            self.cat_sleep()

    def cat_sleep(self):
        self.fullness -= 10
        self.play += 20
        self.sleeping -= 40


yurij = Men(name='Юрий')
maria = Men(name='Маша')
my_sweet_home = House()
murzik = Cat('Мурзик')
my_sweet_home.cat_is_into_house(murzik)
yurij.move_into_house(my_sweet_home)
maria.move_into_house(my_sweet_home)

for day in range(1, 32):
    murzik.cat_living()
    t.cprint('================= день {} ================='.format(day), 'red')
    yurij.act()
    maria.act()
    t.cprint(murzik, 'green')
    t.cprint(yurij, 'green')
    t.cprint(maria, 'green')
    t.cprint(my_sweet_home, 'yellow')
