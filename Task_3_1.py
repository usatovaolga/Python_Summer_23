zpS = 0
counter = 0
while True:
    zp=int(input("Введите зарплату сотрудника (окончание ввода 0) ->"))
    if zp == 0: break
    zpS+=zp
    counter+=1
if zp==0:
    print(f"Окончание ввода")
else:
    print(f"Средняя зарплата сотрудников = {zpS/counter}")