import re
s='-5 -3 0 1 3 5 10 11 39 46 1006 -100'
x=45
ss=input("Введите строку->")
n ='|'.join(str(i) for i in range(0,x+1))
print(re.findall(rf"\b(?<![-])(?:{n})\b",ss)) #проверка, если перед числом нет - ,тогда проверяем шаблон дальше