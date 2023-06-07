s = 'Институт точной механики оптики'
import re
ss=input('Введите строку ->')
def ff(s):
    poz = s.group()
    return poz[:1].upper()
print(re.sub(r"\w+",ff,s).replace(' ',''))