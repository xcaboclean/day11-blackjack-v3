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


def print_baseboard(deck):
  print(f"\n┌───────────────┐\n│{len(deck):03}🃏🎴 card(s)│\n└───────────────┘")

def print_screen(deck):
  clear()
  print(logo)
  print_baseboard(deck)

  
def play_game(deck):
  print_screen(deck)


#**************
#**************
#Start Program
#**************  print_screen()
#**************
hand_player = []
hand_dealer = []
end_game = False
deck = create_deck()

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game(deck)
