# Write a Python function calculate_total_cost that calculates the total
# cost of items purchased from a store. The function should accept multiple keyword
# arguments, where the key is the item name, and the value is the item's price. The
# function should return the total cost of all items

def calculate_total_cost(**kwargs):
    """
        Calculate the total cost based on the items and their corresponding prices.

        Parameters:
        **kwargs: keyword arguments
         Each keyword argument represents an item and its price.

        Returns:
            float or int
                The total cost obtained by summing all the prices of the items.
    """
    cost = 0
    for item,price in kwargs.items():
        cost += price
    return cost

def main():
    print(calculate_total_cost(rose = 100,balloon = 300,cake= 800))
    print(calculate_total_cost(rose = 100))
    

if __name__ == '__main__':
    main()