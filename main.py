#Build on replit.com

import random
from art import logo
from replit import clear

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

is_playing = True



def handle_ace(hand):
  have_ace = False

  for card in hand:
    if card ==11:
      have_ace= True
      ace_index= hand.index(11)
  
  if have_ace:
    hand.pop(ace_index)
    hand.append(1)
    player_sum = sum(hand)

  else:
    player_sum= sum(hand)

  return player_sum

def get_result(player_sum,computer_sum):
  #Tabulate result
  if computer_sum <=21:
    if player_sum <=21 and player_sum>computer_sum:
      print("You win")
    elif player_sum <=21 and player_sum <computer_sum:
      print("You lose")
    elif player_sum<=21 and player_sum == computer_sum:
      print("Draw")
    else:
      print("You lose")

  else:
    if player_sum >21:
      print("Draw")
    else:
      print("You win")



player_choice = input("Do you want to start a game of blackjack? 'y' or 'n'").lower()

if player_choice=='n':
  print("Thank you for playing with us")
  is_playing = False

while is_playing:

  keep_drawing = True
  player_hand=[]
  computer_hand = []
  clear()

  player_hand= random.choices(cards, k=2)
  player_sum = sum(player_hand)

  computer_hand=random.choices(cards, k=2)
  computer_sum=sum(computer_hand)
  computer_first_card = computer_hand[0]

  while computer_sum< 17:
    computer_card = random.choice(cards)
    computer_hand.append(computer_card)
    computer_sum= sum(computer_hand)
    

  #Display#

  print(logo)

  print(f"Your cards are {player_hand}, current score is {player_sum}.")
  print(f"Computer first card is {computer_first_card}.")

  
  while keep_drawing:
    if player_sum<21:
      player_choice2= input("Do you wish to take another card?'y' or 'n' ").lower()
      if player_choice2 == 'y':
      
        player_card = random.choice(cards)
        player_hand.append(player_card)
        
        player_sum= handle_ace(player_hand)
      
        print(f"Your cards are {player_hand}, current score is {player_sum}.")
        print(f"Computer first card is {computer_first_card}." )

      else:
        keep_drawing = False
    else:
      keep_drawing=False
  
  print(f"Your final hand: {player_hand}, Sum is {player_sum}")
  print(f"Computer's final hand is {computer_hand}, Sum is {computer_sum} ")

  get_result(player_sum,computer_sum)
  

  player_choice = input("Do you want to start a game of blackjack? 'y' or 'n'").lower()

  if player_choice=='n':
    print("Thank you for playing with us")
    is_playing = False
