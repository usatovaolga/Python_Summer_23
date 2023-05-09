n = int(input("Введите значение ->"))
zz = [[0]*n for i in range(n)]
sh = 1
x=0
y=-1
sh_s=0#шаг по строке
sh_c=1#шаг по колонке
len=len(str(n*n))
while sh <= n*n:
    if 0<=x+sh_s<n and 0<=y+sh_c<n and zz[x+sh_s][y+sh_c]==0:
        x+=sh_s
        y+=sh_c
        zz[x][y]=sh
        sh+=1
    else:
        if sh_c==1:
            sh_c=0
            sh_s=1

        elif sh_s==1:
            sh_c=-1
            sh_s=0

        elif sh_c==-1:
            sh_c=0
            sh_s=-1

        elif sh_s == -1:
            sh_c = 1
            sh_s = 0

for i in zz:
    for j in i:
        print(str(j).rjust(len),end=' ')
    print()


