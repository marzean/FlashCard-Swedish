from tkinter import *
import pandas as pd
import random
BG_COLOR = "#B1DDC6"
word_list = []
random_swedish_word = {}


"""Reading the csv file and check if unknown words are available"""
try:
    df = pd.read_csv("data/unknown_words.csv")
except FileNotFoundError:
    initial_words = pd.read_csv("data/Swedish_words.csv")
    word_list = initial_words.to_dict(orient="records")
else:
    word_list = df.to_dict(orient="records")

"""Generate the random swedish word"""


def generate_swedish():
    global random_swedish_word, translate_time
    window.after_cancel(translate_time)
    random_swedish_word = random.choice(word_list)
    new_word = random_swedish_word["Swedish"]
    canvas.itemconfig(title_word, text="Swedish", fill="Blue")
    canvas.itemconfig(swedish_word, text=new_word)
    canvas.itemconfig(card_front, image=front_image)
    translate_time = window.after(3000, generate_english)


"""Show the english meaning of the word"""


def generate_english():
    canvas.itemconfig(title_word, text="English", fill="Red")
    canvas.itemconfig(swedish_word, text=random_swedish_word["in English"])
    canvas.itemconfig(card_front, image=back_image)


"""Remove the known word"""

def remove_word():
    word_list.remove(random_swedish_word)
    new_list = pd.DataFrame(word_list)
    new_list.to_csv("data/unknown_words.csv", index=False)
    generate_swedish()


"""Setting up the user interface"""

window = Tk()
window.title("Swedish Flashcard")
window.config(padx=50, pady=50, bg=BG_COLOR)
translate_time = window.after(3000, generate_english)


"""fixing the image and text for the words"""
canvas = Canvas(width=800, height=526)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
card_front = canvas.create_image(400, 263, image=front_image)
title_word = canvas.create_text(400, 150, text="", font=("Ariel", 34, "italic"))
swedish_word = canvas.create_text(400, 263, text="", font=("Ariel", 45, "bold"))
canvas.config(bg=BG_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

"""buttons"""
cancel_image = PhotoImage(file="images/wrong.png")
learn_again_word = Button(image=cancel_image, highlightthickness=0, command=generate_swedish)
learn_again_word.grid(row=1, column=0)
right_image = PhotoImage(file="images/right.png")
learned_word = Button(image=right_image, highlightthickness=0, command=remove_word)
learned_word.grid(row=1, column=1)

"""calling the generate swedish function for initial swedish word"""
generate_swedish()
window.mainloop()