from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#instantiate menu object
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    user_choice = input(f"What drink would you like to order today? Your choices are {menu.get_items()}")
    if user_choice == "report":
        coffee_maker.report()
    else:
        chosen_drink = menu.find_drink(user_choice)
        sufficient_resources = coffee_maker.is_resource_sufficient(chosen_drink)
        if sufficient_resources:
            payment_adequate = money_machine.make_payment(chosen_drink.cost)
            if payment_adequate:
                coffee_maker.make_coffee(chosen_drink)
