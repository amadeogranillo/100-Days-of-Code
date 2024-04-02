from tkinter import *
import pandas as pd
import random

import pandas.errors

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
word_dict = {}

try:
    df = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    word_dict = original_data.to_dict(orient="records")
except pandas.errors.EmptyDataError:
    print("No more words to learn")
else:
    word_dict = df.to_dict(orient="records")



def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(word_dict)
    canvas.itemconfig(card_title, text = "French", fill = "black")
    canvas.itemconfig(card_text, text = current_card["French"],fill = "black")
    canvas.itemconfig(card_background, image = card_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text = "English", fill ="white")
    canvas.itemconfig(card_text, text=current_card["English"], fill ="white")
    canvas.itemconfig(card_background, image=card_back)

def is_known():
    try:
        word_dict.remove(current_card)
    except ValueError:
        print("No more words to learn")
    else:
        print(len(word_dict))
        data = pd.DataFrame(word_dict)
        data.to_csv("data/words_to_learn.csv", index=False)
    try:
        next_card()
    except IndexError:
        print("No more words to learn")

window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)


canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400,263, image = card_front)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness = 0)
card_title = canvas.create_text(400, 150, font=("Ariel", 40, "italic"))
card_text = canvas.create_text(400, 263, font=("Ariel", 60, "bold"))
canvas.grid(column =0, row = 0, columnspan = 2)

right_image = PhotoImage(file="images/right.png")
correct_button = Button(image=right_image,highlightthickness = 0, command=is_known)
correct_button.grid(column=1, row=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness = 0, command=next_card)
wrong_button.grid(column=0, row=1)

try:
    next_card()
except KeyError:
    print("")


window.mainloop()