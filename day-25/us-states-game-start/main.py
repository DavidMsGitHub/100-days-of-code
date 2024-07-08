import turtle
import pandas
import game_mechanism

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


quiz = game_mechanism.QuizBrain()

quiz_is_on = True


while quiz_is_on:
    guessed_counter = f"{quiz.score}/50 States Guessed"
    answer_state = screen.textinput(guessed_counter, "Type in State name you know").title()
    quiz.check_answer(answer_state)



screen.exitonclick()