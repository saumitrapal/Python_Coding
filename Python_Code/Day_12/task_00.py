# Coffee machine program
MANU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "cost": 1.5
    },
    
    "latte": {
        "ingredients": {
            "water": 50,
            "milk": 150,
            "coffee": 18
        },
        "cost": 2.5
    },
    
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 10,
            "coffee": 24
        },
        "cost": 3.0
    }
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}


def is_resource_sufficient(order_ingredents):
    for item in order_ingredents:
        if order_ingredents[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False   
    return True


def procces_coins():
    print("Please insert coins: ")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.10
    total += int(input("how many nickel?: ")) * 0.05
    total += int(input("how many penny?: ")) * 0.01
    return total


def is_transaction_successful(money_recived, drink_cost):
    if money_recived >= drink_cost:
        change = round((money_recived - drink_cost), 2)
        print(f"Here is your change: {change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. here is your refunded money!")
        return False


def make_coffee(drink_name, order_ingredents):
    for item in order_ingredents:
        resources[item] -= order_ingredents[item]
    print(f"Here is your {drink_name}")
    
    
profit = 0
is_on = True


while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"coffee: {resources["coffee"]}")
        print(f"Money: ${profit}")
    else:
        drink = MANU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payments = procces_coins()
            if is_transaction_successful(payments, drink["cost"]):
                make_coffee(choice, drink["ingredients"])

