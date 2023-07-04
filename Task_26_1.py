def diffs(s1,s2):
    n=0
    for i,j in zip(s1,s2):
        if i!=j:
            n+=1
    if s1 in s2 or s2 in s1:
        return True
    if n>1:
        return False
    if len(s1)!=len(s2):return False
    else:return True

s1=input('Введите первую строку->')
s2=input('Введите вторую строку->')
r=len(s1)-len(s2)
if abs(r)>1:
    print(False)
else: print(diffs(s1,s2))