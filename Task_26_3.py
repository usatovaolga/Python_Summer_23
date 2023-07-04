class Pers:
    def __init__(self,age):
        self.__age=age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,age):
        if age<1 or age>100:
            print('Недопустимый возраст')
        else: self.__age=age
    @age.deleter
    def age(self):
        del self.__age

p = Pers(1)
p.age=int(input('Возраст ->'))
