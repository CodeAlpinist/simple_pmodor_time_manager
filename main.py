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
def reset_timer():
    global reps
    window.after_cancel(timer)
    check_mark_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    big_label.config(text="Timer", fg=GREEN)
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_sec)
        big_label.config(text="Break", fg=RED)
        reps = 0
    elif reps % 2 == 0:
        count_down(short_break_sec)
        big_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        big_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_min < 10:
        count_min = "0" + str(count_min)

    if count_sec < 10:
        count_sec = "0" + str(count_sec)
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            mark += "✓"
            check_mark_label.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Time Management")
window.config(padx=50, pady=50, bg=YELLOW)

big_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, 'bold'))
big_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, fill="white", text="00:00", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", bg=YELLOW, highlightthickness=0, relief="flat", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", bg=YELLOW, highlightthickness=0, relief="flat", command=reset_timer)
reset_button.grid(column=2, row=2)

check_mark_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, 'bold'))
check_mark_label.grid(column=1, row=3)

window.mainloop()

