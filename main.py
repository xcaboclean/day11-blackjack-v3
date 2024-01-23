import itertools
import random
from replit import clear
from art import logo


def create_deck():
suits = ["♠️", "♣️", "♥️", "♦️", "♠️", "♣️", "♥️", "♦️"]
values_cards = [
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    '10',
    'J',
    'Q',
    'K',
    'A',
]
return [{
    'value_card': value_card,
    'suit': suit
} for value_card, suit in itertools.product(values_cards, suits)]




def print_screen():
  print(logo)

  
def play_game():
  print_screen()

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()
