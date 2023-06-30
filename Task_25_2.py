s=[-1,0,1,3,5,4,7,9,10]
t=s[0]
tt=[]
for i in s[1:]:
    if i!=t+1:
        tt.append(i)
    t=i
print(tt)