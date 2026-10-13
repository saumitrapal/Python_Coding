from tkinter import *
import task_05
import pyperclip
from tkinter import messagebox
import json


ENTRY_FONT = ("Roboto", 14, "normal")
ENTRY_BACKGROUND = "white"
ENTRY_WIDTH = 35
PASSWD_WIDTH = 21
BUTTON_FONT = ("Roboto", 14, "normal")

#---------------------------------------------SEARCH BUTTON FUNCTION------------------------------#
def search_function():
    web_name = web_entry.get()
    
    try:
        with open(file="data.json", mode="r") as date_file:
            file_data = json.load(date_file)  
            if web_name in file_data:
                email_data = file_data[web_name]["email"]
                password_data = file_data[web_name]["password"]
                messagebox.showinfo(title=f"{web_name}", message=f"Here is your {web_name} Email: {email_data}\n Password: {password_data}")
    except FileNotFoundError:
        messagebox.showerror(title="Error!", message=f"File not found!")
    except KeyError:
        messagebox.showwarning(title="Error!", message=f"Your {web_name} haven't any information. Please create one")

    with open(file="data.json", mode="r") as date_file:
            file_data = list(json.load(date_file))
            if web_name not in file_data:
                messagebox.showerror(title=f"{web_name}", message=f"No detail for {web_name} exist")
                
    
            
    # if web_name not in file_data[web_name]:
    #     messagebox.showerror(title=f"{web_name} Information", message=f"Your {web_name} information not found! please check your website name.")
            
#--------------------------------------------PASSWORD GENERATOR-----------------------------------#
def generated_password():
    passwd_entry.insert(0, f"{task_05.passwd}")
    pyperclip.copy(task_05.passwd)
    pyperclip.paste()
    
#----------------------------------------------SAVE PASSWORD--------------------------------------#
def add_passwd():
    new_data = {
        web_entry.get(): {
            "email": email_entry.get(),
            "password": passwd_entry.get(),
        }
    }
    
    if len(web_entry.get()) == 0 or len(passwd_entry.get()) == 0:
        messagebox.showinfo(title="Oops", message="Please Verify Your Email, Password, Website Field Non Empty.")
    else:  
        try:
            with open(file="data.json", mode="r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open(file="data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open(file="data.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            web_entry.delete(0, END)
            passwd_entry.delete(0, END)
        
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
web_entry.focus_set()

#Create Email entry and Label
email_label = Label(text="Email/Username: ", bg=ENTRY_BACKGROUND, font=ENTRY_FONT, highlightthickness=0)
email_label.grid(column=0, row=2, pady=12)

email_entry = Entry(width=35, highlightcolor="#87CEEB", highlightthickness=2)
email_entry.grid(column=1, row=2, pady=12, columnspan=2)
email_entry.insert(0, string="abc@gmail.com")

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

#Create a search button
search_button = Button(text="Search", font=BUTTON_FONT, command=search_function, width=0)
search_button.grid(column=2, row=1, columnspan=2)


window.mainloop()