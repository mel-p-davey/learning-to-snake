from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

machine_on = True

while machine_on == True:
    order = input("What would you like? " + menu.get_items()+"report/off?:  ")
    if order == "report":
        profit = money_machine.report()
        resources = coffee_maker.report()
    elif order == "off":
        print("Goodbye, see you again soon")
        machine_on = False
    elif order == "latte" or order == "cappuccino" or order == "espresso":
        drink = menu.find_drink(order)
        can_make = coffee_maker.is_resource_sufficient(drink)
        if can_make == True:
            print("We can do that!")
            price = drink.cost
            print(f"The cost of your drink is {price}. How would you like to pay?  ")
            pay = money_machine.make_payment(price)
            if pay == False:
                print("Sorry, that is not enough money.")
            else:
                make_it = coffee_maker.make_coffee(drink)
    else:
        print("Sorry, we don't have that on the menu.")
        
            

