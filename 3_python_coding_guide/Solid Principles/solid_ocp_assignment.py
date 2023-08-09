# Suppose we have a Product class that represents a generic product, and we want to calculate the
# total price of a list of products. Initially, the Product class only has a price attribute, and
# we can calculate the total price of products based on their prices.
# Now, let's say we want to add a discount feature, where some products might have a
# discount applied to their prices. To add this feature, we would need to modify the
# existing Product class and the calculate_total_price function, which violates the
# Open/Closed Principle. Redesign this program to follow the Open-Closed Principle
# (OCP) which represents “Software entities (classes, modules, functions, etc.) should be
# open for extension, but closed for modification.”


class Product:
    def __init__(self, price):
        self.price = price

    def calculated_total_price(self):
        return self.price

class DiscountedProduct(Product):
    def __init__(self, price, discount):
        super().__init__(price)
        self.discount = discount

    def calculated_total_price(self):
        total_price = self.price * (1 - self.discount)
        return total_price

def calculate_total_price(products):
    """
    Calculate the total price of a list of products.

    Parameters:
        products (list): A list of Product objects or its subclasses (e.g., DiscountedProduct).

    Returns:
        float: The total price of all products in the list.
    """
    total_price = 0
    for product in products:
        total_price += product.calculated_total_price()
    return total_price

if __name__ == "__main__":
    products = [Product(100), DiscountedProduct(500, 0.2), DiscountedProduct(750, 0.2)]
    products = [Product(100), DiscountedProduct(500, 0.2), DiscountedProduct(1000, 0.2),DiscountedProduct(1000,0.5)]

    print("Product Prices:")
    for product in products:
        print(f"Price: {product.price}")

    print("\nTotal Price:", calculate_total_price(products))
