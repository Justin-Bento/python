"""
- [x] Random function: to generate rock, paper, or scissors. 
- [x] Valid function: to check the validity of the move.
- [x] Result function: to declare the winner of the round.
- [] Scorekeeper: to keep track of the score.
"""

# Imported randomint package from random module.
from random import randint

# Assigned global variables to be used inside multipule functions.
global options
global computer
global player


def game_logic():
  
  # Created a list of options that a computer and user can play.
  options = ["Rock", "Paper", "Scissors"]

  # Assigns a random number between 0 and 2 for the computer to play the game options.
  computer = options[randint(0,2)]

  # Set player to False
  player = False

  while player == False:
  #set player to True
      # If a player option types in Rock, Paper or Scissors this logic will determin who wins or looses if a user types in anything else the loop will close.
      player = input("Rock, Paper, Scissors?")
      if player == computer:
          print("Tie!")
      elif player == "Rock":
          if computer == "Paper":
              print("You lose!", computer, "covers", player)
          else:
              print("You win!", player, "smashes", computer)
      elif player == "Paper":
          if computer == "Scissors":
              print("You lose!", computer, "cut", player)
          else:
              print("You win!", player, "covers", computer)
      elif player == "Scissors":
          if computer == "Rock":
              print("You lose...", computer, "smashes", player)
          else:
              print("You win!", player, "cut", computer)
      else:
          print("That's not a valid play. Check your spelling!")
          break
      player = False
      computer = options[randint(0,2)]
game_logic()