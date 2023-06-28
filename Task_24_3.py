ss='(()())()(())'
sinp=input("Введите строку ->").replace(" ", "")
def skobka(s):
    t = 0
    for i in s:
        if t==-1: return False
        elif i=='(': t+=1
        else: t-=1
    if t != 0: return False
    else: return True
print(skobka(sinp))