from item import Item


class Phone(Item):
    all = []

    def __init__(self, name: str, price: float, quantity=0, broken_phone = 0):
        assert broken_phone >= 0, f"Broken phone {broken_phone} must be zero or grater than zero"
        self.broken_phone  =broken_phone
        super().__init__(name, price, quantity)