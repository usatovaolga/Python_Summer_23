import re
s="+7(812)654-1234, +7(921)987-12-12, 8(921)987-12-12"
tt=input('Введите строку ->')
def ff(s):
    r = re.findall(r'[+]7\((?:812|921)\)\d{3}-\d{2}[-]?\d{2}', s)
    return r
print(ff(tt))