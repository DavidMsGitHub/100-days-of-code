from turtle import Screen, Turtle

import paddle
import ball
import time
import scoreboard

p1_score = 0
p2_score = 0

paddle_1 = paddle.Paddle((-350, 0))
paddle_2 = paddle.Paddle((350, 0))

scoreboard_p1 = scoreboard.Scoreboard((-60, 220))
scoreboard_p2 = scoreboard.Scoreboard((60, 220))

screen = Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.tracer(False)

c_line = Turtle()

c_line.color("white")
c_line.width(2)
c_line.penup()
c_line.goto(0, -300)
c_line.pendown()
c_line.setheading(90)
for _ in range(60):
    c_line.forward(10)
    c_line.penup()
    c_line.forward(10)
    c_line.pendown()

screen.listen()
screen.onkey(paddle_1.move_up, "w")
screen.onkey(paddle_1.move_down, "s")
screen.onkey(paddle_2.move_up, "Up")
screen.onkey(paddle_2.move_down, "Down")


game_is_on = True

ball = ball.Ball()
while game_is_on:
    screen.update()
    time.sleep(ball.game_speed)
    ball.move()
    #collizia zemo da qvemo kedeltan
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce()

    # kolizia pongis bodystan

    if ball.distance(paddle_1) < 50 and ball.xcor() < -330:
        ball.bounce_from_paddle()

    elif ball.distance(paddle_2) < 50 and ball.xcor() > 330:
        ball.bounce_from_paddle()

    # kolizia gverdita kedlebtan da + qula

    if ball.xcor() > 400:
        p1_score += 1
        scoreboard_p1.add_score(p1_score)
        ball.reset_position()

    elif ball.xcor() < -400:
        p2_score += 1
        scoreboard_p2.add_score(p2_score)
        ball.reset_position()











screen.exitonclick()