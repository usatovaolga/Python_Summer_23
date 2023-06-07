import re
s='1 122 41 33 455'
x=45
ss=input("Введите строку->")
n ='|'.join(str(i) for i in range(0,x+1))
print(re.findall(rf"\b(?:{n})\b",ss))