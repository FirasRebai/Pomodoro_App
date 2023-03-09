import random
from tkinter import *
from tkinter import messagebox
import math
import winsound

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 15
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = random.randint(15, 30)
reps = 0
timer = ""


# break_result = ""


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # if it's the 8th:
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    # if it's the 2nd/4th/6th rep:
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)

    # if it's the 1st/3rd/5th/7th rep:
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)
        # if reps > 1:
        #     messagebox.showinfo("Timer", "Pause Finished")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    # global break_result
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif len(str(count_sec)) == 1:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1, count_down, count - 1)

    else:
        if reps % 7 == 0:
            winsound.PlaySound('chicken.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
            break_result = messagebox.showinfo("Timer", "Take a LONG BREAK!")
            if break_result == "ok":
                winsound.PlaySound(None, winsound.SND_PURGE)
                start_timer()
                marks = ""
                work_sessions = math.floor(reps / 2)
                for _ in range(work_sessions):
                    marks += "✔"
                check_marks.config(text=marks)
        elif reps % 2 != 0:
            winsound.PlaySound('chicken.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
            break_result = messagebox.showinfo("Timer", "Take a 5 MIN PAUSE")
            if break_result == "ok":
                winsound.PlaySound(None, winsound.SND_PURGE)
                start_timer()
                marks = ""
                work_sessions = math.floor(reps / 2)
                for _ in range(work_sessions):
                    marks += "✔"
                check_marks.config(text=marks)
        elif reps % 2 == 0 and reps > 1:
            winsound.PlaySound('chicken.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
            break_result = messagebox.showinfo("Timer", "PAUSE FINISHED,GO BACK TO WORK")
            if break_result == "ok":
                winsound.PlaySound(None, winsound.SND_PURGE)
                start_timer()
                marks = ""
                work_sessions = math.floor(reps / 2)
                for _ in range(work_sessions):
                    marks += "✔"
                check_marks.config(text=marks)

        # else:
        #     break_result = messagebox.showinfo("Timer", "Take a 5 MIN PAUSE")
        # if reps % 2 == 0:
        #     check_marks.config(text="✔")
        # else:
        #     check_marks.config(text="")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
chicken_img = PhotoImage(file="egg1.png")
canvas.create_image(100, 112, image=tomato_img)
# canvas.create_image(100, 50, image=chicken_img)

timer_text = canvas.create_text(115, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
title_label.grid(column=2, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=1, row=3)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=3, row=3)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=2, row=4)

window.mainloop()
