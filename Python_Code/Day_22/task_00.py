from tkinter import *

#create a window
window = Tk()
window.title("Unit Converter") 
window.minsize(width=500, height=300)
 

def button_clicked_command():
    label["text"] = entry_input.get()


 #Lebel
label = Label(text="Hey hello", font=("Courier", 32, "bold"), height=2, width=12, bg="lightblue")
# label.pack() # problem with pack this is visible like stack
#label.place(x=200, y=300)   ##problem with place this so specific need to remember coordinates
label["text"] = "New text"  
label.grid(column=0, row=0) 
label.config(padx=24, pady=24)

#Entry 
entry_input = Entry(width=24)
# entry_input.pack()    # problem with pack this is visible like stack
#entry_input.place(x=400, y=500) ##problem with place this so specific need to remember coordinates
entry_input.grid(column=2, row=3)
# entry_input.config(padx=24, pady=24)


#Button
button = Button(text="Click Me", font=("Courier", 12, "bold"), command=button_clicked_command)
# button.pack() # problem with pack this is visible like stack
#button.place(x=100, y=200)  #problem with place this so specific need to remember coordinates
button.grid(column=1, row=4)
button.config(padx=24, pady=12)



 
# hold window 
window.mainloop()