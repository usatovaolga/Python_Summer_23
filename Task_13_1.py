def p():
    while True:
        yield i*(-1) if i%2==0 else i
posl=p()
for i in range(1,int(input())+1):
    print(next(posl), end=',')