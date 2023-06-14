class Shape:
    def __init__(self,name, color,square=1):
        self.name = name
        self.color = color
        self.square = square
    def ins_color(self, colr):
        self.color=colr
        self.print_color()

    def print_color(self):
        print(f"Цвет {self.name} {self.color}")

    def ins_square(self,sq):
        self.square=sq

    def print_square(self):
        print(f"Площадь {self.name} {self.square}")

a = Shape('CR', 'Красный')
b = Shape('DP', 'Белый')

a.print_color()
a.ins_color('Голубой')
#a.print_color()