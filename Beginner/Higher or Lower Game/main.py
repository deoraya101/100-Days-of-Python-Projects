import random
import art
from game_data import data

score = 0

def higher_followers(a, b):
    if a > b:
        higher = "A"
        print(f"test: A")
    else:
        higher = "B"
        print(f"test: B")
    return higher

def check_guess(a, b):
    global score

    answer = higher_followers(a, b)

    user_guess = input("Who has more followers? Type 'A' or 'B': ").upper()
    if user_guess == answer:
        score += 1
        return True
    else:
        return False

def set_up_compare():
    data_size = len(data)
    compare_a = random.randint(0, data_size - 1)
    followers_a = data[compare_a]['follower_count']
    print(f"Compare A: {data[compare_a]['name']}, a {data[compare_a]['description']}, from {data[compare_a]['country']}")

    print(art.vs)

    compare_b = random.randint(0, data_size)
    followers_b = data[compare_b]['follower_count']
    print(f"Compare B: {data[compare_b]['name']}, a {data[compare_b]['description']}, from {data[compare_b]['country']}")

    return [followers_a, followers_b]

def start():
    global score
    again = True
    while again:
        print("\n" * 10)
        print(art.logo)
        if score != 0:
            print(f"Your right! Current score: {score}.")
        followers = set_up_compare()
        again = check_guess(followers[0], followers[1])
    print(f"{"\n" * 10}{art.logo}\nSorry that's wrong. Final Score: {score}")

start()
