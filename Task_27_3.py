s=['a','b','3',['y','u'],'y']
n=0
def ss(s,n):#n4 i'y'
    if len(s)==0:return n
    for i in s:
        if type(i)!=list and i==s[-1]:return n+1
        elif type(i)!=list: n += 1
        # elif type(i)==list and i==s[-1]: return ss(i,n+1)
        else: return ss(i,n+1)

print(ss(s,n))

####
def nel(lst):
    count=0
    for i in lst:
        if type(i)==list:
            count+=nel(i)+1
        else:
            count +=1
    return count

print(nel([1,2,[3,4]]))