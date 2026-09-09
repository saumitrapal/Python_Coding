from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

item = Menu()   #get_items(self), find_drink(self, order_name), make_coffee(self, order)
coffee_maker = CoffeeMaker() #report(self), is_resource_sufficient(self, drink)
money_machine = MoneyMachine()   #report(self), process_coins(self), make_payment(self, cost)



is_on = True
# print(f"Choose Your Drink: {item.get_items()}")

while is_on:
    user_choice = input("Choose which type of coffee you want(latte/ espresso/ cappuccino): ")
    
    if user_choice == "off":
        is_on = False
    elif user_choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif user_choice not in item.get_items():
        print(f"Sorry! choose only: {item.get_items()}")
    else:
        drink = item.find_drink(user_choice)
        # print(drink)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
    