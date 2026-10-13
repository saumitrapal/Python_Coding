from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"



#-----------------------------------------------------UI STYLE----------------------------------------------#
window = Tk()
window.title("Flashy Game")
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)

canvas = Canvas(width=1000, height=526)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="./images/card_front.png")
canvas.create_image(500, 270, image=card_front_img)
canvas.create_text(500, 150, text="Title", font=("Arial", 40, "italic"))
canvas.create_text(500, 263, text="Word", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)
# canvas.place(anchor="center")





card_back_img = PhotoImage(file="./images/card_back.png")

button_right_img = PhotoImage(file="./images/right.png")
button_right = Button(image=button_right_img, highlightthickness=0)
button_right.grid(column=1, row=1, pady=48)


button_wrong_img = PhotoImage(file="./images/wrong.png")
button_wrong = Button(image=button_wrong_img, highlightthickness=0)
button_wrong.grid(column=0, row=1, pady=48)


# franch_word = Label(canvas, text="French", font=("Arial", 40, "italic"), bg="white")
# franch_word.place(anchor="center", x=500, y=150)


# englist_word = Label(canvas, text="Trouve", font=("Arial", 60, "bold"), bg="white")
# englist_word.place(anchor="center", x=500, y=263)













window.mainloop()
