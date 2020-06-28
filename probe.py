def zero(*args, **kwargs):
    number = 0
    return number


def one(*args, **kwargs): return 1


def two(*args, **kwargs): return 2


def three(*args, **kwargs): return 3


def four(*args, **kwargs): return 4


def five(*args, **kwargs): return 5


def six(*args, **kwargs): return 6


def seven(operation):
    if operation == '*':
        return 7 * number



def eight(*args, **kwargs): return 8


def nine(*args, **kwargs): return 9


def plus(*args, **kwargs): return '+'


def minus(*args, **kwargs): return '-'


def times(number):
    return '*'


def divided_by(*args, **kwargs): '//'


print(seven(times(five())))
