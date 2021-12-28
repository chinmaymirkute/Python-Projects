#Number Guessing using python code
#Coded by - Chinmay Mirkute
#You can find me on Linkedin: Chinmay Mirkute
#                   Twitter: mirkute_chinmay
#                   Instagram: chinmaymirkute


from random import randint
from asciiart import logo

easy_level = 10
hard_level = 5


def test_solution(guess, answer, turns_left):

  if guess > answer:
    print("Oops !!! you entered greater number than expected.")
    return turns_left - 1
  elif guess < answer:
    print("Oops !!! you entered greater number than expected.")
    return turns_left - 1
  else:
    print(f"Congratulations, You've nailed it . The Answer is {answer}.")


def difficulty():
  level = input("Please select the level of game by Typing 'easy' or 'hard': \n")
  if level == "easy":
    return easy_level
  else:
    return hard_level

def game():
  print(logo)
  print("Hey Guys !!! \n Welcome to the Number Guessing \n")
  print("There can be any number between 1 to 50 , lets see what you guess ☻.\n")
  answer = randint(1, 51)
  #print(f"Hint : approx answer is {answer} \n")

  turns = difficulty()

  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining think carefully.")


    guess = int(input("Guess the number: "))


    turns = test_solution(guess, answer, turns)
    if turns == 0:
      print("Oops, You've not entered correct number in given attempts 😔 \n YOU LOSE.")
      return
    elif guess != answer:
      print("Try Guessing again.")


game()

