from art import logo
print(logo)

bid_list = {}

def find_winner():
    winner = 0
    for i in bid_list:
        if bid_list[i] > winner:
            winner = bid_list[i]
            winner_name = i
    print(f"The winner is {winner_name} with a bid of ${bid_list[winner_name]}")

def add_person():
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bid_list[name] = bid
    yes_or_no = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if yes_or_no == "yes":
        print("\n" * 20)
        add_person()
    else:
        print("\n" * 5)
        find_winner()

add_person()
