from tkinter import *
import task_01
import pyperclip

ENTRY_FONT = ("Roboto", 14, "normal")
ENTRY_BACKGROUND = "white"
ENTRY_WIDTH = 35
PASSWD_WIDTH = 21
BUTTON_FONT = ("Roboto", 14, "normal")

#--------------------------------------------PASSWORD GENERATOR-----------------------------------#
def generated_password():
    passwd_entry.insert(0, f"{task_01.passwd}")
    pyperclip.copy(task_01.passwd)
    pyperclip.paste()
    
#----------------------------------------------SAVE PASSWORD--------------------------------------#
def add_passwd():
    with open(file="password_copy.txt", mode="a") as passwd_file:
        passwd_file.write(f"{web_entry.get()} | {email_entry.get()} | {passwd_entry.get()}\n")
    
    
#-----------------------------------------------UI STYLE---------------------------------------------#
window = Tk()
window.title("Password Generator")
window.minsize(width=500, height=500)
window.config(bg="white", padx=50, pady=20)

canvas = Canvas(width=200, height=200, bg=ENTRY_BACKGROUND, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0, padx=100, pady=100)

#Create website entry and Label
web_label = Label(text="Website: ", bg=ENTRY_BACKGROUND, font=ENTRY_FONT, highlightthickness=0)
web_label.grid(column=0, row=1, pady=12)

web_entry = Entry(width=35, highlightcolor="#87CEEB", highlightthickness=2)
web_entry.grid(column=1, row=1, pady=12, columnspan=2)

#Create Email entry and Label
email_label = Label(text="Email/Username: ", bg=ENTRY_BACKGROUND, font=ENTRY_FONT, highlightthickness=0)
email_label.grid(column=0, row=2, pady=12)

email_entry = Entry(width=35, highlightcolor="#87CEEB", highlightthickness=2)
email_entry.grid(column=1, row=2, pady=12, columnspan=2)

# Create password generate entry and Label
passwd_label = Label(text="Password: ", bg=ENTRY_BACKGROUND, font=ENTRY_FONT, highlightthickness=0)
passwd_label.grid(column=0, row=3,  pady=12)



passwd_entry = Entry(window, textvariable=StringVar(), width=21, highlightcolor="#87CEEB", highlightthickness=2)
passwd_entry.grid(column=1, row=3,  pady=12)

#Create password Generate Button
passwd_button = Button(text="Generate Password", command=generated_password, highlightthickness=0, bg="#87CEEB", font=BUTTON_FONT)
passwd_button.grid(column=2, row=3, pady=12)

#Create add Button
add_button = Button(text="Add", font=BUTTON_FONT, bg="black", fg="white", width=36, command=add_passwd)
add_button.grid(column=1, row=4, columnspan=2, pady=32)





window.mainloop()