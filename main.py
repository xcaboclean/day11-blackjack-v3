import itertools
import random
from replit import clear
from art import logo

def drawn_card(deck):
  if not deck:
      print("Empty deck")
      return None
  else:
      return deck.pop()

#Print one card

def print_card(card, lines):
    lines[0] = lines[0] + " " + "┌───┐"
    if card['value_card'] == '10':
        lines[1] = lines[1] + " " + f"│{card['value_card']} │"
        lines[2] = lines[2] + " " + f"│ {card['suit']} │"
    else:
        lines[1] = lines[1] + " " + f"│ {card['value_card']} │"
        lines[2] = lines[2] + " " + f"│ {card['suit']} │"

    lines[3] = lines[3] + " " + "└───┘"
    
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

def print_hands(player, dealer):
  print("\nDealer hand:")
  lines = [" ", " ", " ", " "]
  
  print("\nPlayer hand:")
  lines = [" ", " ", " ", " "]

  
  

def print_baseboard(deck):
  print(f"\n┌───────────────┐\n│{len(deck):03}🃏🎴 card(s)│\n└───────────────┘")

def print_screen(deck, player, dealer):
  clear()
  print(logo)
  print_baseboard(deck)

  
def play_game(deck, hand_player, hand_dealer):
  print_screen(deck, hand_player, hand_dealer)


#**************
#**************
#Start Program
#**************  print_screen()
#**************
hand_player = []
hand_dealer = []
end_game = False
deck = create_deck()
#Shuffle Deck
random.shuffle(deck)
phase_dealer = 0
phase_player = 0


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game(deck, hand_player, hand_dealer)
