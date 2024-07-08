import turtle as t
import time
from food import Food
from snake import Snake
from scoreboard import Scoreboard

screen = t.Screen()

screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Welcome to David's Snake")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
scoreboard.update_scoreboard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")
screen.onkey(snake.left, "a")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


def main_game():
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()


      # Food Collision
        if snake.head.distance(food) < 15:
            scoreboard.score += 1
            scoreboard.update_scoreboard()
            snake.extend()
            food.refresh()

      # Wall Collision

        if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
            scoreboard.reset()
            snake.reset()

    # tail colision

        for segment in snake.all_segments[1:]:
            if snake.head.distance(segment) < 10:
                scoreboard.reset()
                snake.reset()

    scoreboard.reset()
    scoreboard.game_over()





main_game()





screen.exitonclick()