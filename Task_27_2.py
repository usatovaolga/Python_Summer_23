##шаблон прототип
import copy
class Item:
    def __init__(self,name,price,quantity):
        if name:
            self.name=name.title()
        self.price = price
        self.quantity=quantity
        self.total = price*quantity

a=Item('a',500,5)
b=Item('B',1000,3)
print(a.name)
print(a.total)