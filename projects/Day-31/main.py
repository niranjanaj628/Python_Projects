from tkinter import *
import pandas as pd
from random import choice

BACKGROUND_COLOR = "#B1DDC6"

try:
    df= pd.read_csv('Python_Projects/projects/Day-31/data/words_to_learn.csv')
except FileNotFoundError:
    df= pd.read_csv('Python_Projects/projects/Day-31/data/Malayalam_words.csv')
data = df.to_dict(orient= 'records')
current_word={}

def generate_word():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = choice(data)
    canvas.itemconfig(language, text='Malayalam', fill='black')
    canvas.itemconfig(word, text=current_word['Malayalam'], fill='black')
    canvas.itemconfig(card_bg, image = front_image)   
    flip_timer = window.after(3000,func=flip_card ) 
    
def flip_card():
    canvas.itemconfig(language, text='English', fill='white')
    canvas.itemconfig(word, text=current_word['English'], fill='white')
    canvas.itemconfig(card_bg, image = back_image)
    
def remove_word():
    data.remove(current_word)
    unknown = pd.DataFrame(data)
    unknown.to_csv('Python_Projects/projects/Day-31/data/words_to_learn.csv')
    generate_word()
    
window= Tk()
window.title('Flash cards')
window.config(padx=50, pady= 50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000,func=flip_card )


canvas= Canvas(width=800, height=526)
front_image= PhotoImage(file='Python_Projects/projects/Day-31/images/card_front.png')
back_image= PhotoImage(file='Python_Projects/projects/Day-31/images/card_back.png')
card_bg = canvas.create_image(400, 263, image= front_image)
language = canvas.create_text(400, 150, text='Language', font=('Ariel', 40, 'italic'))
word = canvas.create_text(400, 263, text='Word', font=('Ariel', 50, 'bold'))
canvas.config(bg= BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2, rowspan=2)

right_img=PhotoImage(file='Python_Projects/projects/Day-31/images/right.png')
wrong_img= PhotoImage(file='Python_Projects/projects/Day-31/images/wrong.png')

right_btn= Button(image=right_img, highlightthickness=0, bg='white', command=remove_word)
right_btn.grid(column=1, row= 1)

wrong_btn = Button(image=wrong_img, highlightthickness=0, bg='white', command=generate_word)
wrong_btn.grid(column= 0, row= 1)

generate_word()

window.mainloop()

