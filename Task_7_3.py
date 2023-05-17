n = int(input("Введите размер массива, строк ="))
m = int(input("Введите размер массива, столбцов ="))
A = [[int(input("Введите число")) for j in range(n)] for i in range(m)]
print(A)
l = len(A)
#print(l)
A1 = []
for i in range(l):
    for j in A[i]:
        A1.append(j)
A1sort=sorted(A1)
#print(A1sort)
print(A1sort[n*m-3:])
