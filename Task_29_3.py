s1='aadd'
s2='rrtt'
def ismrf(s1,s2):
    if len(s1)!= len(s2):return False
    d = {}
    s = set()
    for i in range(len(s1)):
        x,y = s1[i],s2[i]
        if x not in d:
            d[x] = y
            if y in s: return False
            s.add(y)
        else:
            if d[x]!= y: return False
    return True
print(ismrf(input('1 строка ->'),input('2 строка ->')))