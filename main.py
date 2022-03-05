#Number Guessing Game
import random
import art

def difficulty(hardness):
  """set how many lives the player starts with"""
  if hardness == "easy":
    lives = 10
  elif hardness == "hard":
    lives = 5
  return lives

def game():
  print(art.logo)
  print("Welcome to the Number Guessing Game!")
  print("I am thinking of a number between 1 and 100.")
  chosen_number = random.randint(1, 100) #sets a random number
  level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

  lives_remaining = difficulty(level) #call the difficulty function to define how many lives player starts with
  print(chosen_number)
  winner = False

  while lives_remaining > 0 and winner == False:
    print(f"You have {lives_remaining} attempts remaining to guess the correct the number.")
    guess = int(input("Guess a number: "))

    if guess == chosen_number:
      winner = True
    elif guess > chosen_number:
      print("You guessed too high. \n Try again.")
      lives_remaining -= 1
    elif guess < chosen_number:
      print("You guessed too low. \n Try again.")
      lives_remaining -= 1

    if lives_remaining == 0:
      winner = False

  if winner == True:
    print(f"Congrats you won with {lives_remaining -1} remaining gueses! The correct answer was {chosen_number}")
  elif winner == False:
    print(f"Sorry you ran out of gueses, you loose! The correct answer was {chosen_number}")

while input("Do you want to play the Number Guessing Game? 'y' or 'n': ").lower() == "y":
  game()

