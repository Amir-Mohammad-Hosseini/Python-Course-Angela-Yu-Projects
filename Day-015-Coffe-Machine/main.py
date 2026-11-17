from data import MENU
from data import resources

def show_report(collected_money):
    print(f"Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g\nMoney: ${collected_money}")

def calculate_total_money (quarters_count, dimes_count, nickles_count, pennies_count):
    total_money = (quarters_count * 0.25) + (dimes_count * 0.10) + (nickles_count * 0.05) + (pennies_count * 0.01)
    return round(total_money ,2)

def check_resources_enough(user_ingredients):
    is_resources_enough = True
    for ingredient in user_ingredients:
        selected_item_count = user_ingredients[ingredient]
        if selected_item_count > resources[ingredient]:
            print(f"Sorry, there is not enough {ingredient}")
            is_resources_enough = False
    return is_resources_enough

def calculate_coins_total():
    print("Please insert coins.")

    quarters_count = int(input("How many quarters?"))
    dimes_count = int(input("How many dimes?"))
    nickles_count = int(input("How many nickles?"))
    pennies_count = int(input("How many pennies?"))

    return  calculate_total_money(quarters_count, dimes_count, nickles_count, pennies_count)

def check_paid_money(recieved_money , drink_cost,user_ingredients , selected_item):
    if drink_cost > recieved_money:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        if drink_cost < recieved_money:
            print(f"Here is ${round((recieved_money - drink_cost), 2)} dollars in change.")
        print(f"Here is your {selected_item}. Enjoy!")

        for resource in resources:
            if resource in user_ingredients:
                resources[resource] -= user_ingredients[resource]
        return True

def coffe_machine():
    collected_money = 0
    is_order_continue = True
    while is_order_continue:
        user_prompt = input("What would you like? (espresso/latte/cappuccino):").strip().lower()

        if user_prompt == "report":
            show_report(collected_money)
        elif user_prompt == "off":
            is_order_continue = False
        else :
            user_selected_item = MENU[user_prompt]

            is_resources_enough = check_resources_enough(user_selected_item["ingredients"])

            if is_resources_enough :

                paid_money = calculate_coins_total()
                selected_item_cost = user_selected_item["cost"]

                is_money_enough = check_paid_money(paid_money , selected_item_cost , user_selected_item["ingredients"] , user_prompt)
                if is_money_enough:
                    collected_money += selected_item_cost
    return is_order_continue

is_order_continue = coffe_machine()

if not is_order_continue:
    print("Coffee Machine turned off.")