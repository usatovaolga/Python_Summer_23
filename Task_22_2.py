d=[(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (6, 7), (7, 8)]
d1=[(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (4, 7), (5, 8), (8, 9), (9, 10)]
r1 = d[0][0]
r2 = d[0][1]
s=0
n=0
tt=[]
def bd (d,r,s,tt):
    for i in d:
        if i==d[-1]:
            tt.append(s)
            s=0
        elif i[0]==r:
            #print(i)
            s += 1
            r1 = i[1]
            bd(d,r1,s,tt)
    return tt
print(max(bd(d1,r1,s,tt)))