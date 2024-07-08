from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def timer_reset():
    window.after_cancel(timer)
    Label_Timer.config(text="Timer", pady=20, bg=YELLOW, fg=GREEN, font=(FONT_NAME, 70, "bold"))
    Label_Checkmark["text"] = ""
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0



# ---------------------------- TIMER MECHANISM ------------------------------- # 

def timer_start():
    global reps

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60


    reps += 1
    if reps % 8 == 0:
        Label_Timer["text"] = "Break"
        Label_Timer["fg"] = RED
        countdown(long_break_sec)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        Label_Timer["text"] = "Break"
        Label_Timer["fg"] = PINK
    else:
        countdown(work_sec)
        Label_Timer["text"] = "Work"
        Label_Timer["fg"] = GREEN





# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(count):
    global timer


    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
      timer = window.after(1000, countdown, count - 1)
    else:
        timer_start()
        if reps % 2 == 0:
            Label_Checkmark["text"] += "✅"


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=60, pady=10, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file='tomato.png')
canvas.create_image(100, 100, image=tomato_image)
timer_text = canvas.create_text(100, 115, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1,pady=20)

button_start = Button(text= "Start", command= timer_start, padx=5, pady=5, fg="Black", font=(FONT_NAME,15,"bold"), highlightbackground=RED, highlightthickness= 0.1)
button_start.grid(row=2,column=0)

button_reset = Button(text="Reset", command= timer_reset, highlightbackground=RED, highlightthickness= 0.1, padx=5, pady=5, fg="Black", font=(FONT_NAME,15,"bold"))
button_reset.grid(row=2, column=2)

Label_Timer = Label(text="Timer", pady=20, bg=YELLOW, fg= GREEN, font=(FONT_NAME, 70, "bold"))
Label_Timer.grid(row=0,column=1)

Label_Checkmark = Label( font=(FONT_NAME, 20, "bold"), highlightthickness=0, bg=YELLOW)
Label_Checkmark.grid(row=3,column=1)

window.mainloop()
