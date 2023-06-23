m=[[10,20,30],
   [5,1,80],
   [90,5,70]]
t=0
tt=0
s=m[0][0]
def  finding_way(mm,t,tt,s):
    n=len(mm)
    #print(t, tt)
    #print(mm[t][tt + 1],mm[t + 1][tt])
    if mm[t][tt+1]>mm[t+1][tt]:
        t+=1
    else: tt+=1
    s+=mm[t][tt]
    print(s)
    #print(t,tt)
    while t<n-1 or tt<n-1:
        print(t,tt)
        print(n)
        finding_way(mm,t,tt,s)
    else: return print('конец')

finding_way(m,t,tt,s)


#