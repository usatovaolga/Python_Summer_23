
class NotNature(ValueError):
    pass
while True:
    try:
        n = int(input('Введите число ->'))
        if n<1:raise NotNature('Не натуральное')
        else: break
    except:
        print("Вы ввели не натуральное число, попробуйте снова ->")
def k_c(n):
    if n>=10:
        return 1+k_c(n/10)
    return 1
print(f"Кол-во цифр натурального числа = {k_c(n)}")
