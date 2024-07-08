import turtle as t

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
screen = t.Screen()
screen.bgcolor("black")

timmy = t.Turtle()
timmy.shape("arrow")
timmy.color("white")
timmy.speed(0)
timmy.pensize(2)

num = 0
angle = 0
for i in range(90):
    timmy.color(colours[num])
    timmy.circle(60)
    timmy.setheading(angle)
    angle += 8
    num += 1
    if num > 13:
        num = 0






screen.exitonclick()