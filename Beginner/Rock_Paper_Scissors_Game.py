import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

images = [rock, paper, scissors]

print("Welcome to Rock, Paper, Scissors game! ")

userChoice = int(input("What's your choice? Type 0 for Rock, 1 for Paper, and 2 for Scissors. "))
print("Your move: ")
print(images[userChoice])

compChoice = random.randint(0,2)
print("Computer's move: ")
print(images[compChoice])

if userChoice == 0:
    if compChoice == 0:
        print("Tie.")
    elif compChoice == 1:
        print("You Lose. ")
    elif compChoice == 2:
        print("You Win!")
if userChoice == 1:
    if compChoice == 0:
        print("You Win!")
    elif compChoice == 1:
        print("Tie.")
    elif compChoice == 2:
        print("You Lose. ")
if userChoice == 2:
    if compChoice == 0:
        print("You Lose.")
    elif compChoice == 1:
        print("You Lose.")
    elif compChoice == 2:
        print("Tie.")
