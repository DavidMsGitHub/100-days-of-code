from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

milk = 200

fulismanqana = MoneyMachine()
machine = CoffeeMaker()
menu = Menu()

espresso = MenuItem("espresso", 50, 0, 18, 1.5),
latte = MenuItem("latte", 200,  150, 24, 2.5),
cappucino = MenuItem("latte", 250,  100, 24, 3.0)

while True:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if order == "off":
        break
    elif order == "report":
        machine.report()
        fulismanqana.report()
    elif order in menu.get_items():
        order = menu.find_drink(order)
        print(order)
        if machine.is_resource_sufficient(order):
            print("Gvyofnis bro")
            fulismanqana.make_payment(order.cost)
            machine.make_coffee(order)
        else:
            print("idi naxui")

