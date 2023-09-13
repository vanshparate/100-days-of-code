from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pandas.read_csv("data/German - English.csv")
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')


def next_card():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="German", fill='black')
    canvas.itemconfig(card_text, text=current_card['German'], fill='black')
    canvas.itemconfig(card_background, image=card_front_image)
    flip_timer = window.after(3000, func=card_back)


def card_back():
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_text, text=current_card['English'], fill='white')
    canvas.itemconfig(card_background, image=card_back_image)


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=card_back)
canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, text="", font=('Ariel', 40, 'italic'))
card_text = canvas.create_text(400, 263, text="", font=('Ariel', 60, 'bold'))
# canvas.create_image(400, 263, image=card_back_image)

canvas.grid(row=0, column=0, columnspan=2)

right = PhotoImage(file='images/right.png')
wrong = PhotoImage(file='images/wrong.png')
right_button = Button(image=right, highlightthickness=0, command=is_known)
wrong_button = Button(image=wrong, highlightthickness=0, command=next_card)
right_button.grid(row=1, column=1)
wrong_button.grid(row=1, column=0)

next_card()
window.mainloop()