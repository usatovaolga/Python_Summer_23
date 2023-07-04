n=int(input('Введите число n от 1 до 18 ->'))
t=(n+1)//2
m=[ [0]*n for i in range(n) ]
def ttt(m,n1,n2,t):#1 (m,0,7,1) #2 (m,1,6,2) #3 (m,2,5,3) #4 (m,3,6,4) #5 (m,4,5,5)
    for i in range(n1,n2):
        for j in range(n1,n2):
            if i == n1 or j == n1 or i == n2 - 1 or j == n2 - 1:
                m[i][j] = t
            else:ttt(m,n1+1,n2-1,t+1)
    return m
y=ttt(m,0,n,1)
for i in range(n):
   print(*y[i])