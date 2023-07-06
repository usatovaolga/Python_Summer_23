s=[0,-1]#[-1,0]#[1,1,-1]#[5,4,3,2,1]#[1,2,3,4,5]
def cin(s):
    c = 0
    for i in range(len(s)):
        for j in range(len(s)):
            if i<j and s[i]>s[j]:
                c+=1
    return c
print(cin(s))

