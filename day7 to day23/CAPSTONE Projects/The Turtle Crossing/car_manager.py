COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
import random as r
from turtle import Turtle
import time


class CarManager(Turtle):

    def __init__(self):
        self.all_cars = []
        self.move_distance = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = r.randint(1, 4)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            random_y = r.randint(-250, 300)
            new_car.goto(300, random_y)
            new_car.shape("square")
            new_car.shapesize(1, 2)
            new_car.color(COLORS[r.randint(0, 5)])
            self.all_cars.append(new_car)


    def move_car(self):
        for car in self.all_cars:
            car.backward(self.move_distance)

    def level_up(self):
        self.move_distance += MOVE_INCREMENT






