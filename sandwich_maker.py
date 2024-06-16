from data import recipes

class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        #####
        for ingredient, amount in ingredients.items():
            if self.machine_resources.get(ingredient, 0) < amount:
                print(f"Sorry, there is not enough {ingredient}.")
                return False
        return True


    def make_sandwich(self, sandwich_size, order_ingredients):
        ########
        if sandwich_size in recipes:
            for ingredient, amount in order_ingredients.items():
                self.machine_resources[ingredient] -= amount

