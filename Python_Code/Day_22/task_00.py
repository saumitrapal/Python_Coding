from tkinter import *

window = Tk()
window.title("Unit Converter") 
window.minsize(width=500, height=300)   #window minimum size
 

#Lebel
label = Label(text="Hey hello", font=("Courier", 32, "bold"), height=2, width=12, bg="lightblue")
label.pack() 
label["text"] = "New text"


#Entry 
entry_input = Entry(width=24)
entry_input.pack()

def button_clicked_command():
    label["text"] = entry_input.get()

#Button
button = Button(text="Click Me", height=2, width=12, font=("Courier", 12, "bold"), command=button_clicked_command)
button.pack()


 

# hold window 
window.mainloop()