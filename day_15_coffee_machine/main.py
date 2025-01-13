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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
#Initialize the amount of money in the machine
money_in_machine = 0

#Create method to check resources
def print_resources():
    print(f"Water: {resources["water"]} \nMilk: {resources["milk"]} \nCoffee: {resources["coffee"]}")

#Method to remove resources from machine when a drink is made
def use_resources(drink_name):
    ingredients = MENU[drink_name]["ingredients"]
    resources["water"] -= ingredients.get("water", 0)
    resources["coffee"] -= ingredients.get("coffee", 0)
    resources["milk"] -= ingredients.get("milk", 0)

#Method to check if enough resources are available for the chosen drink
def check_resources(drink_name):
    inadequate_ingredients = []
    ingredients = MENU[drink_name]["ingredients"]
    if ingredients.get("water", 0) > resources["water"]:
        inadequate_ingredients.append("water")
    if ingredients.get("coffee", 0) > resources["coffee"]:
        inadequate_ingredients.append("coffee")
    if ingredients.get("milk", 0) > resources["milk"]:
        inadequate_ingredients.append("milk")
    return inadequate_ingredients

#Method to get user's coins input
def get_coins():
    total_money = 0
    total_money += int(input("How many quarters are you putting in the machine?")) * .25
    total_money += int(input("How many dimes are you putting in the machine?")) * .10
    total_money += int(input("How many nickels are you putting in the machine?")) * .05
    total_money += int(input("How many pennies are you putting in the machine?")) * .01
    return total_money

#Method to get user's choice for what they want and process accordingly
def get_user_choice():
    user_choice = input("What would you like to order today? (Espresso, Latte, Cappuccino)").lower()
    if user_choice == "report":
        print_resources()
    elif user_choice == "off":
        print("You have chosen to turn the machine off. Machine powering down...")
        return False
    elif user_choice in MENU:
        amount_paid = get_coins()
        cost = MENU[user_choice]["cost"]
        if amount_paid < cost:
            print(
                f"${round(amount_paid, 2):.2f} is not enough money for a {user_choice}. A {user_choice} costs ${round(cost, 2):.2f}.")
        else:
            missing_resources = check_resources(user_choice)
            if len(missing_resources) > 0:
                print(f"There is not enough of the following ingredient(s): {' ,'.join(missing_resources)}.")
            else:
                use_resources(user_choice)
                change_due = amount_paid - cost
                print(f"Thank you! Your change is ${round(change_due, 2):.2f}.")
    else:
        print("You entered an invalid choice. Please choose Espresso, latte, cappuccino or report.")

    return True  # Continue the loop if the machine isn't turned off

#Set the machine to "on"
machine_on = True

while machine_on:
    machine_on = get_user_choice()