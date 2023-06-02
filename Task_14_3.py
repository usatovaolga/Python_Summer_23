def t_s(n):
    if n==0:return
    else:
        print('*'*n)
        t_s(n-1)
        print('*'*n)
t_s(int(input("Введите число->")))