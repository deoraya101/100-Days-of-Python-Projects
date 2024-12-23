import random
import art

def guess(num):
    a = num
    pc_num = random.randint(1,100)
    print(f"testing: {pc_num}")
    while a > 0:
        print(f"You have {a} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        if user_guess != pc_num:
            if user_guess > pc_num:
                print("Too High.")
            else:
                print("Too Low.")
            a -= 1

            if a != 0:
                print("Guess Again.")
        else:
            print(f"You got it! The answer was {pc_num}")

    print("You've run out of guesses, you lose.")

def start():
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        attempts = 10
    else:
        attempts = 5

    guess(attempts)

start()
