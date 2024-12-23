MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

money = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

logo = r"""
    _______      ,-----.     ________  ________     .-''-.      .-''-.             
   /   __  \   .'  .-,  '.  |        ||        |  .'_ _   \   .'_ _   \            
  | ,_/  \__) / ,-.|  \ _ \ |   .----'|   .----' / ( ` )   ' / ( ` )   '           
,-./  )      ;  \  '_ /  | :|  _|____ |  _|____ . (_ o _)  |. (_ o _)  |           
\  '_ '`)    |  _`,/ \ _/  ||_( )_   ||_( )_   ||  (_,_)___||  (_,_)___|           
 > (_)  )  __: (  '\_/ \   ;(_ o._)__|(_ o._)__|'  \   .---.'  \   .---.           
(  .  .-'_/  )\ `"/  \  ) / |(_,_)    |(_,_)     \  `-'    / \  `-'    /           
 `-'`-'     /  '. \_/``".'  |   |     |   |       \       /   \       /            
   `._____.'     '-----'    '---'     '---'        `'-..-'     `'-..-'             
,---.    ,---.   ____        _______   .---.  .---..-./`) ,---.   .--.    .-''-.   
|    \  /    | .'  __ `.    /   __  \  |   |  |_ _|\ .-.')|    \  |  |  .'_ _   \  
|  ,  \/  ,  |/   '  \  \  | ,_/  \__) |   |  ( ' )/ `-' \|  ,  \ |  | / ( ` )   ' 
|  |\_   /|  ||___|  /  |,-./  )       |   '-(_{;}_)`-'`"`|  |\_ \|  |. (_ o _)  | 
|  _( )_/ |  |   _.-`   |\  '_ '`)     |      (_,_) .---. |  _( )_\  ||  (_,_)___| 
| (_ o _) |  |.'   _    | > (_)  )  __ | _ _--.   | |   | | (_ o _)  |'  \   .---. 
|  (_,_)  |  ||  _( )_  |(  .  .-'_/  )|( ' ) |   | |   | |  (_,_)\  | \  `-'    / 
|  |      |  |\ (_ o _) / `-'`-'     / (_{;}_)|   | |   | |  |    |  |  \       /  
'--'      '--' '.(_,_).'    `._____.'  '(_,_) '---' '---' '--'    '--'   `'-..-'   
"""

def get_coins():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def calc_change(money, coffee_type):
    if coffee_type == "espresso":
        cost = MENU["espresso"]["cost"]
        if money < cost:
            print("Sorry that is not enough money. ")
        else:
            change = money - cost
            resources["cost"] = cost
            return round(change, 2)

def enough_money(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global money
        money += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_drink(coffee_choice, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {coffee_choice} ☕️. Enjoy!")

def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def coffee_machine():
    print(logo)
    print("MENU:")
    for item in MENU:
        print(f"{item} - ${MENU[item]["cost"]}")
        
    is_on = True
    while is_on:
        coffee_choice = input("Which coffee would you like?: ").lower()
        if coffee_choice == "off":
            is_on = False
        elif coffee_choice == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${money}")
        else:
            drink = MENU[coffee_choice]
            if check_resources(drink["ingredients"]):
                payment = get_coins()
                if enough_money(payment, drink["cost"]):
                    make_drink(coffee_choice, drink["ingredients"])

coffee_machine()
