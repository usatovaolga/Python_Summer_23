i1 = int(input("Введите первое число"))
i2 = int(input("Введите второе число"))
summ = i1+i2
diff = i1-i2
mult = i1*i2
quot = i1/i2
qoutfl = i1//i2
print(f" Сумма = {summ} , Разница = {diff}, Произведение = {mult}, Деление = {quot}, Целочисленное деление = {qoutfl}")

if summ > diff:
    f = summ
    s = diff
else: f = diff
s = summ
if mult > f:
    s = f
    f = mult
elif mult > s:
    s = mult
if quot > f:
    s = f
    f = quot
elif quot > s:
    s = quot
if qoutfl > f:
    s = f
    f = qoutfl
elif qoutfl > s:
    s = qoutfl
print(s)
print(f)
