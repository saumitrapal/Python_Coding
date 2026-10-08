from tkinter import *
import math

FONT = ("Cuerier", 48, "bold")
BUTTON_FONT = ("Cuerier", 16, "bold")
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5 
LONG_BREAK_MIN = 20
CHECKMARK = "✔"
REPS = 0
time = None

#-----------------------------------------------RESTART TIME---------------------------------------------------------#
def restart_time():
    window.after_cancel(time)
    canvas.itemconfig(timer_text, text=f"00:00")
    check.config(text="")
    
    global REPS
    REPS = 0

    
#-----------------------------------------------TIMER MACHENISIOM---------------------------------------------------#
def start_timer():
    global REPS
    REPS += 1
    
    long_break_time_sec = LONG_BREAK_MIN * 60
    short_break_time_sec = SHORT_BREAK_MIN * 60
    work_time_sec = WORK_MIN * 60
    
    if REPS % 2 == 0:
        timer["text"] = "Short Break"
        timer["fg"] = PINK
        count_down(short_break_time_sec)
    elif REPS % 2 != 0:
        timer["text"] = "Work Time"
        timer["fg"] = GREEN
        count_down(work_time_sec)
    elif REPS % 8 == 0:
        timer["text"] = "Long Break"
        timer["fg"] = RED
        count_down(long_break_time_sec)


#-----------------------------------------------FUNCTINALITY---------------------------------------------#
# import time
# count_time = True
# count = 5
# while count_time:
#     time.sleep(1)
#     count -= 1
#     timer["text"] = count
#     if count == 0:
#         count_time = False


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    elif count_sec == 0:
        count_sec = "00"
    
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global time
        time = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(REPS / 2)
        for _ in range(work_sessions):
            mark += CHECKMARK
            
        check.config(text=mark)
        


#----------------------------UI_STYLE--------------------------------------------------------#

#Create window
window = Tk()
window.title("Pomodoro Clock")
window.config(padx=100, pady=50, bg=YELLOW)

# Promodoro Technique Label
timer = Label(text="Timer", fg=GREEN, bg=YELLOW)
timer.config(font=FONT)
timer.grid(column=1, row=0)

# Create a canvas
canvas = Canvas(width=500, height=500, highlightthickness=0, bg=YELLOW)
background_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=background_image)
timer_text = canvas.create_text(100, 130, text="00:00", font=FONT, fill="white")
canvas.grid(column=1, row=1)
# count_down(5)


#Start Button
start_button = Button(text="Start", font=BUTTON_FONT, highlightthickness=0, command=start_timer)
# start_button.grid(column=1, row=3, padx=100, pady=48)
start_button.grid(column=0, row=2)

#Retart Button
restart_button = Button(text="Restart", font=BUTTON_FONT, highlightthickness=0, command=restart_time)
# restart_button.grid(column=1, row=4, padx=200, pady=48)
restart_button.grid(column=2, row=2)

#Create a checkmark
check = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 24))
check.grid(column=1, row=3)



# Hold window
window.mainloop()