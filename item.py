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
        self.__name = name
        self.__price = price
        self.__quantity = quantity
        # Actions to execute
        Item.all.append(self)
 
    @property
    # Propert Decorator  = Read-Only Attribute
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        if len(name) > 10:
            raise Exception("The name is too long")
        else: 
            self.__name = name


    @property
    def price(self):
        return self.__price

    def apply_discount(self):
        self.price = self.__price * self.pay_rate

    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value

    
    @property
    def quantity(self):
        return self.__quantity

    def calculate_total_price(self):
        return self.__price * self.__quantity
    

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            # print(item)
            Item(
                name = item.get("name"),
                price = float(item.get("price")),
                quantity = int(item.get("quantity")), 
            )


    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        # For i.e: 5.0, 10.0
        if isinstance(num, float):
            # count out the float that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__} ('{self.name}','{self.price}','{self.quantity}')"
    
    
    def __connect(self, connecting):
        pass

    def __prepare_body(self):
        return f"""
        Hello Someone
        We have {self.name} {self.quantity} times
        Regards, Lawrence Mugwena
        """
    def __send(self):
        pass
    

    def send_email(self):
        self.__connect("")
        self.__prepare_body()
        self.__send()