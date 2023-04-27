i1 = int(input("Введите первое число"))
i2 = int(input("Введите второе число"))
summ = i1+i2
diff = i1-i2
mult = i1*i2
quot = i1/i2
qoutfl = i1//i2
print(f" Сумма = {summ} , Разница = {diff}, Произведение = {mult}, Деление = {quot}, Целочисленное деление = {qoutfl}")

if summ>diff:    x=summ
else:    x=diff
if mult>quot: y=mult
else: y=quot
if x>y: t=x
else: t=y
if t>qoutfl: print(t)
else: print(qoutfl)