import data
from sandwich_maker import SandwichMaker
from cashier import Cashier

# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()


def main():
    while True:
        try:
            # 5 options
            choice = input("What would you like? (small/medium/large/off/report): ").lower()
            # Check if off first, and break the while loop
            if choice == "off":
                print("Turning off the machine.")
                break
            # Check if choice is a report, and print current resources
            elif choice == "report":
                print(f"Bread: {sandwich_maker_instance.machine_resources['bread']} slice(s)")
                print(f"Ham: {sandwich_maker_instance.machine_resources['ham']} slice(s)")
                print(f"Cheese: {sandwich_maker_instance.machine_resources['cheese']} slice(s)")
            # Check if choice is a valid choice, "small", "medium", "large"
            elif choice in recipes:
                order_ingredients = recipes[choice]["ingredients"]
                order_cost = recipes[choice]["cost"]

                if sandwich_maker_instance.check_resources(order_ingredients):
                    print("Please insert coins.")
                    total_coins = cashier_instance.process_coins()

                    if cashier_instance.transaction_result(total_coins, order_cost):
                        sandwich_maker_instance.make_sandwich(choice, order_ingredients)
                        print(f"{choice.capitalize()} sandwich is ready. Bon appetit!")
            else:
                raise ValueError("Invalid input")
        except ValueError as e:
            print(f"{e}, please try again.")


if __name__ == "__main__":
    main()
