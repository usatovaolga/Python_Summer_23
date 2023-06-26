import itertools
def p(sp):
    t=[]
    r =list(itertools.permutations(sp))
    for i in r:
        t.append(int(''.join(map(str,i))))
    return t
s= [1,21,3]
print(max(p(s)))