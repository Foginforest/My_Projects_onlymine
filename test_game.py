import random


def secret_number():
    number = random.randint(1000, 10000)
    return number


def check_the_number(number=secret_number(), users_number):
    number_list = [i for i in str(number)]


def is_game_over():
    pass


while True:
    users_number = input('Введите число')
    print(users_number)
        if users_number == number:
            print('4 быка')
        users_number_list = [j for j in str(users_number)]
        for i in number_list:
            for j in users_number_list:
                if i == j:
                    print('Бык')