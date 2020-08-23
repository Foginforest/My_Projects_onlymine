from random import randint

import simple_draw as sd


class Snowflake:

    def __init__(self, x, y):
        self.length = 50
        self.color = sd.COLOR_WHITE
        self.speed = 50
        self.point = sd.get_point(x, y)

    def clear_previus_picture(self):
        sd.clear_screen()

    def move(self):
        self.point.y -= self.speed

    def draw(self):
        sd.snowflake(center=self.point, length=self.length, color=self.color)


flake = Snowflake(x=randint(20, 500), y=randint(400, 500))
while True:
    flake.clear_previus_picture()
    flake.move()
    flake.draw()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break
