class Item:
    """
    Defines a class Item
    """
    # class attribute
    pay_rate = 0.2 # discount after buying 20% of the product
    
    def __init__(self, name: str, price: float, quantity = 0):
        # Run validation to the recieved arguments
        assert price >= 0, f"price {price} is not greater than Zero"
        assert quantity >= 0, f"Qunatity {quantity} not greater that or equla to zero"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        """
        The method calculate the total of quantity

        args:
        
        return: i
        """
        return self.price * self.quantity


item1 = Item("Phone", 100, 4)
item2 = Item("Laptop", 3000, 6)

print(Item.pay_rate)
print(item1.pay_rate)
print(item2.pay_rate)