s=(input()).split()
d={x: s[x] for x in range(0,3)}
if d[1]=='+':
    print(int(d[0])+int(d[2]))
elif d[1]=='-':
    print(int(d[0])-int(d[2]))
elif d[1]=='*':
    print(int(d[0])*int(d[2]))
elif d[1] == '/':
    if int(d[2]) == 0: print("Деление на 0")
    else: print(int(d[0]) // int(d[2]))
else: print("Простой калькулятор с таким не справится((")
