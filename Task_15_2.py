import re
tt=input('Введите строку ->')
def ff(s):
    reg = r'\b[A-ZА-Я]\d{3}[A-ZА-Я]{2}[1]?78\b'
    d = re.findall(reg, s)
    return d
    r = re.sub(d,'',s)
    ff(r)
print(ff(tt))