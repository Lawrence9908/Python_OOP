from item import Item
from phone import Phone

Item.instantiate_from_csv()
# print(Item.all)

item  = Item("Mango", 20)
item.name = "Apple"
print(item.name)
print(item.price)
print(item.quantity)