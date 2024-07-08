import turtle as t
import random


screen = t.Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Type Color of turtle you think will win")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

y_position_adder = -100
for turtle_index in range(0, 6):
    new_turtle = t.Turtle("turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-230, y_position_adder)
    y_position_adder += 30
    all_turtles.append(new_turtle)
    print(all_turtles)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"ou've lost! The {winning_color} turtle is the winner!")
        r_distance = random.randint(0, 10)
        turtle.forward(r_distance)


screen.exitonclick()