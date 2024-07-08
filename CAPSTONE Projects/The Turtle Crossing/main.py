
def level_up():
    player.check_level_up()
    car_manager.level_up()
    scoreboard.level_up()










import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("grey56")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()

screen.onkey(player.move, "space")

car_manager = CarManager()

scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()

    if player.check_level_up() is True:
        level_up()

    # check car colission

    for cars in car_manager.all_cars:
        if player.distance(cars) < 26:
            game_is_on = False




scoreboard.game_over()



screen.exitonclick()



