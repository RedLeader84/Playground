import random

def get_choices():
  player_choice = input("Enter a choice (rock, paper, scissors: ")
  options = ["paper", "rock", "scissors"]
  computer_choice = random.choice(options)
  choices = {"player": player_choice, "computer": computer_choice}
  return choices

def check_win(player, computer):
  print(f"you chose {player}, computer chose {computer}")
  if player == computer:
    return "It's a tie!"

check_win("rock", "paper")