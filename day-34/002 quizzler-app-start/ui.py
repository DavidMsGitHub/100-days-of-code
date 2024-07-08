THEME_COLOR = "#375362"
import tkinter as tk
import time
from quiz_brain import QuizBrain
class QuizGUI():
    def __init__(self, quiz_brain: QuizBrain):

        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.configure(padx=20, pady=20,bg=THEME_COLOR)
        self.window.title("Quizzler")
        self.quiz_score = 0


        #score indicator
        self.score_label = tk.Label(text= f"Score: {self.quiz_score}", padx=20, highlightthickness=0, bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)
        #middle canvas
        self.canvas = tk.Canvas(width=300, height=250, bg="white", highlightthickness=0)

        self.question_text = self.canvas.create_text(150,125,text="Some Question Text", width= 290,fill=THEME_COLOR, font="Arial 20 italic")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

    #buttons

        image_of_yes = tk.PhotoImage(file="images/true.png")
        self.yes_button = tk.Button(image=image_of_yes,highlightthickness=0, command= self.yes_button_pressed)
        self.yes_button.grid(column=0, row=2)

        image_of_no = tk.PhotoImage(file="images/false.png")
        self.no_button = tk.Button(image=image_of_no,highlightthickness=0, command= self.no_button_pressed)
        self.no_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text="CONGRATS BRO, THATS END")
            self.yes_button.config(state="disabled")
            self.no_button.config(state="disabled")

    def yes_button_pressed(self):
        is_right = self.quiz.check_answer(user_answer="True")
        self.give_feedback(is_right)

    def no_button_pressed(self):
        is_right = self.quiz.check_answer(user_answer="False")
        self.give_feedback(is_right)


    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="limegreen")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
