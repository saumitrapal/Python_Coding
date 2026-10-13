from tkinter import *

FONT = ("Courier", 12, "bold")

#Create a window
window = Tk()
window.title("Mile To Kilometer Converter")
window.minsize(width=500, height=500)
    
# Create a Lable for sentence -> "ENter mile"
label = Label(text="Enter mile")
label.grid(column=0, row=0)

#Create a feild
input_entry = Entry(width=20)
input_entry.grid(column=1, row=0)
input_entry.focus_set()

#Create a Label for sentence -> "is equal to"
equal_label = Label(text="Miles is equal to:")
equal_label.grid(column=0, row=1)
equal_label.config(padx=24, pady=24)

#Create a Label for sentence -> "converter number"
converter_number = Label(text=0)
converter_number.grid(column=1, row=1)

#Create a Label for word -> "km"
km_word = Label(text="km")
km_word.grid(column=2, row=1)

#Create a fn number that change converter number 
def conversion():
    """
    this function take input from input_entry with get() method as string type convert into following calculation
    """
    number = input_entry.get()
    converter = float(number) * 1.609344
    converter_number["text"] = round(converter, 5)

# Create a Button
button = Button(text="Convert", command=conversion, font=FONT)
button.grid(column=1, row=3)
button.config(padx=24, pady=8)


#Hold window
window.mainloop()