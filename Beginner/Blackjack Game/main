import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def card_deal():
    player_cards = []
    dealer_cards = []

    player_total = 0
    dealer_total = 0

    while len(player_cards) < 2:
        player_cards.append(random.choice(cards))
    for i in player_cards:
        player_total += i
    print(f"Your cards: {player_cards}, current score: {player_total}")

    while len(dealer_cards) < 2:
        dealer_cards.append(random.choice(cards))
    for i in dealer_cards:
        dealer_total += i
    while dealer_total <= 16:
        dealer_cards.append(random.choice(cards))
        dealer_total += dealer_cards[-1]
    print(f"Computer's first card: {dealer_cards[0]}")

    while player_total < 21:
        add_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if add_card == "y":
            player_cards.append(random.choice(cards))
            player_total += player_cards[-1]
            print(f"Your cards: {player_cards}, current score: {player_total}")
            print(f"Computer's first card: {dealer_cards[0]}")
        else:
            break

    print(f"Your final hand: {player_cards}, final score: {player_total}")
    print(f"Computer's final hand: {dealer_cards}, final score: {dealer_total}")
    print(blackjack(player_total, dealer_total))
    return


def blackjack(p_total, d_total):
    if p_total == d_total:
        return "Your numbers are the same. Its a draw!"
    elif p_total > d_total:
        if p_total == 21:
            return "You have blackjack! You win!"
        elif p_total > 21:
            return "You went over. You lose!"
        else:
            return "You have a higher score. You win!"
    else:
        if d_total == 21:
            return "Computer has blackjack! You lose!"
        elif d_total > 21:
            return "Computer went over. You Win!"
        else:
            return "Computer has a higher score. You lose!"


start = True
while start:
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if play == "y":
        print("\n" * 30)
        print(art.logo)
        card_deal()
    else:
        start = False
        print("Goodbye!")

