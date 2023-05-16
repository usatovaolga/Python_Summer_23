
y=[]
str1= input("Введите строку-")
n=int(input("Введите шаг-"))
def code(string, n):
    s = 'abcdefghijklmnopqrstuvwxyz'
    for i in string:
        if i in s:
            t=s[(s.find(i)+n)%len(s)]
            y.append(t)
        else:
            y.append(i)
    print(f"Зашифрованная строка- {''.join(y)}")
code(str1,n)