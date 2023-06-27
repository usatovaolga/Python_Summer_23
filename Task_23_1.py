s='aabbccddcc'
m=''
ss = input('Введите строку ->')
for i in range(len(ss)):
    for j in range(len(ss),i,-1):
        if ss[i:j]==ss[i:j][::-1]:
            if len(m)<len(ss[i:j]):
                m=ss[i:j]

print(m)
