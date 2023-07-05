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
#############
# class Item:
#     def __init__(self,name,price,quantity):
#         self._name=name
#         self.price = price
#         self.quantity=quantity
#
#     @property
#     def total(self):
#         return self.price*self.quantity
#
#     @property
#     def name(self):
#         return self._name.titel()

#########

# class Item:
#     def __init__(self,name,price,quantity):
#         self.name=name
#         self.price = price
#         self.quantity=quantity
#
#     def __getattribute__(self, attr):
#         if attr=='name':
#             return object.__getattribute__(self,attr).titel()
#         elif attr=='price':
#             return 2*object.__getattribute__(self,attr)
#         else:
#             return object.__getattribute__(self,attr)
#
#     def __getattr__(self, attr):
#         if attr=='total':
#             return self.price*self.quantity
#         else:
#             raise AttributeError