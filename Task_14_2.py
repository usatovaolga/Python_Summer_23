n = int(input('Введите число ->'))
class NotNature(ValueError):
    pass
while True:
    try:
        if n>=1:
            break
        else: raise NotNature('Не натуральное')
    except:
        n = int(input("Вы ввели не натуральное число, попробуйте снова ->"))
def k_c(n):
    if n>=10:
        return n%10+k_c(n//10)
    return n
print(f"Сумма цифр натурального числа = {k_c(n)}")
