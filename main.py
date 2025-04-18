from tkinter import *
import requests
from pprint import pprint
import os


def get_quote():
    response = requests.get(url="https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()['quote']
    canvas.itemconfig(quote_text, text=data)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file=os.path.join(BASE_DIR, "assets/background.png"))
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Believe in your flyness...conquer your shyness.", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file=os.path.join(BASE_DIR, "assets/kanye.png"))
kanye_button = Button(image=kanye_img, highlightthickness=0, borderwidth=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()
