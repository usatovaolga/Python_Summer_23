import math

n = int(input("Введите чисто n для расчета n! ->"))
f = 1
for i in range(1, n+1):
    f = i*f
print(f"{n}! = {f}")
print(f"Проверка с помощью math.factorial = {math.factorial(n)}")