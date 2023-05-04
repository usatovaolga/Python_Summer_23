n = int(input("Введите число ->")) #133244459
nL = list(str(n))
counter = 0
print("Кол-во цифр в записи введенного числа")
for i in range(10):
    for j in nL:
        if int(j)==i: counter+=1

    print(f"{i} - {counter}")
    counter = 0