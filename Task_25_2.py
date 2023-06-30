s=[-1,0,1,3,5,4,7,9,10]
ss = list(map(int, input().split()))
t=ss[0]
tt=[]
for i in ss[1:]:
    if i!=t+1:
        tt.append(i)
    t=i
print(tt)

#print([s[i] for i in range(1,len(s)) if s[i-1]+1 != s[i]])
