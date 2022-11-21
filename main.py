import csv

class Item:
    """
    Defines a class Item
    """
    # class attribute
    pay_rate = 0.2 # discount after buying 20% of the product
    all = []
    def __init__(self, name: str, price: float, quantity = 0):
        # Run validation to the recieved arguments
        assert price >= 0, f"price {price} is not greater than Zero"
        assert quantity >= 0, f"Qunatity {quantity} not greater that or equla to zero"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            print(item)


    def __repr__(self):
        return f"Item ('{self.name}','{self.price}','{self.quantity}')"

print(Item.all)