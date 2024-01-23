import itertools
import random
from replit import clear
from art import logo





def print_screen():
  print(logo)

  
def play_game():
  print_screen()

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()
