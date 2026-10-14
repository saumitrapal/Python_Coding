from tkinter import *
import pandas
import random
import time


BACKGROUND_COLOR = "#B1DDC6"
data = pandas.read_csv("./data/french_words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}

#--------------------------------------------------------FIND MEANING AFTER 3 SECOUD-------------------------#
# def find_word_meaning():
#     english_word_dataframe = pandas.read_csv("./data/french_words.csv")
#     english_word_list = english_word_dataframe["English"].tolist()
#     french_word_list = english_word_dataframe["French"].tolist()
#     random_english_word = random.choice(english_word_list)
#     random_french_word = random.choice(french_word_list)
#     print(random_english_word)
#     print(english_word_list.index(random_english_word))
#     time.sleep(3)
#     print(french_word_list[english_word_list.index(random_english_word)])
#     print(french_word_list.index(french_word_list[english_word_list.index(random_english_word)]))
    
    
    
    
# find_word_meaning()

#------------------------------------------------------DATA READING----------------------------------------#
def english_word_finder():
    english_word_dataframe = pandas.read_csv("./data/french_words.csv") 
    english_word_list = english_word_dataframe["English"].tolist()
    french_word_list = english_word_dataframe["French"].tolist()
    random_english_word = random.choice(english_word_list)
    canvas.itemconfig(card_title, text="English")
    canvas.itemconfig(card_word, text=f"{random_english_word}")
    random_word_index = english_word_list.index(random_english_word)
    print(random_word_index)
    print(english_word_list[random_word_index])
    
    # canvas.itemconfig(word, text=random_english_word)
    
    
    corresponding_french_word = french_word_list[random_word_index]
    print(corresponding_french_word)
    print(french_word_list.index(corresponding_french_word))
    
    
    time.sleep(3)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=corresponding_french_word)
    # this for updating word to english
    # canvas.itemconfig(word, text=random_english_word)
    # canvas.itemconfig(title, text="English")
    
# english_word_finder()
  
def french_word_finder():
    french_word_dateframe = pandas.read_csv("./data/french_words.csv")
    french_word_list = french_word_dateframe["French"].tolist()
    english_word_list = french_word_dateframe["English"].tolist()
    random_french_word = random.choice(french_word_list)
    random_word_index = french_word_list.index(random_french_word)

    # this for updating word to french
    # canvas.itemconfig(word, text=random_french_word)
    # canvas.itemconfig(title, text="French")
    
# french_word_finder()

# def next_card():
#     global current_card
#     current_card = random.choice(to_learn)
#     canvas.itemconfig(title, text="French")
#     canvas.itemconfig(word, text=current_card["French"])

# def flip_card():
#     # global current_card
#     # current_card = random.choice(to_learn)
#     canvas.itemconfig(title, text="English")
#     canvas.itemconfig(word, text=current_card["English"])
#     # canvas.itemconfig(card_background, image=card_back_img)
    
    
#-----------------------------------------------------UI STYLE----------------------------------------------#
window = Tk()
window.title("Flashy Game")
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)
window.after(3000, func=french_word_finder)

canvas = Canvas(width=1000, height=526)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(500, 270, image=card_front_img)
card_title = canvas.create_text(500, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(500, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)



button_right_img = PhotoImage(file="./images/right.png")
button_right = Button(image=button_right_img, highlightthickness=0, command=english_word_finder)
button_right.grid(column=1, row=1, pady=48)


button_wrong_img = PhotoImage(file="./images/wrong.png")
button_wrong = Button(image=button_wrong_img, highlightthickness=0)
button_wrong.grid(column=0, row=1, pady=48)






window.mainloop()
