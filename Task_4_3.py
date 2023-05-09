s1="".join(c for c in input("Введите предложение 1") if c.isalpha())
s2="".join(c for c in input("Введите предложение 2") if c.isalpha())
d1={}
d2={}
for i in s1:
    d1[i]=d1.get(i,0)+1
    print(i,'',d1[i],sep='',end=' ')
print()
for i in s2:
    d2[i]=d2.get(i,0)+1
    print(i,'',d2[i],sep='',end=' ')
print()
print(d1==d2)
