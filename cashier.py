class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        ###
        while True:
            try:
                dollar = int(input("How many dollars?: "))
                half_dollar = int(input("How many half dollars?: "))
                quarter = int(input("How many quarters?: "))
                nickel = int(input("How many nickels?: "))
                if (dollar < 0 or half_dollar < 0 or quarter < 0 or nickel < 0):
                    raise ValueError("Negatives not allowed")
                break
            except ValueError as e:
                print(f"Invalid input, {e}, please try again.")

        total = dollar + (half_dollar * .5) + (quarter * 0.25) + (nickel * 0.05)
        return total


    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        ##
        if (coins < cost):
            #Print insufficient fund
            print("Insufficient funds.")
            return False
        #Print change in this method
        print(f"Change: {coins - cost}")
        return True
