import turtle as t
import time
import heroes
import random

timmy = t.Turtle()
timmy.shape("arrow")
timmy.color("white")
timmy.speed(2)

colours = [
    "Red",
    "OrangeRed",
    "Orange",
    "Gold",
    "Yellow",
    "GreenYellow",
    "LimeGreen",
    "Green",
    "SpringGreen",
    "Cyan",
    "DodgerBlue",
    "Blue",
    "MediumSlateBlue",
    "DarkViolet",
    "Magenta"
]

random_angle = [0, 90, 180, 270]


screen = t.Screen()
screen.bgcolor("black")
color_num = 1
timmy.speed(0)
for i in range(500):
    timmy.pensize(7)
    timmy.forward(20)
    timmy.color(colours[color_num])
    timmy.setheading(random.choice(random_angle))
    color_num += 1
    if color_num > 13:
        color_num = 0
    timmy.write(i)

screen.exitonclick()





