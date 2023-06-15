import itertools
s=[50,100,200,500,1000,5000]
res=[]
for x in range(1,7):
    for i in itertools.combinations(s,x):
        res.append(sum(i))
print(f"Все возможные суммы: {sorted(res)}")