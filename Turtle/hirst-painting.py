# import colorgram
#
#
# # colors = colorgram.extract('image.jpg', 30)
# #
# # gay = colors[0]
# #
#
# #
# #
# # for color in colors:
# #     r = color.rgb.r
# #     g = color.rgb.g
# #     b = color.rgb.b
# #     new_color = (r, g, b)
# #     color_list.append(new_color)
import turtle as t
import random

screen = t.Screen()
screen.bgcolor("black")
t.colormode(255)
timmy = t.Turtle()
timmy.shape("arrow")
timmy.color("white")
timmy.speed(0)
timmy.pensize(2)
timmy.penup()
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)

color_list = [(243, 243, 245), (244, 240, 232), (244, 237, 242), (236, 243, 240), (214, 154, 105), (49, 96, 139), (163, 80, 45), (223, 209, 107), (17, 36, 59), (185, 163, 25), (120, 163, 202), (56, 30, 18), (126, 68, 94), (210, 91, 69), (43, 128, 70), (193, 140, 160), (162, 20, 10), (125, 181, 156), (58, 28, 40), (129, 26, 42), (19, 52, 43), (194, 91, 113), (48, 170, 98), (39, 62, 97), (27, 91, 52), (235, 162, 187), (108, 118, 172), (225, 206, 2), (6, 88, 108), (227, 179, 170)]

for _ in range(10):
    for i in range(10):
        color = random.choice(color_list)
        timmy.color(color)
        timmy.dot(20)
        timmy.forward(50)
    timmy.left(90)
    timmy.forward(50)
    timmy.left(90)
    timmy.forward(500)
    timmy.left(180)


