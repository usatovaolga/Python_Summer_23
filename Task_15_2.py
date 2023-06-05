import re
tt=input('Введите строку ->')
def ff(s):
    reg = r'\b[АВСЕНКМОРТХABCEHKMOPTX]\d{3}[АВСЕНКМОРТХABCEHKMOPTX]{2}[1]?78\b'
    d = re.findall(reg, s)
    return d
print(ff(tt))