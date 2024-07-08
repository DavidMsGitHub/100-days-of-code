from turtle import Turtle
import pandas

data = pandas.read_csv("50_states.csv")

guessed_states = []

class QuizBrain(Turtle):
    def __init__(self):
        self.score = 0

    def check_answer(self, user_answer):
        answer = data[data.state == user_answer]
        if not answer.empty:
            if user_answer not in guessed_states:
                retrieved_data = data[data.state == user_answer]
                x_coord = int(retrieved_data.x.values[0])
                y_coord = int(retrieved_data.y.values[0])

                its_coords = (x_coord, y_coord)
                guessed_states.append(user_answer)
                self.reveal_state(its_coords, user_answer)
                self.score = len(guessed_states)
            else:
                print("You have already guessed it")
        else:
            print("this state is not in data")

    def reveal_state(self, coords, state_name):
        new_state = Turtle()
        new_state.hideturtle()
        new_state.penup()
        new_state.goto(coords)
        new_state.write(state_name, False, "center", ("Helvetica", 15, "normal"))



