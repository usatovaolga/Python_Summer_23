def t_s(n):
    if n==0:return
    elif n==1:
        print('*' * n)
    else:
        print('*'*n)
        t_s(n-1)
        print('*'*n)
t_s(int(input("Введите число->")))