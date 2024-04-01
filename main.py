from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Comic Sans MS"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    main_label.config(text="Being lazy >:c")
    check_mark.config(text="")
    global reps
    reps = 0
    start_button.config(state="active")


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    start_button.config(state="disabled")
    global reps
    reps += 1
    work_secs = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_sec)
        main_label.config(text="Long Break")
    elif reps % 2 == 0:
        count_down(short_break_sec)
        main_label.config(text="Short Break")
    else:
        count_down(work_secs)
        main_label.config(text="WORK!")
        mark = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            mark += "✔"
        check_mark.config(text=mark)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.minsize(300, 500)
window.config(padx=100, pady=80, bg=PINK)

# highlightthickness gets rid of the weird border, not documented
# fg = "somecolor"
canvas = Canvas(width=200, height=224, bg=PINK, highlightthickness=0)
background = PhotoImage(file="images/tomato.png")

canvas.create_image(100, 112, image=background)
timer_text = canvas.create_text(100, 120, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=2)

main_label = Label()
main_label.config(text="Being lazy >:c", font=(FONT_NAME, 20, "bold"), fg="#000000", bg=PINK)
# main_label.place(x=40, y=300)
main_label.grid(row=0, column=2)

start_button = Button()
start_button.config(width=5, height=0, text="Start", command=start_timer)
# start_button.place(x=0, y=300)
start_button.grid(row=3, column=1)

reset_button = Button(command=reset_timer)
reset_button.config(width=5, height=0, text="Reset")
# reset_button.place(x=220, y=300)
reset_button.grid(row=3, column=3)

check_mark = Label()
check_mark.config(bg=PINK, font=(FONT_NAME, 25), background=PINK, foreground=RED)
# check_mark.place(x=110, y=290)
check_mark.grid(row=3, column=2)
window.mainloop()
