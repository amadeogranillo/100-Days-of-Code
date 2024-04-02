from tkinter import *


def button_clicked():
    miles = float(input.get())
    conversion = round(miles * 1.609)
    conversion_label.config(text= f"{conversion}")


window = Tk()
window.title("Miles to Km Converter")
#Padding
window.config(padx=20, pady=20)

input = Entry(width = 7)
input.grid(column=1, row=0)

miles_label = Label(text="Miles", font=("Arial", 12, "normal"))
miles_label.grid(column=2, row=0)

equal_label = Label(text="Is equal to", font=("Arial", 12, "normal"))
equal_label.grid(column=0, row=1)

conversion_label = Label(text= "0", font=("Arial", 12, "normal"))
conversion_label.grid(column=1, row=1)

km_label = Label(text="Km", font=("Arial", 12, "normal"))
km_label.grid(column=2, row=1)

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)


window.mainloop()