g = open("text1.txt", 'r', encoding='utf-8')
s = g.readlines()
print(s)
g.close()
dct={}
for k in ''.join(s).lower():
    dct[k] = dct.get(k,0)+1
print(sorted(sorted(dct.items()), key=lambda item: -item[1])[:10])
