import pandas as pd
df = pd.DataFrame([[1, 3, 'коньки',23],
                   [2, 'весна', 'зелень',4],
                   [3, 'лето', 'жара',3],
                   [4, 'осень','листва',9]])
s=0
for k,v in df.items():
    for i,j in v.items():
        if type(j)==int:
            s+=j
print(s)
