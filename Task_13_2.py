def p(n):
    for i in range(n):
        d=len(str(i))
        s = d // 2
        if d==1 and i!=0:
            yield i
        elif d%2==0 and str(i)[:s] == str(i)[s:][::-1]:
            yield i
        elif d%3==0 and str(i)[:s] == str(i)[s+1:][::-1]:
            yield i
posl=p(int(input('Введите число ограничения->')))
for b in posl:
    print(b,end=' ')


