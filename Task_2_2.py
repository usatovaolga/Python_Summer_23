lst = []
n = int(input("Введите кол-во элементов в списке ->"))
for i in range(n):
    lst.append(int(input("Введите элемент списка ->")))
lst.sort()
print(lst[0])

