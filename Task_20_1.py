import re
from datetime import datetime
q={
    'Pitcher':[('Американо',160),('Капучино',200),('Эспрессо',150),('Двойной эспрессо',190),('Баноффи',250)],
    'Кофеварим':[('Американо',140),('Капучино',170),('Латте',200),('Блины',250),('Хот-дог',300)],
    'Британские пекарни':[('Американо',190),('Капучино',230),('Латте',250),('Эспрессо',180),('Эклер',230)]
}
class Client:
    itog=[]

    def __init__(self, id):
        self.id =id
    def analysis(self,z):
        for i in z:
            self.itog.append(i)
    def choice_c(self):
        itog_t = []
        ch=admin.choice()
        t_way_pay=admin.buy(ch)
        print("Приятного аппетита. Спасибо за покупку")
        for i in ch:
            t=i+(t_way_pay,)
            itog_t.append(t)
        self.analysis(itog_t)

class Admin:
    def __init__(self):
        t=[]
    def menu(self,s):
        if s=='D':
            for k, v in q.items():
                print("Меню «" + k + '»')
                for i in v:
                    print(*i)
                print()
        else:
            for k, v in q.items():
                if k == s:
                    print("Меню «" + k + '»')
                    for i in v:
                        print(*i)
                    print()
    def check(self,place,poz):
        date_now=datetime.now()
        itod_order=[]
        r=re.findall(r'\b\w+\b',poz)
        for i in r:
            for k,v in q.items():
                if k==place:
                    for p in v:
                        if i == p[0].lower():
                            t=(place,p[0],p[1],date_now)
                            itod_order.append(t)
        return itod_order
    def buy(self,checks):
        sum_pay=0
        for i in checks:
            sum_pay+=int(i[2])
        way_pay=input(f"Итого к оплате {sum_pay} рублей. Выберите способ оплаты 1 - Безналичный расчет, 2 - Расчет наличными (введите цифру):")
        match way_pay:
            case '1': return 'Карта'
            case '2': return 'Налич'
            case _: return 'Нет оплаты'
    def choice(self):
        m = []
        for k, v in q.items():
            m.append(k)
        sel = input(
            f"Куда бы вы хотели пойти {', '.join(m)}? Если хотите ознакомиться с меню введите 1 -")  # Кофе, кофе и пироженное, завтрак
        if sel == '1':
            self.menu('D')
            sel = input("Какое место выбираете? ")
        print(f"         Вы выбрали {sel}")
        self.menu(sel)
        s = input("Чем хотите себя порадовать?")
        return self.check(sel,s.lower())





admin = Admin()
id1 = Client('id1')
id1.choice_c()
id1.choice_c()
