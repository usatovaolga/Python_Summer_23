s=[0,1,1,0]
def sort_v(sp):
    for i in range(len(sp)):
        t=i
        for j in range(t + 1, len(sp)):
            if sp[j] < sp[t]:
                t = j
        sp[i], sp[t] = sp[t], sp[i]
    return sp
print(*sort_v(s))