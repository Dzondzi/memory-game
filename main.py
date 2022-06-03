from tkinter import *
import random
import time

opened = False
last_opened_card = None
left_pairs = 12

# init Tk game instance
game = Tk()
game.title("Memory game")
game.geometry("900x600")

play_area = Frame(game, width=300, height=300, bg="white")

# loading required images
back_image = PhotoImage(file="images/back.png")
card_images = []
for i in range(12):
    card_images.append(PhotoImage(file=f"images/image{i}.png"))


class Card:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.value = None
        self.button = Button(
            play_area,
            image=back_image,
            width=100,
            height=100,
            command=lambda: on_button_clicked(self),
        )
        self.button.grid(row=x, column=y)

    def set_value(self, value):
        self.value = value


def init_game():
    global opened
    global last_opened_card
    global left_pairs
    opened = False
    last_opened_card = None
    left_pairs = 12
    cards = []
    for x in range(0, 4):
        for y in range(0, 6):
            card = Card(x, y)
            cards.append(card)
    set_values(cards)


def open_card(card):
    card.button = Button(
        play_area,
        image=card_images[card.value],
        width=100,
        height=100,
    )
    card.button.grid(row=card.x, column=card.y)
    play_area.pack(pady=50, padx=0)
    # without this table doesnt update instantly
    Tk.update(game)


def close_card(card):
    card.button = Button(
        play_area,
        image=back_image,
        width=100,
        height=100,
        command=lambda: on_button_clicked(card),
    )
    card.button.grid(row=card.x, column=card.y)
    play_area.pack(pady=50, padx=0)


def on_button_clicked(card: Card):
    global opened
    global last_opened_card
    global left_pairs
    global result_label

    open_card(card)

    if opened:
        time.sleep(1)
        if card.value == last_opened_card.value and last_opened_card != card:
            left_pairs -= 1
            if left_pairs == 0:
                print("Game ended")
        else:
            close_card(card)
            close_card(last_opened_card)
        opened = False
        last_opened_card = None
    else:
        opened = True
        last_opened_card = card
    return


def set_values(cards):
    card_values = [i for i in range(12)]
    card_values = card_values * 2
    random.shuffle(card_values)
    for i, card in enumerate(cards):
        card.set_value(card_values[i])


reset_button = Button(game, text="New game", pady=10, command=lambda: init_game())
init_game()
reset_button.pack()
play_area.pack(pady=50, padx=0)

game.mainloop()
