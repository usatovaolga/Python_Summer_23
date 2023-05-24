import calendar
from datetime import date
g = int(input("Введите год - "))
n=0
print("Список дат бесплатного входа в Эрмитаж")
for m in range(1,13):
    n = 0
    for d in range(1,28):
        if calendar.weekday(g,m,d)==3:
            n+=1
            if n==3:
                print(date(g,m,d))

