from turtle import Turtle
import random
import math

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.75, 0.75)
        self.color("blue")
        self.speed(0)
        self.refresh()

    def refresh(self):
        random_x = round(random.randint(-280, 280), 2)
        random_y = round(random.randint(-280, 280), 2)
        self.goto(random_x, random_y)
