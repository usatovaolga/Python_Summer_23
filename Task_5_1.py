import math

n = int(input("Введите число ->"))
for x in range(n):
    for y in range(n):
        print(math.factorial(x)/(math.factorial(y)*(math.factorial(abs(x-y)))))