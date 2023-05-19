s = [[1,2,3],[2,334,24,6],[8,6]]
t=[1,2,3]
s2=[]
for i in s:
    t=sorted(i,reverse=True)
    s2.append(t)
print(s2)
print(sorted(s2,key= lambda s:len(''.join(map(str,s)))))
#print(sorted(t,reverse=True))