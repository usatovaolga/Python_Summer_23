def s_l(lst):
    for x in lst:
        if x%2!=0:
            yield x
lst = list(map(int,input().split()))
p = s_l(lst)
for _ in range(len(lst)):
    try:
        print(next(p),end=' ')
    except StopIteration:
        print('Stop')
        break