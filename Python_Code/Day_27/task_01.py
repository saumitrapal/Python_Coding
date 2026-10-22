import requests
from tkinter import *

"""
this project is about kanye weste questo. That project teaches how to use api and how to call api to get answer.
api: https://api.kanye.rest
"""

# Quotes fn create quotes
def kanye_quotes():
    responce = requests.get(url="https://api.kanye.rest")
    data = responce.json()
    quote = data["quote"]
    canvas.itemconfig(quote_text, text=quote)


window = Tk()
window.title("Kanye Quotes")

#Create canvas
canvas = Canvas(window, width=500, height=500)
back_image = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=back_image)
quote_text = canvas.create_text(150, 207, text="Kanye quotes here", width=250, font=("Roboto", 30, "normal"), fill="white")
canvas.grid(column=0, row=0)

# Create button
kanye_image = PhotoImage(file="kanye.png")
quote_button = Button(image=kanye_image, command=kanye_quotes)
quote_button.grid(column=0, row=1, pady=100)

window.mainloop()
