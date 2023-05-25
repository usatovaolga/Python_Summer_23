dr = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
      'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
      'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
n = int(input("Введите число - "))
def transl(n):
    rez = ''
    for k, v in dr.items():
        while n >= v:
            rez += k
            n -= v
    return rez
print(f" {n} -> {transl(n)}")