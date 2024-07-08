import data


def report():
    water_current = data.resources["water"]
    milk_current = data.resources["milk"]
    coffee_current = data.resources["coffee"]
    money_current = data.resources["money"]
    print(f"Water: {water_current}ml")
    print(f"Milk: {milk_current}ml")
    print(f"Coffee: {coffee_current}g")
    print(f"Money: {money_current}$")

def coin_prompt():
    quarters_count = float(input("How many quarters?:"))
    dimes_count = float(input("How many dimes?:"))
    nickles_count = float(input("How many nickles?:"))
    pennies_count = float(input("How many pennies?:"))
    all_coins_calculated = (quarters_count * 0.25) + (dimes_count * 0.10) + (nickles_count * 0.05) + (pennies_count * 0.01)
    return all_coins_calculated

def check_resources(yava):
    for ingredient in data.MENU[yava]["ingredients"]:
        if data.MENU[yava]["ingredients"][ingredient] > data.resources[ingredient]:
            print(f"there is not enough {ingredient} in Coffee Machine")
            return False
    return True


def check_transaction(chosen_coffee, payment):
    if payment > data.MENU[chosen_coffee]["cost"]:
        xurda = round(payment - data.MENU[chosen_coffee]["cost"], 2)
        data.resources["money"] += data.MENU[chosen_coffee]["cost"]
        if xurda > 0:
            print(f"Here is your change ${xurda}")
        return True
    else:
        print("You inserted not enough coins")
        return False



def coffee_make(chosen_coffee):
    for ingredient in data.MENU[chosen_coffee]["ingredients"]:
        data.resources[ingredient] -= data.MENU[chosen_coffee]["ingredients"][ingredient]
    print(f"Here is your {chosen_coffee}")


def main():
    while True:
        command = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if command == "off":
            break
        elif command == "report":
            report()
        elif command in data.MENU:
            if check_resources(command):
                x = coin_prompt()
                if check_transaction(command, x):
                    coffee_make(command)
        else:
            print("idi naxui")



main()







